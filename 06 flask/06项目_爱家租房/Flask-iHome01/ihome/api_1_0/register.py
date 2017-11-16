# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入蓝图对象api
from . import api
# 导入captcha扩展,实现图片验证码的生成
from ihome.utils.captcha.captcha import captcha
# 导入redis数据库实例
from ihome import redis_store,constants,db
# 导入flask内置的模块
from flask import current_app,jsonify,make_response,request,session
# 导入自定义状态码
from ihome.utils.response_code import RET
# 导入正则模块
import re
# 导入random模块
import random
# 导入云通信接口
from ihome.utils import sms
# 导入模型类User
from ihome.models import User

@api.route('/imagecode/<image_code_id>',methods=['GET'])
def generate_image_code(image_code_id):
    """
    生成图片验证码
    1/导入扩展captcha,生成 图片验证码,name,text,image
    2/存储图片验证码内容
    3/返回图片验证码
    :param image_code_id:
    :return:
    """
    # 生成图片验证码 获得 图片名称 验证码字符串 图片对象
    name,text,image = captcha.generate_captcha()
    # 保存图片验证码的内容 到缓存当中
    try:
        redis_store.setex("ImageCode_" + image_code_id,constants.IMAGE_CODE_REDIS_EXPIRES,text)
    except Exception as e:
        # 记录日志
        current_app.logger.error(e)
        # 传入key value 转为json后返回
        return jsonify(errno=RET.DBERR,errmsg="保存图片验证码失败")
    else:
        # 使用响应对象返回图片验证码
        response = make_response(image)
        return response



@api.route('/smscode/<mobile>',methods=['GET'])
def send_sms_code(mobile):
    """
    发送短信:获取参数/校验参数/查询数据/返回结果
    1/获取参数,mobile,text,id
    2/校验参数完整性
    3/校验手机号,正则校验手机号格式
    4/获取本地存储的真实图片验证码,校验查询结果
    5/删除图片验证码
    6/比较图片验证码是否一致
    7/构造短信验证码,random模块
    8/在redis中缓存短信验证码
    9/调用云通信接口,发送短信
    10/保存发送结果,返回前端结果
    :param mobile:
    :return:
    """
    # 获取参数,图片验证码和图片验证码编号
    image_code = request.args.get("text")
    image_code_id =request.args.get("id")
    # 校验参数完整性
    # if mobile and image_code and image_code_id:
    # any
    # 检验 所有参数 是否都获取到了
    if not all([mobile,image_code,image_code_id]):
        return jsonify(errno=RET.PARAMERR,errmsg="参数缺失")
    # 校验手机号
    if not re.match(r"^1[34578]\d{9}$",mobile):
        return jsonify(errno=RET.PARAMERR,errmsg="手机号格式错误")
    # 从缓存中获取真实的图片验证码
    try:
        real_image_code = redis_store.get("ImageCode_" + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="获取图片验证码失败")
    # 校验查询结果
    if not real_image_code:
        return jsonify(errno=RET.DATAERR,errmsg="图片验证码过期")
    # 删除图片验证码
    try:
        redis_store.delete("ImageCode_" + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
    # 比较图片验证码
    if real_image_code.lower() != image_code.lower():
        return jsonify(errno=RET.DATAERR,errmsg="图片验证码不一致")

    # 检验用户是否已经注册
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno =RET.DBERR , errmsg='数据库链接错误')
    else :
        if user is not None:
            return jsonify(errno=RET.DBERR,errmsg='手机号已注册')


    # 生成短信验证码内容
    sms_code = "%06d" % random.randint(0,999999)
    # 保存短信验证码到redis中
    try:
        redis_store.setex("SMSCode_" + mobile,constants.SMS_CODE_REDIS_EXPIRES,sms_code)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="保存短信验证码失败")

    # 调用云通信接口,准备发送短信
    try:
        ccp = sms.CCP()
        # 发送短信的模板方法
        result = ccp.send_template_sms(mobile,[sms_code,constants.SMS_CODE_REDIS_EXPIRES/60],1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR,errmsg="短信发送异常")
    # 判断发送短信结果
    # if result = 0:
    if 0 == result:
        return jsonify(errno=RET.OK,errmsg="短信发送成功")
    else:
        return jsonify(errno=RET.THIRDERR,errmsg="短信发送失败")


@api.route('/users',methods=['POST'])
def register():
    '''
    用户注册:
    1 获取参数 mobile sms_code poassword 手机号 短信验证码 密码
            方法: get_json()
    2 校验参数 是否存在
    3 进一步获取详细的参数信息
    4 校验参数的完整性
    5 校验手机号格式
    6 校验短信验证码 获取真实的短信验证码
    7 比较短信验证码
    8 使用模型类 存储用户信息 提交数据到数据库
    9 缓存用会信息到redis中
    10 返回注册结果
    '''
    # 获取前端发送的post参数
    user_data = request.get_json()
    # 判断参数是否存在
    if not user_data:
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')

    # 进一步获取参数信息
    mobile = user_data.get('mobile')
    sms_code = user_data.get('sms_code')
    password = user_data.get('password')

    # 判断参数完整性
    if not all([mobile,sms_code,password]) :
        return jsonify(errno=RET.PARAMERR,errmsg='参数缺失')

    # 校验手机号
    if not re.match(r'^1[34578]\d{9}$',mobile) :
        return jsonify(errno=RET.PARAMERR,errmsg='手机号错误')
    # 获取本地短信验证码
    try :
        real_sms_code = redis_store.get('SMSCode_'+mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='获取短信验证码失败')
    # 校验查询结果
    if not real_sms_code:
        return jsonify(errno=RET.DATAERR,errmsg='短信验证码过期')
    # 比较短信验证码
    if real_sms_code != str( sms_code ) :
        return jsonify(errno=RET.DATAERR,errmsg='短信验证码错误')
    # 删除缓存中短信验证码
    try:
        redis_store.delete("SMSCode_"+mobile)
    except Exception as e:
        current_app.logger.error(e)

    # 存储用户信息
    user = User(name=mobile , mobile=mobile)
    user.password = password
    try :
        # 提交到数据库
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        # 数据提交失败 回滚
        db.session.rollback()
        return jsonify(errno=RET.DBERR,errmsg='保存用户信息错误!')

    # 缓存用户信息到redis中
    session['user_id'] = user.id
    session['name'] = mobile
    session['mobile'] = mobile
    # 返回结果
    return jsonify(errno=RET.OK,errmsg='注册成功',data=user.todict())







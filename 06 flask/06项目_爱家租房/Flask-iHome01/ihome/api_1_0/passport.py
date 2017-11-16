#coding:utf8
# 导入蓝图
from . import api
from flask import request,jsonify,current_app,session,g
# 导入自定义状态吗
from ihome.utils.response_code import RET
import re
# 导入用户模型类
from ihome.models import User
# 导入登陆验证装时期
from ihome.utils.commons import login_required
# 导入数据库
from ihome import db
# 导入骑牛运借口
from ihome.utils.image_storage import storage
from ihome import constants

@api.route('/sessions',methods=["POST"])
def login():
    '''
    用户登陆:
        1 获取参数 get_json()
        2 校验参数存在
        3 获取详细参数信息 mobile password
        4 校验参数的完整性
        5 校验手机号格式
        6 根据手机号进行查询 保存查询对象
        7 校验查询结果,user存在 密码正确 返回错误信息
        8 缓存用户信息 user.id name mobile
        9 返回结果 user.id
    '''
    # 1 获取post请求的json数据
    user_data = request.get_json()
    # 2 校验参数存在
    if not user_data :
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')
    # 3 获取详细参数信息
    mobile = user_data.get('mobile')
    password = user_data.get('password')
    # 4 校验参数的完整性
    if not all([mobile,password]):
        return jsonify(errno = RET.PARAMERR,errmsg='缺失参数')
    # 5 校验手机号格式
    if not re.match(r'^1[34578]\d{9}$',mobile):
        return jsonify(errno=RET.DATAERR,errmsg='手机号格式错误')
    # 6 查询数据库 获取用户信息
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.erro(e)
        return jsonify(errno=RET.DBERR,errmsg='查询用户信息失败')
    # 7 校验查询结果和密码
    if user is None or not user.check_password(password):
        return jsonify(errno=RET.DATAERR,errmsg='用户名或密码错误')
    # 8 缓存用户信息 返回注册结果
    session['user_id'] = user.id
    session['name'] = mobile
    session['mobile'] = mobile
    return jsonify(errno=RET.OK,errmsg='ok',data={'user_id':user.id})


@api.route('/user',methods=['GET'])
@login_required
def get_user_profile():
    '''
    获取用户信息
        1 获取参数用户id 通过g变量获取用户id
        2 根据用户id 查询数据库 保存查询结果
        3 校验查询结果 无效操作
        4 返回结果 user.to_dict()

    '''
    # 获取用户id
    user_id = g.user_id
    # 查询数据库
    try:
        user = User.query.filter_by(id = user_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='查询用户信息失败')
    # 校验查询结果
    if user is None :
        return jsonify(errno=RET.DATAERR,errmsg='无效操作')
    # 返回结果
    return jsonify(errno=RET.OK,errmsg='OK',data=user.to_dict())

@api.route('/session',methods=['DELETE'])
@login_required
def logout():
    '''
    退出登陆
    '''
    session.clear()
    return jsonify(errno=RET.OK,errmsg='OK')


api.route('/user/name',methods=['POST'])
@login_required
def change_user_name():
    '''
    修改用户名
    1 获取用户id,g变量
    2 获取参数 get_json() name
    3 校验参数存在
    4 判断name字段 存在
    5 查询数据库 修改用户名信息 根据user.id查询
    6 更新用户缓存
    7 返回结果 data = {'name':name}
    '''
    # 获取用户id
    user_id = g.user_id
    # 获取用户put 请求发送来的参数
    user_data = request.get_json()
    # 判断参数是否存在
    if not user_data:
        return jsonify(errno=RET.PARAMERR,errmsg='缺少错误')
    # 获取详细的参数信息
    name = user_data.get('name')
    # 校验参数
    if not name:
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')
    # 查询数据库 更新数据
    try:
        User.query.filter_by(id=user_id).update({'name':name})
        db.session.commit()
    except Exception as e :
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR,errmsg='数据库错误')

    # 更新缓存中的用户服信息
    session['name'] = name
    return jsonify(errno=RET.OK,errmsg='修改成功',data={'name':name})


@api.route('/user/avatar',methods=['POST'])
@login_required
def save_user_avator():
    '''
    上传头像
    1 获取用户信息
    2 获取头像文件 request.files.get('avatar')
    3 校验参数是否存在
    4 读取图片数据 avatar.read()
    5 调用骑牛运借口 上传用户头像
    6 保存用户头像信息 图片名称(骑牛运返回的结果)
    7 拼接图片完整路径: 骑牛外联域名 + 骑牛运上传图片返回的结果
    8 返回前端图片url
    '''
    # 获取用户id
    user_id = g.user_id
    # 获取用户上传的投降文件
    avatar = request.files.get('avatar')
    # 判断参数是否存在
    if not avatar :
        return jsonify(errno=RET.PARAMERR,errmsg='未上传文件')
    # 准备调用骑牛运借口
    avatar_data = avatar.read()
    # 调用接口
    try:
        image_name = storage(avatar_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR,errmsg='上传头像失败')
    # 保存头像数据到mysql数据库
    try:
        User.query.filter_by(id=user_id).update({'avatar_url':image_name})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR,errmsg='存储头像失败')
    # 拼接路径
    image_url = constants.QINIU_DOMIN_PREFIX + image_name
    return jsonify(errno=RET.OK,errmsg='ok',data={'avatar_url':image_url})

@api.route('/user/auth',methods=['POST'])
@login_required
def save_user_auth():
    '''
    保存用户实名信息
    1 获取用户id
    2 获取参数 get_json() 校验参数
    3 获取详细参数信息 校验参数完整性
    4 保存数据 需要确认 未实名验证过 real_name id_card
    5 返回结果
    '''
    # 获取用户id
    user_id = g.user_id
    # 获取post请求的参数
    user_data = request.get_json()
    # 校验参数
    if not user_data:
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')
    # 获取详细参数信息
    real_name = user_data.get('real_name')
    id_card = user_data.get('id_card')
    # 校验参数完整性
    if not all([real_name,id_card]):
        return jsonify(errno=RET.PARAMERR,errmsg='参数缺失')
    # 查询数据库 判断是否已经实名认证过
    try:
        User.query.filter_by(id=user_id,real_name=None,id_card=None).update({'real_name':real_name,'id_card':id_card})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR,errmsg='保存失败')
    return jsonify(errno=RET.OK,errmsg='OK')


@api.route('/user/auth',methods=['GET'])
@login_required
def get_user_auth():
    '''
    获取用户实名信息
        1 获取用户id
        2 根据用户id 查询数据库 保存查询结果
        3 校验查询结果  无效操作
        4 返回结果 user.auth_to_dict()
    '''
    #获取用户id
    user_id = g.user_id
    # 查询数据库
    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='数据库错误')
    # 校验查询结果
    if user is None:
        return jsonify(errno=RET.DATAERR,errmsg='无效操作')
    # 返回数据
    return jsonify(errno=RET.OK,errmsg='OK',data=user.auth_to_dict())








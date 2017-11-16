#coding:utf8
# 导入蓝图对象
from . import api
from ihome import redis_store,constants,db
from flask import current_app,jsonify,request,session
from ihome.models import Area,House,Facility,HouseImage,User,Order
from ihome.utils.response_code import RET
import json
from ihome.utils.commons import login_required
from ihome.utils.image_storage import storage
import datetime


@api.route('/areas',methods = ['GET'])
def get_area_info():
    '''
    获取区域信息
    1 先尝试从redis中 获取区域信息 校验查询结果
    2 如果没有获取 查询mysql
    3 校验查询结果
    4 把区域信息放入缓存中 先序列化area_json
    5 返回区域数据
    '''
    # 从redis中获取区域信息
    try:
        areas = redis_store.get('area_info')
    except Exception as e:
        current_app.logger.error(e)
        areas = None
    # 校验查询结果
    if areas:
        # 记录访问redis数据库的时间
        current_app.logger.info( 'hit area info redis' )
        return '{"errno":0,"errmsg":"OK","data":%s}' % areas

    # 查询mysql数据库 获取区域信息
    try:
        areas = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取区域信息异常")
    # 校验查询结果
    if not areas:
        return jsonify(errno=RET.DATAERR, errmsg="查询无数据")
    # 定义列表存储查询结果
    areas_list = []
    # 遍历查询结果
    for area in areas:
        areas_list.append(area.to_dict())
    # 序列化数据
    areas_json = json.dumps(areas_list)
    # 区域信息　传入缓存中
    try:
        redis_store.setx('area_info',constants.AREA_INFO_REDIS_EXPIRES,areas_json)
    except Exception as e:
        current_app.logger.error(e)
    #返回查询结果
    return '{"errno":0,"errmsg":"OK","data":%s}' % areas_json


@api.route('/houses',methods=['POST'])
@login_required
def save_house_info():
    '''
    保存房屋信息
    1 获取参数 user_id = g.user_id 房屋所属用户
    2 获取参数 post请求的房屋信息 get_json()
    3 校验参数存在
    4 获取详细的参数信息
    5 校验参数完整性
    6 对价格信息进行处理
    7 保存房屋基本信息 house = House() house,title = title
    8 尝试获取配套设施信息,如果存在 判断设施编号和数据源中存储的一致
    9 保存房屋设施数据
    10 提交数据到数据库
    11 返回结果 data:{'house_id':house.id}
    '''
    # 获取用户id
    user_id = g.user_id
    # 获取post请求的房屋基本信息
    house_data = request.get_json()
    # 校验参数
    if not house_data:
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')
    # 获取纤细参数
    title = house_data.get('title') # 房屋标题
    price = house_data.get('price') # 房屋价格
    area_id = house_data.get('area_id') # 房屋区域
    address = house_data.get('address') # 房屋地址
    room_count = house_data.get('room_count') # 房屋数目
    acreage = house_data.get('acreage') # 房屋面积
    unit = house_data.get('unit') # 房屋户型
    capacity = house_data.get('capacity') # 适住人数
    beds = house_data.get('beds') # 床位设施
    deposit = house_data.get('deposit') # 房屋押金
    min_days = house_data.get('min_days') # 最少入住天数
    max_days = house_data.get('max_days') # 最多入住天数
    # 校验参数完整性
    if not all([title,price,area_id,address,room_count,acreage,unit,capacity,beds,deposit,min_days,max_days]):
        return jsonify(errno=RET.PARAMERR,errmsg='参数缺失')
    # 对价格信息进行转换
    try:
        price = int( float(price)*100 )
        deposit = int( float(deposit)*100 )
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="房屋价格信息异常")
    # 构造模型对象 存储数据
    house = House()
    house.user_id = user_id
    house.area_id = area_id
    house.title = title
    house.price = price
    house.address = address
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days
    # 尝试获取房屋配套设施信息
    facility = house_data.get('facility')
    # 配套设施如果存在 需要过滤配套设施对应到数据库中真实存在
    if facility:
        try :
            # 过滤房屋设施编号 如果该房屋设施编号不存在 需要过滤操作
            facilities = Facility.query.filter(Facility.id.in_(facility).all())
            # 保存查询结果
            house.facilities = facilities
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="查询房屋配套设施异常")
    # 保存房屋数据,提交数据到数据库中
    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        # 存储房屋数据发生异常,需要进行回滚操作
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存房屋信息失败")
    # 返回结果
    return jsonify(errno=RET.OK, errmsg="OK", data={"house_id": house.id})


@api.route('/houses/<int:house_id>/images',methods=["POST"])
@login_required
def save_house_image(house_id):
    '''
    保存房屋图片
    1 获取图片文件内容 校验参数
    2 根据house_id 查询数据库 校验结果
    3 读取图片数据
    4 调用骑牛运借口 上传图片
    5 保存图片数据 到数据库当中 HouseImage() House() 把一条数据 存储到两张表里
    6 如果发生异常 进行回滚
    7 拼接路径 返回结果
    '''
    # 获取图片参数
    image = request.files.get('house_image')
    # 校验参数
    if not image:
        return jsonify(errno=RET.PARAMERR,errmsg='')
    # 校验房屋存在
    try:
        house = House.query.filter_by(id = house_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno = RET.DBERR,errmsg='查询房屋信息异常')
    # 校验查询结果
    if not house:
        return jsonify(errno=RET.NODATA,errmsg='查询无数据')
    # 读取图片数据
    image_data = image.read()
    # 调用骑牛运接口
    try:
        image_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR,errmsg='骑牛运上传文件失败')
    # 保存图片数据到数据库中
    house_image = HouseImage()
    house_image.house_id=house_id
    house_image.url = image_name
    # 提交模型类对象 到数据库
    db.session.add(house_image)
    # 房屋主图片如果没有设置 默认添加房屋第一章图片为主图片
    if not house.index_image_url:
        house.index_image_url = image_name
        db.sesiion.add(house)

    # 提交到数据库中
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR,errmsg='保存房屋图片失败')

    # 拼接外链域名
    image_url = constants.QINIU_DOMIN_PREFIX + image_name
    return jsonify(errno=RET.OK,errmsg='OK',data=image_url)


@api.route('/user/houses',methods=['GET'])
@login_required
def get_user_houses():
    '''
    获取用户房屋信息
    1 查询用户 id  user_id = g.user_id
    2 根据user_id查询数据库
    3 使用反向引用 查询用户的所有房屋信息
    4 定义列表 存储查询结果
    5 如果有房屋信息 存储到列表中
    6 返回结果
    '''
    user_id = g.user_id
    try:
        user = User.query.get(user_id)
        # 使用反向引用获取用户发布的房屋信息
        houses = user.houses
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='查询用户房屋信息异常')
    # 定义列表存储查询结果
    house_list = []
    if houses:
        for house in houses:
            house_list.append(house.to_basic_dict())
    # 返回查询结果
    return jsonify(errno=RET.OK,errmsg='OK',data={'houses':house_list})


@api.route('/session',methods=['GET'])
def check_login():
    '''
    登陆查询状态
    1 从缓存中获取用户的登陆信息
    2 判断获取结果 如果有数据 返回name
    3 返回结果
    '''
    name = session.get('name')
    # 判断获取结果
    if name is not None:
        return jsonify(errno=RET.OK, errmsg="true", data={"name": name})
    else:
        return jsonify(errno=RET.SESSIONERR, errmsg="false")


@api.route('/houses/index',methods=['GET'])
def get_house_index():
    '''
    获取项目首页幻灯片信息
    1 尝试从redis 中获取缓存的首页信息
    2 判断结果 如果有数据返回结果
    3 查询mysql
    4 默认按照房屋的成交量最高的五套房屋
    5 校验查询结果
    6 存储查询结果
    7 序列化数据
    8 存储到缓存中
    9 返回响应数据
    '''
    try:
        ret = redis_store.get('house_page_data')
    except Exception as e:
        current_app.logger.error(e)
        ret = None
    # 判断查询结果
    if ret:
        # 记录访问redis缓存数据的时间
        current_app.logger.info("hit houses index info redis")
        return '{"errno":0,"errmsg":"OK","data":%s}' % ret
    # 如果未获得 去mysql中查询
    try:
        houses = House.query.order_by(House.order_count.desc()).limit(constants.HOME_PAGE_MAX_HOUSES)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询房屋信息异常")
    # 判断查询结果
    if not houses:
        return jsonify(errno=RET.NODATA, errmsg="无房屋数据")
        # 存储查询结果
        houses_list = []
        # 遍历查询结果,判断房屋是否设置主图片,如未设置,不添加数据
        for house in houses:
            if not house.index_image_url:
                continue
            houses_list.append(house.to_basic_dict())
        # 序列化数据,准备存入缓存中
        houses_json = json.dumps(houses_list)
        # 存储数据到缓存中
        try:
            redis_store.setex("home_page_data", constants.HOME_PAGE_DATA_REDIS_EXPIRES, houses_json)
        except Exception as e:
            current_app.logger.error(e)
        # 构造响应数据
        resp = '{"errno":0,"errmsg":"OK","data":%s}' % houses_json
        return resp



@api.route('/houses/<int:house_id>',methods=['GET'])
def get_hosue_detail(house_id):
    """
    获取房屋详情信息
    1/获取参数,user_id,用来判断用户身份是否为房东,user_id = session.get("user_id',-1)
    2/判断house_id参数存在
    3/尝试从缓存中获取房屋详情信息
    4/校验查询结果
    5/查询mysql数据库
    6/校验查询结果
    7/调用模型类的to_full_dict()方法,需要进行异常处理
    8/序列化数据,存入缓存中
    9/构造响应数据,返回结果
    :return:
    """
    # 获取user_id,用来判断用户身份是否为房东,默认给-1
    user_id = session.get("user_id","-1")
    # 校验house_id参数
    if not house_id:
        return jsonify(errno=RET.PARAMERR,errmsg="参数缺失")
    # 尝试从redis中获取房屋缓存信息
    try:
        ret = redis_store.get("house_info_%s" % house_id)
    except Exception as e:
        current_app.logger.error(e)
        ret = None
    # 判断查询结果
    if ret:
        current_app.logger.info("hit house detail info redis")
        return '{"errno":0,"errmsg":"OK","data":{"user_id":%s,"house":%s}}' % (user_id,ret)
    # 查询mysql数据库
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="查询房屋详情信息失败")
    # 校验查询结果
    if not house:
        return jsonify(errno=RET.NODATA,errmsg="无房屋数据")
    # 调用模型类中的to_full_dict()
    try:
        house_data = house.to_full_dict()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR,errmsg="房屋数据格式错误")
    # 序列化数据
    house_json = json.dumps(house_data)
    # 把房屋数据存入缓存中
    try:
        redis_store.setex("house_info_%s" % house_id,constants.HOUSE_DETAIL_REDIS_EXPIRE_SECOND,house_json)
    except Exception as e:
        current_app.logger.error(e)
    # 构造响应报文
    resp = '{"errno":0,"errmsg":"OK","data":{"user_id":%s,"house":%s}}' % (user_id,house_json)
    return resp


@api.route('/houses',methods=['GET'])
def get_house_list():
    '''
    获取房屋列表
    1 获取参数 area_id start_date_str end_date_str sort_key,page 可选参数
    2 可选参数sort_key 需要有默认值 默认按照房屋发布时间进行排序 page 默认加载第一页
    3 校验参数 对日期进行格式化处理 datetime.striptime(start_data_str,'%Y-%m-%d')
    4 需要判断日期的天数 至少为1天
    5 对页数进行格式化 page = int( page )
    6 尝试从redis中获取缓存房屋列表信息 redis_key = ''
    7 校验查询结果
    8 如果未获取数据 查询mysql数据库
    9 用户选择的顾虑条件 区域信息 日期信息
    10 根据保存的过滤条件 查询数据库 booking price time 默认按照发布时间
    11 对查询结果进行分页处理 house,paginate(page,2,False)
    13 保存分页胡的房屋数据 和列表总页数
    14 存储分页后 构造返回结果
    15 存储hash类型的缓存

    '''
    # 尝试湖区参数 区域
    area_id = request.args.get('aid','')
    start_date_str = request.args.get('sd','')
    end_date_str = request.args.get('ed','')
    sort_key = request.args.get('sk','')
    page = request.args.get('p','1')
    try:
        #格式化日期
        start_date,end_date = None,None
        # 如果用户选择了了日期 对用户选择日期格式化
        if start_date_str:
            start_date = datetime.datetime.strptime(start_date_str,'%Y-%m-%d')
        if end_date_str:
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
        # 校验用户选择日期 至少是1天
        if start_date_str and end_date_str :
            # 断言如果实在try except 中 可以不用定义异常信息
            assert start_date <= end_date ,'false'
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR,errmsg='日期格式错误')
    # 对页数进行格式化
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR,errmsg='页数格式错误')
    # 禅师从redis中获取房屋列表信息
    try:
        redis_key = 'houses_%s_%s-%s-%s'%(area_id,start_date_str,end_date_str,sort_key)
        # 使用哈希数据类型获取数据
        ret = redis_store.hget(redis_key,page)
    except Exception as e:
        current_app.logger.error(e)
        ret = None
    # 查询结果
    if ret :
        # 记录访问缓存数据的时间
        current_app.logger.info('hit houses list info redis')
        return ret
    # 查询mysql 数据库
    try:
        # 定义列表 用来存储查询过滤的参数 区域信息 日期信息
        params_filter = []
        # 判断区域参数
        if area_id :
            params_filter.append(House.area_id == area_id)
        if start_date and end_date:
            # 对日期进行判断 来判断用户选择的日期和数据库中已经成交订单的日期是不冲突的
            conflict_orders = Order.query.filter(Order.begin_date<=end_date,Order.end_date>=start_date).all()
            # 根据冲突订单 获取冲突的房屋
            conflict_houses_id = [order.house_id for order in conflict_orders]
            # 判断冲突房屋数据
            if conflict_houses_id :
                # 对有冲突的房屋的id进行取反
                params_filter.append(House.id.notin_(conflict_houses_id))
        elif start_date :
            conflict_orders = Order.query.filter(Order.end_date>= start_date ).all()
            # 根据冲突订单 获取冲突的房屋
            conflict_houses_id = [order.house_id for order in conflict_orders]
            # 判断冲突房屋数据
            if conflict_houses_id:
            # 对有冲突的房屋的id进行取反
                params_filter.append(House.id.notin_(conflict_houses_id))
        elif end_date:
            conflict_orders = Order.query.filter(Order.start_date<=end_date).all()
            conflict_houses_id = [order.house_id for order in conflict_orders]
            if conflict_houses_id:
                # 对有冲突的房屋的id进行取反
                params_filter.append(House.id.notin_(conflict_houses_id))
        # 根据过滤条件以及用户选择的排序条件和排序条件进行查询
        if 'booking' == sort_key:   # 按照成交进行查询
            houses = House.query.filter(*params_filter).order_by(House.order_count.desc() )
        elif 'price-inc' == sort_key:
            houses = House.query.filter(*params_filter).order_by(House.price.asc())
        elif 'price-des' == sort_key:
            houses = House.query.filter(*params_filter).order_by(House.price.desc())
        else: # 按照房屋发布时间进行排序
            houses = House.query.filter(*params_filter).order_by(House.create_time.desc())
        # 对查询结果进行分页
        houses_page = houses.pagenate(page,constants.HOUSE_LIST_PAGE_CAPACITY,False)
        # 保存分页后的房屋数据
        houses_list = houses_page.items
        # 保存分页之后的总页数
        total_page = houses_page.page
        # 遍历分页后的数据
        houses_dict_list = []
        for house in houses_list:
            houses_dict_list.append(house.to_basic_dict)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='查询房屋列表信息异常')

    #　构造响应数据
    resp = {
        'errno':0,
        'errmsg':'OK',
        'data':{'houses':houses_dict_list,
                'total_page':total_page,
                'current_page':page
                }
    }
    # 序列化数据
    resp_json = json.dumps(resp)
    if page <= total_page:
        redis_key = 'houses_%s_%s_%s_%s'%(area_id,start_date_str,end_date_str,sort_key)
        # 一个jian 对应多个zhi
        pip = redis_store.pipline()
        try:
            # 开启事物
            pip.multi()
            # 存储缓存数据
            pip.hset(redis_key,page,resp_json)
            # 设置过期时间
            pip.expire(redis_key,constants.HOUSE_LIST_REDIS_EXPIRES)
            # 执行事务
            pip.execute()
        except Exception as e:
            current_app.logger.error(e)
    # 返回房屋列表页数据
    return resp_json
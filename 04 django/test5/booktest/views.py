from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *
# Create your views here.

# 分页
def page_test(request, pindex):
    # 查询所有地区的信息
    list1 = AreaInfo.objects.filter(aParent__isnull = True)
    # 将地区按一页10条进行分页
    p = Paginator(list1,10)
    # 获取第pindex条数据
    if pindex=="":
        pindex=1
    areas = p.page(pindex)

    #获取所有的页码
    plist = p.page_range

    #传到模板中
    return render(request,'booktest/page_test.html',{'areas':areas,"plist":plist})



# 级联菜单
def getAreas(request):
    return render(request,'booktest/getAreas.html')

#获得省份
def getProvince(request):
    provinces = AreaInfo.objects.filter(aParent__isnull = True)
    res = []
    for i in provinces:
        res.append( [i.id , i.atitle] )
    return JsonResponse({'provinces':res})

#获得城市
def getCity(request):
    city_id = request.GET.get('city_id')
    cities = AreaInfo.objects.filter(aParent_id=city_id)
    res = []
    for i in cities:
        res.append([i.id, i.atitle])
    return JsonResponse({'cities':res})

#获得区 县
def getDistrict(request):
    district_id = request.GET.get('district_id')
    cities = AreaInfo.objects.filter(aParent_id=district_id)
    res = []
    for i in cities:
        res.append([i.id, i.atitle])
    return JsonResponse({'district': res})



# 上传图片
from django.conf import settings
from .models import Pictures
# 返回上传图片的页面
def getUpload(request):
    return render(request,'booktest/upload.html')

#　发来表单　实现上传功能
def upload(request):
    # 从请求当中　获取文件对象
    f1 = request.FILES.get('picture')
    #　利用模型类　将图片要存放的路径存到数据库中
    Pictures.objects.upload( url = "booktest/" + f1.name)
    # p = Pictures()
    # p.pic = "booktest/" + f1.name
    # p.save()
    # 在之前配好的静态文件目录static/media/booktest 下 新建一个空文件
    # 然后我们循环把上传的图片写入到新建文件当中
    fname = settings.MEDIA_ROOT + "/booktest/" + f1.name
    with open(fname,'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("上传成功")

#　显示图片
def show_pic(request):
    pic = Pictures.objects.get(id=1)
    return render(request,'booktest/show_pic.html',{'pic':pic})



# 富文本编辑器
def editor(request):

    return render(request,'booktest/editor.html')
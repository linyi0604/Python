from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^page_test(\d*)/$',views.page_test),  #分页
    # 省市区下拉级联
    url(r'^getAreas/$',views.getAreas),
    url(r'^getProvince/$',views.getProvince),
    url(r'^getCity/$',views.getCity),
    url(r'^getDistrict',views.getDistrict),

    # form表单上传图片
    url(r'^getUpload/$',views.getUpload),
    url(r'^upload/$', views.upload),
    url(r'^show_pic$',views.show_pic),

    #富文本编辑器
    url(r'^editor/$',views.editor)

]

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pictures)


class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10 #每页多少条数据
    actions_on_top = False  #关掉上访的操作选项
    actions_on_bottom = True    #开启下方的操作选项
    list_display = ['id','atitle']
admin.site.register(AreaInfo,AreaInfoAdmin)


from django.db import models

# Create your models here.

# 建立城市自关联数据库表
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)
    aParent = models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return self.atitle

    class Meta:
        db_table = 'areas'  # 指定表名称



class PicturesAdmin(models.Manager):
    def upload(self,url):
        pic = self.model()
        pic.pic = url
        pic.save()
        return pic

#上传图片的模型类
class Pictures(models.Model):
    pic = models.ImageField(upload_to='booktest/')
    def __str__(self):
        return self.pic

    objects = PicturesAdmin()


#定义图书管理类
from django.db import models
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)   #书名
    bpub_date = models.DateField()  #发布日期
    bread = models.IntegerField(default=0)  #阅读数
    bcomment = models.IntegerField(default=0)   #评论数
    isDelete = models.BooleanField(default=False) #逻辑删除

#定义英雄模型类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄名
    hgender = models.BooleanField(default=True) #英雄性别
    isDelete = models.BooleanField(default=False)   #逻辑删除
    hcomment = models.CharField(max_length=200)#英雄描述
    hbook = models.ForeignKey('BookInfo') #外键约束 一对多关系









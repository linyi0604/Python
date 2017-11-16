from django.db import models

# Create your models here.

class AreasAdmin(models.Manager):
    def all(self):
        return super().all()
    def getProvince(self):
        area = self.model()
        provinces = super().filter( aParent__isnull=True )
        return provinces

class Areas(models.Model):
    atitle = models.CharField(max_length=30)
    aParent = models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return self.atitle

    class Meta:
        db_table = 'areas'

    objects = AreasAdmin()



class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField(auto_now_add=True)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo')



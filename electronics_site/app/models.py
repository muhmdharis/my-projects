from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    img = models.ImageField( upload_to='media', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    price = models.IntegerField(null=True)


class verify(models.Model):
    img = models.ImageField( upload_to='media', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productName = models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)


class exchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    exprectedPrice =  models.CharField(max_length  = 1000 , null=True)
    img = models.ImageField( upload_to='img', height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length  = 1000)
    model = models.CharField(max_length  = 1000)
    email = models.CharField(max_length  = 1000)
    discription = models.CharField(max_length  = 1000)
    isActive = models.CharField(max_length  = 1000,default='waiting')


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    premiumState = models.CharField( max_length=1000,null=True , default="False")
    startDate = models.CharField( max_length=1000,null=True)
    endDate =   models.CharField( max_length=1000,null=True)
    totalAmount =  models.IntegerField(null=True,default=0)
    

class HistoryExchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    Exchangeitem = models.ForeignKey(exchange, on_delete=models.CASCADE,null=True)
    exchangeDate = models.CharField( max_length=1000,null=True)
    exchangeRate = models.IntegerField(null=True)
    totalAmount =  models.IntegerField(null=True,default=0)


class chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_f = models.CharField( max_length=1000)
    t =   models.CharField( max_length=1000)


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totalAmount =  models.IntegerField(null=True,default=0)





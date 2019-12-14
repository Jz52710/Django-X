from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
#验证
def name_min(data):
    if len(data) <=2:
        raise ValidationError('长度不够两位以上',params={'value':data})

class Goods(models.Model):
    name = models.CharField(max_length=200,validators=[name_min])
    time = models.DateTimeField(auto_now=True,blank=True)

class User(models.Model):
    name = models.CharField(max_length=20,validators=[name_min],default='默认')
    password = models.CharField(max_length=20,default=123456)
    sex = models.IntegerField(choices=(
        (1,'男'),
        (2,'女')
    ),error_messages={'null':'no null','blank':'no blank'}
    )

class UserAdmins(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

#token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


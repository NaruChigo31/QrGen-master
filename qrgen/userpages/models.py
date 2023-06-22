from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Модели плана и модифицированного пользователя
class Plan(models.Model):
    price = models.FloatField()
    plantype = models.CharField(max_length=255)
    qrcode_amount = models.IntegerField()

class UserMod(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete = models.CASCADE) 
    last_payment = models.CharField(max_length=255)
    qr_scans = models.IntegerField()
    qr_amount = models.IntegerField()
    
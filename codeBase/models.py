from django.db import models

# Create your models here.

# JGold Services Api
class GiftCardModel(models.Model):
    card_name = models.CharField(max_length=100)
    buy_rate = models.CharField(max_length=20)
    sell_rate = models.CharField(max_length=20)
    buy_active = models.BooleanField(default=True)
    sell_active = models.BooleanField(default=True)
    logo = models.ImageField(blank=True, null=True)
    first_page = models.BooleanField(default=False)

class CryptoModel(models.Model):
    currency = models.CharField(max_length=100)
    buy_rate = models.CharField(max_length=20)
    sell_rate = models.CharField(max_length=20)
    buy_active = models.BooleanField(default=True)
    sell_active = models.BooleanField(default=True)
    logo = models.ImageField(blank=True, null=True)
    first_page = models.BooleanField(default=False)

class TestimonialModel(models.Model):
    name = models.CharField(max_length=100)
    approval_status = models.BooleanField(default=False)
    testimony = models.CharField(max_length=200)

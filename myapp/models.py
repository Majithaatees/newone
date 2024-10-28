from django.db import models

# Create your models here.
class customers(models.Model):
    cus_name=models.CharField(max_length=200)
    cus_email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    cus_age=models.IntegerField()
    cus_address=models.TextField()
    cus_image=models.ImageField(upload_to='static/customers/',default='null')
    def __str__(self):
        return self.cus_name
class users(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    age=models.IntegerField()
class Products(models.Model):
    p_name=models.CharField(max_length=200)
    p_desc=models.TextField()
    p_rate=models.IntegerField()
    p_image=models.ImageField(upload_to='static/products/')
class fav(models.Model):
    username=models.ForeignKey(users,on_delete=models.CASCADE)
    prd_name=models.ForeignKey(Products,on_delete=models.CASCADE)
    
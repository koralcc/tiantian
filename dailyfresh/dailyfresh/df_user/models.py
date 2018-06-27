from django.db import models

# Create your models here.

# 用户名、密码、邮箱

class User(models.Model):
    # 用户名
    name = models.CharField(max_length = 20)
    # 密码
    password = models.CharField(max_length = 100)
    # 邮箱
    email = models.CharField(max_length = 50)
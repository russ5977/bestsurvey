from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=128, verbose_name='用户名', unique=True, null=True)
    password = models.CharField(max_length=128, verbose_name='密码', unique=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

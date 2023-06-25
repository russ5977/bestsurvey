from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import SurveyMessage


class User(AbstractUser):
    username = models.CharField(max_length=128, verbose_name='用户名', unique=True, null=True)
    password = models.CharField(max_length=128, verbose_name='密码', unique=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class SurveyDetail(models.Model):
    STATUS_CHOICES = (
        ('1', '已成功'),
        ('2', '未通过'),
        ('3', '已退款'),)
    survey_message = models.ForeignKey(SurveyMessage, on_delete=models.CASCADE, verbose_name='关联题目')
    ip = models.CharField(max_length=128, verbose_name='ip', unique=True, null=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='开始时间')
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='结束时间')
    status = models.CharField(verbose_name='平台', max_length=1, choices=STATUS_CHOICES)
    time_consuming = models.CharField(max_length=128, verbose_name='耗时(分钟)', unique=True, null=True)
    notes = models.TextField(max_length=1500, verbose_name='备注')

    class Meta:
        db_table = 'survey_detail'

    def __str__(self):
        return self.ip

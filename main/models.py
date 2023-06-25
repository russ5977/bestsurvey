from django.db import models


class SurveyMessage(models.Model):
    PLATFORM_CHOICES = (
        ('1', 'AMD'),
        ('2', 'ACA'),
        ('3', 'AIN'),
        ('4', 'BCA'),
        ('5', 'ALP'),
        ('6', 'APN'))
    number = models.CharField(max_length=128, verbose_name='项目编号', unique=True, null=True)
    introduction = models.CharField(max_length=128, verbose_name='项目名称', unique=True, null=True)
    country = models.CharField(max_length=128, verbose_name='国家名称', unique=True, null=True)
    platform = models.CharField(verbose_name='平台', max_length=1, choices=PLATFORM_CHOICES)
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='价格')
    duration = models.IntegerField(verbose_name='时长')
    date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='更新时间')
    notes = models.TextField(max_length=1500)

    class Meta:
        db_table = 'survey_message'

    def __str__(self):
        return self.number

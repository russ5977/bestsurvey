from django.forms import model_to_dict

from .models import *
from rest_framework import serializers


class SurveyMessageSer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    platform = serializers.CharField(source='get_platform_display')

    class Meta:
        model = SurveyMessage
        fields = "__all__"

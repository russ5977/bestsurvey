from main.serializers import SurveyMessageSer
from .models import *
from rest_framework import serializers


class SurveyDetailSer(serializers.ModelSerializer):
    survey_message = serializers.SerializerMethodField()
    start_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    def get_survey_message(self, obj):
        answer = SurveyMessage.objects.filter(id=obj.id).order_by('id')
        data = {}
        for i in answer:
            data['id'] = i.id
            data['number'] = i.number
            data['introduction'] = i.introduction
            data['country'] = i.country
            data['duration'] = i.duration
            data['price'] = i.price
        return data

    class Meta:
        model = SurveyDetail
        fields = "__all__"

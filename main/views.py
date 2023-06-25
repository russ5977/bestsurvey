from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from bestsurvey.pagenation import MyPagination
from main.models import SurveyMessage
from main.serializers import SurveyMessageSer


class BrandViewSet(ModelViewSet):
    queryset = SurveyMessage.objects.all().order_by('-date')
    serializer_class = SurveyMessageSer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    # 分页
    pagination_class = MyPagination


class SearchSurvey(APIView):
    def post(self, request):
        q = request.data.get('keyword')
        # 能搜索
        if q:
            message = SurveyMessage.objects.filter(Q(number__contains=q)
                                                   | Q(platform__contains=q))
            result_message = SurveyMessageSer(message, many=True).data
            result = {'code': 200, 'data': result_message}
            return Response(result)

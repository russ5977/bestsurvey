import random
import string
from rest_framework.response import Response
from rest_framework.views import APIView


class GeneratePassword(APIView):
    def post(self, request):
        password = ''
        length = 10
        for i in range(length):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        return Response({'msg': '注册成功', 'code': 200})

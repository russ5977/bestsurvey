from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from django.contrib.auth import logout
import random
import string

from werkzeug.security import check_password_hash, generate_password_hash

from jiayin.pagenation import MyPagination
from user.models import User, SurveyDetail
from user.serializers import SurveyDetailSer


class RegisterView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not all([username, password]):
            return Response({'msg': '用户信息不全', 'code': 500})
        # 判断姓名
        user_name_num = User.objects.filter(username=username).count()
        if user_name_num != 0:
            return Response({'msg': '该用户用户名已经注册过', 'code': 500})
        # 加密存入 create_user
        password = generate_password_hash(password)
        User.objects.create(username=username, password=password)
        return Response({'msg': '注册成功', 'code': 200})


class LoginViews(APIView):
    """
    登录
    账号或密码
    """

    def post(self, request):
        username = request.data.get('username')
        pwd = request.data.get('password')
        print('pwd', pwd)
        if not all([username, pwd]):
            return Response({'msg': '账号或密码不全', 'code': 400})
        res = User.objects.filter(username=username).count()
        if res == 0:
            return Response({'msg': '账号不存在', 'code': 400})
        else:
            # 登录
            user = User.objects.get(username=username)
            # 密码效验check_password(输入，数据库的)
            rest = check_password_hash(user.password, pwd)
            if not rest:
                return Response({'msg': '账号或密码错误', 'code': 400})
                # 加密时生成第二部分的字符串
        # payload_dict = jwt_payload_handler(user)
        # 加密时生成第二部分的字符串
        payload_dict = jwt_payload_handler(user)
        # 生成token
        token = jwt_encode_handler(payload_dict)
        return Response({"msg": "登录成功", "code": "200", 'token': token, 'username': user.username})


class GeneratePassword(APIView):
    def post(self, request):
        password = ""
        length = 10
        for i in range(length):
            password += random.choice(string.ascii_letters + string.digits)
        return Response({'msg': '生成成功', 'code': 200, 'password': password})


class LogoutView(APIView):
    def get(self, request):
        logout(request=request)
        request.session.clear()
        return Response({"msg": "退出成功", "code": "200"})


class PutPass(APIView):
    def post(self, request):
        user_name = request.data.get('username')
        pwd = request.data.get('password')
        password = generate_password_hash(pwd)
        user = User.objects.filter(username=user_name)
        users = User.objects.get(username=user_name)
        user.update(password=password)
        payload_dict = jwt_payload_handler(users)
        # 生成token
        token = jwt_encode_handler(payload_dict)
        return Response({"msg": "修改密码成功", "code": "200", 'token': token, 'username': users.username})


class SurveyDetailViewSet(ModelViewSet):
    queryset = SurveyDetail.objects.all().order_by('id')
    serializer_class = SurveyDetailSer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    # 分页
    pagination_class = MyPagination
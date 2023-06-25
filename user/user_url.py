from django.urls import path
from user import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # 注册 账号 密码 手机号 验证码
    path('register/', views.RegisterView.as_view()),
    # 普通登录 账号 密码
    path('login/', views.LoginViews.as_view()),
    path('generate_password/', views.GeneratePassword.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('put_pass/', views.PutPass.as_view()),
]
router = DefaultRouter()
router.register('show_detail', views.SurveyDetailViewSet)
urlpatterns += router.urls

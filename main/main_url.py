from django.urls import path
from main import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('search/', views.SearchSurvey.as_view()),
]
router = DefaultRouter()
router.register('show', views.BrandViewSet)
urlpatterns += router.urls

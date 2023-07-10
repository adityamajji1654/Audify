from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload_video/', views.upload_video, name="upload_video"),
    path('home/',views.home,name="home"),
    path('register/', views.register_page, name="register_page"),
    path('login/', views.login_page, name="login_page")
]
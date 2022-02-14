"""
first_app의 길 이라고 생각하면 됨. 다른 어플리케이션을 연결시켜줌. (라우팅)
"""
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
]

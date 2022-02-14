"""
ex_myproject의 길 이라고 생각하면 됨. 다른 어플리케이션을 연결시켜줌. (라우팅)
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls'))
]

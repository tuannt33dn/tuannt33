from django.contrib import admin
from django.urls import path
from dangky import views
urlpatterns = [
    path('', views.dangky),
    path('xuly_dangky/', views.xuly_dangky, name="xuly_dangky"),
]
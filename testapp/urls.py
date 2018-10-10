from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.alldata, name='data-table'),
    path('webdata/', views.allwebdata, name='web-table'),
    path('myform/', views.myformview, name='myform'),
]

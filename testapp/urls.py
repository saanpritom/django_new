from django.urls import path
from testapp import views

testapp = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.alldata, name='datatable'),
    path('webdata/', views.allwebdata, name='web-table'),
    path('myform/', views.myformview, name='myform'),
    path('createtopics/', views.mytopicmodelform, name='topicmodelform'),
    path('createwebpage/', views.mywebpagemodelform, name='webpagemodelform'),
]

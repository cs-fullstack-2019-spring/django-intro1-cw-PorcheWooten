
from django.urls import path

from . import views
#set url path to let user know where to go !
urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='index'),
    path('music/future/', views.future, name='index'),
    path('music/cardi/', views.cardi, name='index'),
    path('music/keke/', views.keke, name='index'),
]
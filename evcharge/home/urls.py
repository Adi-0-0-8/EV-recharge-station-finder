from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    
    path('addpoint', views.addpoint, name="addpoint"),   
    path('details', views.details, name="details"),
    path('map', views.map, name="map"),
 
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logsout"),
    path('add', views.add, name="add"),
    path('details/<str:name>', views.details, name="details"),
    path('details/addreviews/<str:stationname>', views.addreviews, name="addreviews")
]

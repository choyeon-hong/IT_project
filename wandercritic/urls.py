from django.urls import path
from wandercritic import views

app_name = 'wandercritic' 

urlpatterns = [

    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
]
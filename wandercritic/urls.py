from django.urls import path
from wandercritic import views

app_name = 'wandercritic' 

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('explore/', views.explore, name='explore'),
]
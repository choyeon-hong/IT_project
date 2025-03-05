from django.urls import path
from wandercritic import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'wandercritic' 

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('become-agent/', views.become_agent, name='become_agent'),
    path('report/', views.report, name='report'),
    path('policies/<str:policy_type>/', views.policy, name='policy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
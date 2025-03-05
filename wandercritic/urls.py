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
    
    # Place URLs
    path('places/', views.place_list, name='place_list'),
    path('places/create/', views.place_create, name='place_create'),
    path('places/<slug:slug>/', views.place_detail, name='place_detail'),
    path('places/<slug:slug>/edit/', views.place_edit, name='place_edit'),
    
    # Admin URLs
    path('admin/applications/', views.admin_applications, name='admin_applications'),
    path('admin/applications/<int:application_id>/<str:action>/', 
         views.admin_application_action, name='admin_application_action'),
    path('admin/reports/', views.admin_reports, name='admin_reports'),
    path('admin/reports/<int:report_id>/<str:action>/', 
         views.admin_report_action, name='admin_report_action'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
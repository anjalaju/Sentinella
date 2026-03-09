from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('incidents/', views.incidents, name='incidents'),
    path('live-monitor/', views.live_monitor, name='live_monitor'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('accounts/', views.accounts, name='accounts'),
    path('settings/', views.settings, name='settings'),
    path('camera/', views.camera, name='camera'),
    path('reports/', views.reports, name='reports'),
    path('heatmap/', views.heatmap, name='heatmap'),
    path('notification/', views.notification, name='notification'), 
    path('floor-map/', views.floor_map, name='floor_map'),
    path('privacy-logs/', views.privacy_logs, name='privacy_logs'),
    path('system-config/', views.system_config, name='system_config'),
    path('staff-portal/', views.staff_portal, name='staff_portal'),
    path('history/', views.history, name='history'),
]
from django.urls import path
from. import views


urlpatterns = [
    path('', views.home, name ='vaccidocapp-home'),
    path('about/', views.about, name ='vaccidocapp-about'),


]
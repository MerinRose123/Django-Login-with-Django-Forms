from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
   path('formnew/', views.contact),
   path('register/', views.register),
   path('login/', views.login),
   path('loginview/', views.loginview),
   path('editpage/', views.editrender),
   path('edit/', views.edit),
]
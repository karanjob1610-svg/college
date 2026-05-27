from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admission/', views.admission, name='admission'),
    path('fees/', views.fees, name='fees'),
    path('placement/', views.placement, name='placement'),
    path('contact/', views.contact, name='contact'),
]
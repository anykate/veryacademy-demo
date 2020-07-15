from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # path('home/', views.home, name='home_fbv'),
    path('', views.HomeView.as_view(), name='home_cbv'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

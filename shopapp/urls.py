from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name = 'indexpage'),
    path('accounts/profile/',views.profile,name = 'profile'),
]
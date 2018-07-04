from django.urls import path, include
from django.contrib.auth.views import login
from . import views
app_name = "shop"

urlpatterns = [
    path('', views.index, name='index'),
]

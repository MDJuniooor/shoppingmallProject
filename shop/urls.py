from django.urls import path, include
from . import views
app_name = "shop"

urlpatterns = [
    path('', views.index, name='index'),
    path('<item_id>/order/new/',views.order_new,name='order_new')
]

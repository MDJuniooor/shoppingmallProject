from django.urls import path, include
from django.contrib.auth.views import login

app_name = "accounts"

urlpatterns = [
    path("login/",login,name='login',kwargs={
        'template_name':'accounts/login.html',
    }),
]

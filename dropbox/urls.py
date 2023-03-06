from django.urls import path
from . import views 



urlpatterns = [
     path('', views.index, name='index'),
     path('login', views.user_login, name='login'),
     path('signup',views.signup, name='signup'),
     path('signout',views.signout, name='signout'),
]

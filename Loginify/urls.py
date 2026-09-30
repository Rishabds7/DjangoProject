from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('api/all-users/', views.AllUsersData, name='all_users'),
    path('api/single-user/<str:username>/', views.SingleUserData, name='single_user'),
]


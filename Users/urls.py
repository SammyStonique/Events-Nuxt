from django.urls import path,include

from . import views

urlpatterns = [
    path('register/', views.UserRegistration.as_view()),
    path('user-list/', views.UserList.as_view()),
    path('current-user-details/', views.CurrentUser.as_view()),
    path('user-list/<str:pk>/', views.UserDetails.as_view()),
    path('login', views.login ,name='login'),

]
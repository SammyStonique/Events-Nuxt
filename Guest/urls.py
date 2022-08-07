from django.urls import path,include

from . import views

urlpatterns = [

    path('profile/', views.UserProfiles.as_view(),name= 'profile'),
    path('user-profile/<int:pk>/', views.EditProfile.as_view(),name= 'edit_profile'),
    path('current-user/', views.ProfileDetails.as_view()),
    path('register/',views.register,name = 'register'),
    path('contact/',views.contact,name = 'contact'),
    path('about/',views.about,name = 'about'),
    # path('create_guests_list/', views.create_guests_list,name= 'create_guests_list'),
    path('create_guests_list/', views.guest_registration,name= 'create_guests_list'),
    path('view_guests_list/', views.ViewGuests.as_view(),name= 'view_guests_list'),
    path('update_guests_list/<str:pk>/', views.update_guests_list, name="update_guests_list"),
    path('delete_guests_list/<str:pk>/', views.delete_guests_list, name="delete_guests_list"),
    path('guest_registration/<int:id>/', views.guest_registration,name= 'guest_registration'),
    path('invites_only_application/<int:id>/', views.invites_only_application,name= 'invites_only_application'),
]
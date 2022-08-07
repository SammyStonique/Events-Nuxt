from django.urls import path
from .import views

urlpatterns = [
    path('create_event/', views.createevent,name= 'create_event'),
    path('events_list/', views.EventsList.as_view()),
    path('view_event/<int:pk>/', views.ViewEvent.as_view(),name= 'view_event'),
    path('update_event/<str:pk>/', views.update_event, name="update_event"),
    path('delete_event/<str:pk>/', views.delete_event, name="delete_event"),
    path('print_events/', views.generate_pdf_events,name ='generate_pdf_events'),
    path('print_guests/', views.generate_pdf_guests,name ='generate_pdf_guests'),
    path('send_mail/<int:id>/', views.sendmail,name ='send_mail'),
    #path('guest_registration_email/', views.guest_registration_email,name ='guest_registration_email'),
    path('guest_view_events/', views.guest_view_events, name='guest_view_events'),
    path('view_applications/', views.view_applications,name= 'view_applications'),
    path('view_invites_only_applications/', views.view_invites_only_applications,name= 'view_invites_only_applications'),
    path('reject_application/<str:pk>/', views.reject_application, name="reject_application"),
    path('reject_invites_only_application/<int:id>/', views.reject_invites_only_application, name="reject_invites_only_application"),
    path('print_applications/', views.generate_pdf_applicants,name ='generate_pdf_applicants'),
    path('print_invites_only_applications/', views.generate_pdf_invites_only_applicants,name ='generate_pdf_invites_only_applicants'),
    path('succesful_application/<int:id>/', views.succesful_application,name ='succesful_application'),
    path('ussd_callback/', views.ussd_callback,name = 'ussd_callback'),
    path('events_report/', views.events_report, name = 'events_report'),
]
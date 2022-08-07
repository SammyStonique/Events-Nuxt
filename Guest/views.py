from django.shortcuts import render,redirect,get_object_or_404
from. forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import render_to_pdf
from django.template.loader import get_template
from django.http import HttpResponse,FileResponse
import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt #for the ussd function
#from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException#for sms
import africastalking
from .filters import *
from django.core.paginator import Paginator
from .permissions import *

import io
import reportlab
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4
#from reportlab.lib.units import inch
#from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

username = 'your africastalking username'
api_key = 'your africastalking api_key'
africastalking.initialize(username, api_key)  
sms = africastalking.SMS 


# Create your views here.
def contact(request):
    return render(request,'Users/contact.html')

def about(request):
    return render(request,'Users/about.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, Your account has succesfully been created')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'Users/register.html', {'form': form})

                        #USER PROFILE


class ProfileDetails(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.filter(user=request.user)
        serializer = ProfileSerializer(profile)
        permission_classes = [IsProfileOwner]
        return Response(serializer.data)

class UserProfiles(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer 

class EditProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



                        #CREATING A GUESTS LIST views

#Create a guests list
def guest_registration(request):
    serializer = GuestRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(event_organizer=request.user)
        return Response(serializer.data)

# class GuestRegistration(generics.ListCreateAPIView):
#     queryset = InvitesOnlyRegistration.objects.all()
#     serializer_class = GuestRegistrationSerializer

#View guests list

class ViewGuests(generics.ListAPIView):
    queryset = GuestRegistration.objects.all()
    serializer_class = GuestRegistrationSerializer

#Update guests list
@login_required
def update_guests_list(request, pk):

	guestlist = InvitedGuests.objects.get(id=pk)
	form3 = InvitedGuestsForm(instance=guestlist)

	if request.method == 'POST':
		form3 = InvitedGuestsForm(request.POST, instance=guestlist)
		if form3.is_valid():
			form3.save()
			return redirect('view_guests_list')

	context = {'form3':form3}
	return render(request, 'Users/update_guests_list.html', context)

#Delete guest
@login_required
def delete_guests_list(request, pk):
	guestlist = InvitedGuests.objects.get(id=pk)
	if request.method == "POST":
		guestlist.delete()
		return redirect('view_guests_list')

	context = {'item':guestlist}
	return render(request, 'Users/delete_guests_list.html', context)



                        #GUEST ACTIONS views


#Guest Registration For Public Events
def guest_registration(request,id):
    form4 = GuestRegistrationForm()
    viewevent = get_object_or_404(CreateEvent,id=id)
    if request.method == 'POST':
        form4 = GuestRegistrationForm(request.POST)
        
        if form4.is_valid:
            new_form4 = form4.save(commit=False)
            new_form4.event_organizer = viewevent.created_by
            new_form4.event_applied_for = viewevent.eventname
            new_form4.save()
            name = form4.cleaned_data.get('firstname')
            email =  form4.cleaned_data.get('email')
            phone_number = form4.cleaned_data.get('phonenumber')
            recipient = [email]
            subject = f'Registration for the {viewevent.eventname} event'
            content = f'Dear {name},\n\nYou have succesfully enrolled for the {viewevent.eventname} event that is to be held on {viewevent.date} in {viewevent.venue}.\n\nDescription: {viewevent.description}.\n\nFor more enquiries, email us at ezenfinancialsevents@gmail.com\n\nSee you there.'
            send_mail(subject, content, settings.EMAIL_HOST_USER,recipient, fail_silently=False)
            messages.success(request,'Success, you will receive a confirmation email')
            #sms.send(f'Dear {name},You have succesfully enrolled for the {viewevent.eventname} event that is to be held on {viewevent.date} in {viewevent.venue}. Check your mail for more details',[f'{phone_number}'], callback = guest_registration)
            return redirect('guest_view_events')
           
    return render(request,'Users/Guests/guest_register.html', {'form4':form4})

#Invites Only Event Application
def invites_only_application(request,id):
    form5 = InvitesOnlyRegistrationForm()
    viewevent = get_object_or_404(CreateEvent,id=id)
    
    if request.method == 'POST':
        form5 = InvitesOnlyRegistrationForm(request.POST)
        
        if form5.is_valid:
            new_form5 = form5.save(commit=False)
            new_form5.event_organizer = viewevent.created_by
            new_form5.event_applied_for = viewevent.eventname
            new_form5.save()
            name = form5.cleaned_data.get('firstname')
            email =  form5.cleaned_data.get('email')
            phone_number = form5.cleaned_data.get('phonenumber')
            recipient = [email]
            subject = f'Registration for the {viewevent.eventname} event'
            content = f'Dear {name},\n\nYour application for the {viewevent.eventname} event has been succesfully received. You will receive a confirmation email.\n\nThank you.'
            send_mail(subject, content, settings.EMAIL_HOST_USER,recipient, fail_silently=False)
            messages.success(request,'Your application has been received. You will be notified if it\'s succesful')
            #sms.send(f'Dear {name}, Your application for the {viewevent.eventname} event has been succesfully received. You will receive a confirmation email.\nThank you.',[f'{phone_number}'], callback = invites_only_application)
            return redirect('guest_view_events')
            
    return render(request,'Users/Guests/invites_only_registration.html', {'form5':form5})



from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta :
        model = Profile
        fields = ['id','user','firstname','lastname','image','bio','birthdate','gender','email','contact','city','county']

class GuestRegistrationSerializer(serializers.ModelSerializer):
    event_organizer = serializers.ReadOnlyField(source = 'event_organizer.email')
    event_applied_for = serializers.ReadOnlyField(source='event_applied_for.eventname')
    class Meta :
        model = GuestRegistration
        fields = ['id','title','firstname','lastname','email','identificationnumber','phonenumber','gender','county','event_organizer','event_applied_for','reservation','guestrole']
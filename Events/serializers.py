from rest_framework import serializers
from .models import *
from Users.models import *
from Guest.models import *

class CreateEventSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = 'created_by.email')
    class Meta :
        model = CreateEvent
        fields = ['id','eventtype','eventname','venue','description','date','guests','created_by','images']


class InvitedGuestsSerializer(serializers.ModelSerializer):
    class Meta :
        model = InvitedGuests
        fields = ['id','guesttitle','guestname','email','identificationnumber','guestrole','created_by','contribution']


class InvitesOnlyRegistrationSerializer(serializers.ModelSerializer):
    class Meta :
        model = InvitesOnlyRegistration
        fields = ['id','firstname','lastname','email','identificationnumber','phonenumber','gender','county','event_organizer','event_applied_for','reservation']
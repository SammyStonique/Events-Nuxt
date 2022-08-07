from django.db import models
from django.contrib.auth import get_user_model
from Users.models import User
import datetime


UserModel = get_user_model()
# Create your models here.
class CreateEvent(models.Model):

    EVENTTYPE_CHOICES = (('','Select Event Type'),('Public Event', 'Public Event'),('Invites Only','Invites Only'))
    GUEST_LIST = (('','Select Gender'),('Dr.', 'Dr.'),('Sir','Sir'),('Madam','Madam'),('Mr.','Mr.'),('Mrs.','Mrs.'))
    
    id = models.AutoField(primary_key=True)
    eventtype = models.CharField(max_length=100,choices=EVENTTYPE_CHOICES,default='')
    eventname = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='uploads/')
    date = models.DateField(default=datetime.date.today)
    guests = models.CharField(max_length=100)
    created_by = models.ForeignKey('Users.User', on_delete=models.CASCADE,related_name='create_events')

    def __str__(self):
        return f'{self.eventname}'
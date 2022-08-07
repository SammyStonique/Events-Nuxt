from django.db import models
from PIL import Image
from multiselectfield import MultiSelectField
from django.contrib.auth import get_user_model
from Users.models import User
from Events.models import CreateEvent

# Create your models here.
UserModel = get_user_model()

class Profile(models.Model):

    CITY = (('','Select your city'),('Nairobi','Nairobi'),('Mombasa','Mombasa'),('Kisumu','Kisumu'))
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other')) 
    COUNTY = (('','Select County'),('Kisumu','Kisumu'),('Nairobi','Nairobi'),('Mombasa','Mombasa'),('Siaya','Siaya'))

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField('Users.User', on_delete=models.CASCADE,null=True,blank=True)
    firstname = models.CharField(max_length=250,null=True,blank=True)
    lastname = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=250,null=True,blank=True)
    birthdate = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=250,choices=GENDER,default='')
    email = models.CharField(max_length=250,null=True,blank=True)
    contact = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,choices=CITY,default='')
    county = models.CharField(max_length=250,choices=COUNTY,default='')


    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save()

        img = Image.open(self.image.path)

        if img.height > 20 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class InvitedGuests(models.Model):
    GUEST_TITLE = (('','Select Title'),('Dr.', 'Dr.'),('Sir','Sir'),('Madam','Madam'),('Mr.','Mr.'),('Mrs.','Mrs.'))
    GUEST_ROLE = (('','Select Role'),('Guest of Honour','Guest of Honour'),('Main Speaker','Main Speaker'),('Attendee','Attendee'))
    
    id = models.AutoField(primary_key=True)
    guesttitle = models.CharField(max_length=100,choices=GUEST_TITLE,default='')
    guestname= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    identificationnumber = models.CharField(max_length=100)
    guestrole = models.CharField(max_length=100,choices=GUEST_ROLE,default='')
    created_by = models.ForeignKey('Users.User', on_delete=models.CASCADE,null=True,blank=True)
    contribution = models.CharField(max_length=100)

    def __str__(self):
        return self.guestname

class GuestRegistration(models.Model):
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other'))
    COUNTY = (('','Select County'),('Kisumu','Kisumu'),('Nairobi','Nairobi'),('Mombasa','Mombasa'),('Siaya','Siaya'))
    TITLE = (('','Select Title'),('Dr.', 'Dr.'),('Sir','Sir'),('Madam','Madam'),('Mr.','Mr.'),('Mrs.','Mrs.'))
    RESERVATION = (('','Select Reservation'),('VVIP','VVIP'),('VIP','VIP'),('First Class','First Class'),('Economy','Economy'))
    ROLE = (('','Select Role'),('Guest of Honour','Guest of Honour'),('Master of Ceremony','Master of Ceremony'),('Main Speaker','Main Speaker'),('Attendee','Attendee'))

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,choices=TITLE,default='')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    identificationnumber = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=GENDER,default='')
    county = models.CharField(max_length=100,choices=COUNTY,default='')
    reservation = models.CharField(max_length=100, choices=RESERVATION,default='')
    guestrole = models.CharField(max_length=100, choices=ROLE,default='')
    event_organizer = models.ForeignKey('Users.User',on_delete=models.CASCADE,null=True,blank=True)
    event_applied_for = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.firstname

class InvitesOnlyRegistration(models.Model):
    TITLE = (('','Select Title'),('Dr.', 'Dr.'),('Sir','Sir'),('Madam','Madam'),('Mr.','Mr.'),('Mrs.','Mrs.'))
    GENDER = (('','Select Gender'),('Male','Male'),('Female','Female'),('Other','Other'))
    COUNTY = (('','Select County'),('Kisumu','Kisumu'),('Nairobi','Nairobi'),('Mombasa','Mombasa'),('Siaya','Siaya'))
    RESERVATION = (('','Select Reservation'),('VVIP','VVIP'),('VIP','VIP'),('Normal','Normal'))

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,choices=TITLE,default='')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    identificationnumber = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=GENDER,default='')
    county = models.CharField(max_length=100,choices=COUNTY,default='')
    reservation = models.CharField(max_length=100, choices=RESERVATION,default='')
    event_organizer = models.ForeignKey('Users.User',on_delete=models.CASCADE,null=True,blank=True)
    event_applied_for = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.firstname
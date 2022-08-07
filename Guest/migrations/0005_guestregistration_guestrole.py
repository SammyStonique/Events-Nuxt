# Generated by Django 4.0.6 on 2022-07-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_guestregistration_reservation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestregistration',
            name='guestrole',
            field=models.CharField(choices=[('', 'Select Role'), ('Guest of Honour', 'Guest of Honour'), ('Master of Ceremony', 'Master of Ceremony'), ('Main Speaker', 'Main Speaker'), ('Attendee', 'Attendee')], default='', max_length=100),
        ),
    ]

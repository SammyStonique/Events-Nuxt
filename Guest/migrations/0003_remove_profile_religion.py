# Generated by Django 4.0.6 on 2022-07-20 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='religion',
        ),
    ]

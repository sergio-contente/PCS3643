# Generated by Django 4.1 on 2022-11-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlightApp', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('1', 'admin'), ('2', 'operator'), ('3', 'employee'), ('4', 'unauthorized')], default=('4', 'unauthorized'), max_length=20),
        ),
    ]

# Generated by Django 4.1 on 2022-12-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlightApp', '0008_voo_erro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_voo',
            field=models.CharField(default='EMBARCANDO', max_length=20),
        ),
    ]

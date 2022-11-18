# Generated by Django 4.1 on 2022-11-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlightApp', '0002_alter_horarioprevisto_id_previsao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('isLocked', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=3)),
            ],
        ),
    ]
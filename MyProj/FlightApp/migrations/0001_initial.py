# Generated by Django 4.1 on 2022-10-10 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioPrevisto',
            fields=[
                ('id_previsao', models.IntegerField(primary_key=True, serialize=False)),
                ('partida_prevista', models.DateTimeField()),
                ('chegada_prevista', models.DateTimeField()),
            ],
            options={
                'db_table': 'horarios_previstos',
            },
        ),
        migrations.CreateModel(
            name='HorarioReal',
            fields=[
                ('id_real', models.IntegerField(primary_key=True, serialize=False)),
                ('partida_real', models.DateTimeField()),
                ('chegada_real', models.DateTimeField()),
            ],
            options={
                'db_table': 'horarios_reais',
            },
        ),
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id_rota', models.IntegerField(primary_key=True, serialize=False)),
                ('aeroporto_destino', models.CharField(max_length=3)),
                ('aeroporto_saida', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'rotas',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.IntegerField(primary_key=True, serialize=False)),
                ('status_voo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('codigo_voo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('companhia_aerea', models.CharField(max_length=10)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightApp.status')),
                ('previsao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightApp.horarioprevisto')),
                ('real', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightApp.horarioreal')),
                ('rota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightApp.rota')),
            ],
            options={
                'db_table': 'voos',
            },
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id_relatorio', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
                ('tempo_real_atraso', models.DateTimeField()),
                ('data_geracao', models.DateTimeField()),
                ('codigo_voo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightApp.voo')),
            ],
            options={
                'db_table': 'relatorios',
            },
        ),
    ]

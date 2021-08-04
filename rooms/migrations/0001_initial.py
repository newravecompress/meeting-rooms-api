# Generated by Django 3.2.4 on 2021-06-17 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('num_chairs', models.PositiveSmallIntegerField()),
                ('has_desk', models.BooleanField(blank=True, default=False)),
                ('has_projector', models.BooleanField(blank=True, default=False)),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('status', models.CharField(blank=True, choices=[('N', 'New'), ('R', 'Reserved'), ('C', 'Cancelled')], default='N', max_length=1)),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='rooms.room')),
            ],
            options={
                'ordering': ('-date', '-time_start'),
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-30 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0002_doctore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('booked', models.DateField()),
                ('time', models.TimeField()),
                ('decs', models.TextField(max_length=500)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emergency.doctore')),
            ],
        ),
    ]

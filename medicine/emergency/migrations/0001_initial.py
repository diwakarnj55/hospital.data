# Generated by Django 5.0.6 on 2024-05-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.TextField(max_length=20)),
                ('dep_desc', models.TextField(max_length=100)),
            ],
        ),
    ]

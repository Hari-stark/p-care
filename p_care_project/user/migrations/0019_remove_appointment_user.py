# Generated by Django 5.0.4 on 2024-07-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-30 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_address_customer_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='city',
            new_name='address',
        ),
    ]

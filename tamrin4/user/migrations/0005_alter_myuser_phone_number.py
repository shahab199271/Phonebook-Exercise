# Generated by Django 3.2.3 on 2021-06-03 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_myuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='phone number invalid', regex='^09[0-9]{9}$')]),
        ),
    ]
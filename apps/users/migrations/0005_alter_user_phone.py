# Generated by Django 5.0.3 on 2024-04-15 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_useradditionalinfo_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=19, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(19), django.core.validators.RegexValidator(message='Телефон должен быть в формате: +996999999900', regex='^\\+?1?\\d{11}$')], verbose_name='Телефон'),
        ),
    ]

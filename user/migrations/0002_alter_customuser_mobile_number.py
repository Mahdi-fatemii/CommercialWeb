# Generated by Django 5.0 on 2024-01-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]

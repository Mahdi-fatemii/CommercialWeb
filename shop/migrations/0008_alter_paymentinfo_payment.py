# Generated by Django 5.0 on 2024-01-12 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_paymentinfo_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.payment'),
        ),
    ]
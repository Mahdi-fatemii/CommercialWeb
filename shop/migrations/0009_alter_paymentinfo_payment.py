# Generated by Django 5.0 on 2024-01-14 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_paymentinfo_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.payment'),
        ),
    ]

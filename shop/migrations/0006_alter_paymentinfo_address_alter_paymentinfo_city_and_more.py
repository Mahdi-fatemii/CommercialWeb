# Generated by Django 5.0 on 2024-01-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_payment_card_pan_payment_date_created_payment_refid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='zipcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

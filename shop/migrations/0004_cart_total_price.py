# Generated by Django 5.0 on 2024-01-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_cartitems_cartitem_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

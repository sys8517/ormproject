# Generated by Django 4.0.2 on 2022-02-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_cust_item_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='regdate',
            field=models.DateField(auto_now=True),
        ),
    ]

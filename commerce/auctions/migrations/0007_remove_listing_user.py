# Generated by Django 3.1.4 on 2020-12-21 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bid_bid_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_user_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-16 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_directorderitem_direct_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]

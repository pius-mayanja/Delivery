# Generated by Django 5.0.3 on 2024-04-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0015_category_alter_type_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='business',
        ),
    ]

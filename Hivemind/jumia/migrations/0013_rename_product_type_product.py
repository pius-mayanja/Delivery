# Generated by Django 5.0.3 on 2024-04-03 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0012_remove_type_category_type_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='Product',
            new_name='product',
        ),
    ]

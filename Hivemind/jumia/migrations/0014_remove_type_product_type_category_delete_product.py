# Generated by Django 5.0.3 on 2024-04-16 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0013_rename_product_type_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='product',
        ),
        migrations.AddField(
            model_name='type',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='jumia.categories'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

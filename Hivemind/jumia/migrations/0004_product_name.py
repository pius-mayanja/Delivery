# Generated by Django 5.0.3 on 2024-03-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0003_rename_name_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

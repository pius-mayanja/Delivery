# Generated by Django 5.0.3 on 2024-03-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumia', '0007_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]

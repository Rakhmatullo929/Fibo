# Generated by Django 4.0.3 on 2022-06-09 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_type_alter_product_image_alter_product_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
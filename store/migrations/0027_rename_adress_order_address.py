# Generated by Django 4.0.4 on 2022-06-24 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_rename_name_order_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adress',
            new_name='address',
        ),
    ]
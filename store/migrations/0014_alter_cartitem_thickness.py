# Generated by Django 4.0.4 on 2022-06-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_cartitem_quantity_alter_cartitem_thickness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='thickness',
            field=models.PositiveIntegerField(choices=[('Традиционное', 'Традиционное'), ('Тонкое', 'Тонкое')], null=True),
        ),
    ]

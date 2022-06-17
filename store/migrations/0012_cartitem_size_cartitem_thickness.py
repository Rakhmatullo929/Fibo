# Generated by Django 4.0.4 on 2022-06-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_order_city_remove_order_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(choices=[('Маленькая', 'Маленькая'), ('Средняя', 'Средняя'), ('Большая', 'Большая')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='thickness',
            field=models.CharField(choices=[('Традиционное', 'Традиционное'), ('Тонкое', 'Тонкое')], max_length=30, null=True),
        ),
    ]
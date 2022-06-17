# Generated by Django 4.0.4 on 2022-06-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_cartitem_size_cartitem_thickness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='thickness',
            field=models.PositiveIntegerField(choices=[('Традиционное', 'Традиционное'), ('Тонкое', 'Тонкое')], max_length=30, null=True),
        ),
    ]
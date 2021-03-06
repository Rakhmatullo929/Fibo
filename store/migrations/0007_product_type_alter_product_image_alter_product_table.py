# Generated by Django 4.0.3 on 2022-06-09 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_sale_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterModelTable(
            name='product',
            table='store_product',
        ),
    ]

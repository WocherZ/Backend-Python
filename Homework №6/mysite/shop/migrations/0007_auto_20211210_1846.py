# Generated by Django 3.2.9 on 2021-12-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20211210_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='Описание продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', null=True, upload_to='', verbose_name='Картинка продукта'),
        ),
    ]

# Generated by Django 2.1.4 on 2019-11-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191107_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpriceblock',
            name='image_low',
        ),
        migrations.RemoveField(
            model_name='partnersblock',
            name='image_low',
        ),
        migrations.AlterField(
            model_name='newpriceblock',
            name='image_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Изображение для блока'),
        ),
        migrations.AlterField(
            model_name='newslider',
            name='slide_576_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Фото'),
        ),
        migrations.AlterField(
            model_name='newslider',
            name='slide_768_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Фото'),
        ),
        migrations.AlterField(
            model_name='newslider',
            name='slide_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Фото'),
        ),
        migrations.AlterField(
            model_name='newworkingmethods',
            name='image_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Изображение для элемента'),
        ),
        migrations.AlterField(
            model_name='partnersblock',
            name='image_full',
            field=models.BooleanField(default=False, verbose_name='Изображение на вcю ширину блока'),
        ),
        migrations.AlterField(
            model_name='partnersblock',
            name='image_webp',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='WEBP | Логотип партнера'),
        ),
    ]

# Generated by Django 2.1.4 on 2020-05-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200426_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='autocatalog',
            name='image_jp2',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='JPEG2000 | Изображение'),
        ),
    ]

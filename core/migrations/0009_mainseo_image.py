# Generated by Django 2.1.4 on 2020-04-19 13:28

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_advantagestext_methodstext'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainseo',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение для OpenGraph'),
        ),
    ]

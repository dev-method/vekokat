# Generated by Django 2.1.4 on 2020-02-04 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200204_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neworder',
            old_name='type',
            new_name='typecat',
        ),
        migrations.RenameField(
            model_name='neworder',
            old_name='val',
            new_name='valcat',
        ),
    ]

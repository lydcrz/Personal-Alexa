# Generated by Django 2.1.7 on 2019-04-15 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20190415_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='time_created',
            new_name='time_modified',
        ),
    ]
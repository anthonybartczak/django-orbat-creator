# Generated by Django 4.2 on 2023-04-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platoon',
            old_name='platoon',
            new_name='structure',
        ),
    ]
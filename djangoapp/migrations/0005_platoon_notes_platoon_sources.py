# Generated by Django 4.2 on 2023-04-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_platoon_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='platoon',
            name='notes',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='platoon',
            name='sources',
            field=models.JSONField(null=True),
        ),
    ]
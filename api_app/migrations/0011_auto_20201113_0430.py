# Generated by Django 3.1.3 on 2020-11-13 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0010_auto_20201113_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='department',
        ),
        migrations.RemoveField(
            model_name='post',
            name='department',
        ),
        migrations.RemoveField(
            model_name='post',
            name='team',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]

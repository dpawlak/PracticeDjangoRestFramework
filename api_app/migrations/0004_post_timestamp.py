# Generated by Django 3.0.5 on 2020-09-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_remove_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

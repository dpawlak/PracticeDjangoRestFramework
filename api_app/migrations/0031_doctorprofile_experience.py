# Generated by Django 3.1.3 on 2020-12-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0030_remove_doctorprofile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='experience',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

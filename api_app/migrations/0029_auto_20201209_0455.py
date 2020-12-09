# Generated by Django 3.1.3 on 2020-12-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0028_auto_20201204_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='experience',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='doctor',
            field=models.ManyToManyField(to='api_app.DoctorProfile'),
        ),
    ]

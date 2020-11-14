# Generated by Django 3.1.3 on 2020-11-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0018_doctorprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='shirt_sizes',
        ),
        migrations.AddField(
            model_name='post',
            name='building',
            field=models.CharField(choices=[('A', 'Building A'), ('B', 'Building B'), ('B', 'Building C')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]

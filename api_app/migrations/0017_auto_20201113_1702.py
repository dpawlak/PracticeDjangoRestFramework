# Generated by Django 3.1.3 on 2020-11-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0016_post_shirt_sizes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='patient_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default='Doe', max_length=100),
            preserve_default=False,
        ),
    ]
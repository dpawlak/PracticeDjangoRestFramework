# Generated by Django 3.1.3 on 2020-11-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0015_remove_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shirt_sizes',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='L', max_length=1),
            preserve_default=False,
        ),
    ]

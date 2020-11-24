# Generated by Django 3.1.3 on 2020-11-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0023_auto_20201120_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='tags',
            field=models.ManyToManyField(to='api_app.Tag'),
        ),
    ]
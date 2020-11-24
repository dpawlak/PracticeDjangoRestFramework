# Generated by Django 3.1.3 on 2020-11-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0017_auto_20201113_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_first_name', models.CharField(max_length=100)),
                ('doctor_last_name', models.CharField(max_length=100)),
                ('doctor_summary', models.TextField(max_length=500)),
            ],
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0027_auto_20201202_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorprofile',
            old_name='doctor_summary',
            new_name='doctor_bio',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='doctor_first_name',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='doctor_last_name',
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='doctor',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='focus',
            field=models.CharField(choices=[('Counseling', 'Counseling'), ('Disease', 'Disease'), ('Surgeon', 'Surgeon'), ('Data Analysis', 'Data Analysis')], default='test', max_length=25),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='post',
            name='doctor',
        ),
        migrations.AddField(
            model_name='post',
            name='doctor',
            field=models.ManyToManyField(null=True, to='api_app.DoctorProfile'),
        ),
    ]

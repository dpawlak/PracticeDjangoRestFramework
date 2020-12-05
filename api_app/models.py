from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class DoctorProfile(models.Model):

    FOCUS = (
        ('Counseling', 'Counseling'),
        ('Disease', 'Disease'),
        ('Surgeon', 'Surgeon'),
        ('Data Analysis', 'Data Analysis'),
    )

    doctor = models.CharField(max_length=50)
    doctor_bio = models.TextField(max_length=500)
    focus = models.CharField(max_length=25, choices=FOCUS)
    
    def __str__(self):
        return self.doctor

class Post(models.Model):

    SHIRT_SIZES = (
        ('A', 'Building A'),
        ('B', 'Building B'),
        ('C', 'Building C'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    doctor = models.ManyToManyField(DoctorProfile, null=True)
    timestamp = models.DateTimeField(auto_now=True)
    building = models.CharField(max_length=1, choices=SHIRT_SIZES)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.last_name



            
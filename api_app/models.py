from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):

    SHIRT_SIZES = (
        ('A', 'Building A'),
        ('B', 'Building B'),
        ('B', 'Building C'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    doctor = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now=True)
    building = models.CharField(max_length=1, choices=SHIRT_SIZES)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.last_name

class DoctorProfile(models.Model):

    customer = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    doctor_first_name = models.CharField(max_length=100)
    doctor_last_name = models.CharField(max_length=100)
    doctor_summary = models.TextField(max_length=500)
    
    def __str__(self):
        return self.doctor_last_name

            
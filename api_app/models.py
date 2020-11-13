from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    
    patient_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    doctor = models.CharField(max_length=100)

    timestamp = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.patient_name


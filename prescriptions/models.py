from django.db import models
from api_app.models import Post

# Create your models here.

class Prescriptions(models.Model):

    MEDICATIONS = (
        ('Advil', 'advil'),
        ('Tylenol', 'tylenol'),
        ('Propranolol', 'propranolol'),
        ('Benadryl', 'benadryl'),
    )
    
    patient = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    medication = models.CharField(max_length=20, choices=MEDICATIONS)
    refills = models.IntegerField()

    def __str__(self):
        return self.patient
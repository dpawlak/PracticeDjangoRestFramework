from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

Departments = (
    ('PED', 'pediatrics'),
    ('SRG', 'surgery'),
    ('TRM', 'trauma'),
    ('PAN', 'pandemics'),
)

Teams = (
    ('RED', 'red'),
    ('BLU', 'blue'),
    ('BLK', 'black'),
    ('GRY', 'grey'),
    ('WHT', 'white'),
)

Doctors = (
    ('JON', 'Dr. Jon'),
    ('ABE', 'Dr. Abhramson'),
    ('XIU', 'Dr. Xiu'),
)


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Team(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    patient_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    doctor = models.CharField(max_length=100)
    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, choices=Departments)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, choices=Teams)
    


    timestamp = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.patient_name


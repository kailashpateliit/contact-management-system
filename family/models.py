# Create your models here.
from pathlib import PosixPath
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class FamilyHead(models.Model):
    family_code = models.CharField(max_length=14, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    family_user = models.OneToOneField(User, on_delete=models.CASCADE)
    ritwik = models.CharField(max_length=127)
    date_of_init = models.DateField(default=date.today())
    def __str__(self):
        return self.full_name
        
class FamilyMembers(models.Model):
    initation_choices = (('yes', 'YES') ,('no','NO'))

    familyhead = models.ForeignKey(FamilyHead, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=150)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=150)
    initiation = models.CharField(choices=initation_choices, max_length=3)

    def __str__(self):
        return self.full_name
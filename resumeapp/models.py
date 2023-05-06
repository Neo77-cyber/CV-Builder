from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PersonalInfo(models.Model):
    username = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=800)
    address = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/')
    degree = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    school = models.CharField(max_length=200, null=True, blank=True)
    name_of_previous_job = models.CharField(max_length=200, null=True, blank=True)
    start_year_of_previous_job = models.IntegerField(null=True, blank=True)
    location_of_previous_job = models.CharField(max_length=200, null=True, blank=True)
    description_of_previous_job = models.TextField(max_length=2000, null=True, blank=True)
    name_of_current_job = models.CharField(max_length=200, null=True, blank= True)
    start_date_of_current_job = models.CharField(max_length=10, null=True, blank= True)
    location_of_current_job = models.CharField(max_length=200, null=True, blank= True)
    description_of_current_job = models.TextField(max_length=2000, null=True, blank= True)
    about = models.TextField(max_length=2000, null=True, blank= True)
    

    def get_absolute_url(self):
        return reverse("template")

    def __str__(self):
        return self.name







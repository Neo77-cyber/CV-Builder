from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import PersonalInfo




class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ('name', 'summary', 'address', 'phone_number', 'profile_picture', 'degree', 'year', 'school', 'name_of_previous_job', 'start_year_of_previous_job', 'location_of_previous_job', 'description_of_previous_job', 'name_of_current_job', 'start_date_of_current_job', 'location_of_current_job', 'description_of_current_job', 'about')


   


       
            

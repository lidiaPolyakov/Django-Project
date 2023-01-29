from django import forms
from .models import Users, Chore
from django.forms import ModelForm, TextInput, EmailInput

class Register(ModelForm):    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'type', 'birth_date', 'description', 'address', 'profile_pic']




class ChoreForm(ModelForm):    
    class Meta:
        model = Chore
        fields = ['title', 'description', 'date', 'start_hour', 'time', 'status']

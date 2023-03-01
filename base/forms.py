from django import forms
from .models import Users, Chore
from django.forms import ModelForm, TextInput, EmailInput
from datetime import datetime
from django.forms.widgets import DateInput

class PastDateInput(DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs']['max'] = datetime.today().strftime('%Y-%m-%d')
        super().__init__(*args, **kwargs)

class Register(ModelForm):    
    class Meta:
        model = Users
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }        
        fields = ['first_name', 'last_name', 'email', 'type', 'birth_date', 'description', 'address', 'profile_pic']




class ChoreForm(ModelForm):    
    class Meta:
        model = Chore
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }  
        fields = ['title', 'description', 'date', 'start_hour', 'time', 'status']

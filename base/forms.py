from django import forms
from .models import Users
from django.forms import ModelForm, TextInput, EmailInput

class Register(ModelForm):
    # TYPE = (
    #     ('S', 'Student'),
    #     ('E', 'Elder'),
    #     )
    # first_name = forms.CharField(max_length=200, label= 'first_name', required=True)
    # last_name = forms.CharField(max_length=200, label= 'last_name', required=True)
    # email = forms.CharField(max_length=200, label='email')
    # type = forms.ChoiceField(widget = forms.RadioSelect, choices = TYPE, required=True, label='type')
    # birth_date = forms.CharField(required=True, label='birth_date')
    # description = forms.CharField()
    # address = forms.CharField(max_length=200)
    # profile_pic = forms.ImageField(label='profile_pic')

    # first_name.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'First name'})
    # last_name.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Last name'})
    # email.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Email'})
    # type.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'User Type'})
    # birth_date.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Birth date'})
    # description.widget.attrs.update({'class': 'form-control', 'style': 'width: 800px;', 'placeholder': 'A little bit about you...'})
    # address.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Address'})
    # profile_pic.widget.attrs.update({'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Profile picture'})
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'type', 'birth_date', 'description', 'address', 'profile_pic']
        #fields = ['first_name']
        #fields = ('"first_name", "last_name", "email", "type", "birth_date", "description", "address", "profile_pic"',)
        # labels = '"first_name", "last_name", "email", "type", "birth_date", "description", "address", "profile_pic"'
        def __init__(self, *args, **kwargs):
            user = kwargs.pop("user", None)
            super().__init__(*args, **kwargs)

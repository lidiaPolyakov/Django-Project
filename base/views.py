from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
#from django.shortcuts import HttpResponseRedirect
#from django.http import HttpResponse

from .forms import Register
from .models import Users
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'base/home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            form = Register()
            return render(request, 'base/register.html', {'form': form} )

        else:
            return render(request, 'base/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'base/signup.html', {'form': form})


@login_required(login_url='/login/') 
def register(request):
        if request.method == 'POST':
            form = Register(request.POST, request.FILES)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                type = form.cleaned_data['type']
                birth_date= form.cleaned_data['birth_date']
                description = form.cleaned_data['description']
                address = form.cleaned_data['address']
                profile_pic = request.FILES['profile_pic']
                 # last_name = request.POST['last_name']
                item = Users(request.user.id, first_name, last_name, email, type, birth_date, description, address, profile_pic)
                item.save(); 
                # last_name = request.POST['last_name']
                # email = request.POST['email']
                # type = request.POST['type']
                # birth_date = request.POST['birth_date']
                # description = request.POST['description']
                # address = request.POST['address']
                # profile_pic= request.FILES['profile_pic']
                # user = Users(request.user.id , first_name = first_name, last_name = last_name, email = email, type = type, birth_date = birth_date, description= description, address = address, profile_pic = profile_pic)
                # user.save()
                return redirect('/')
            else:
                return render(request, 'base/signup.html')
        else:
            form = Register(request.POST, request.FILES)
        return render(request, 'register.html', {'form': form})

@login_required(login_url='/login/')      
def edit_profile(request, pk):
    
    item = Users.objects.get(pk = pk)
    if (request.method == 'POST'):
        form = Register(request.POST, request.FILES, instance=item)  
        if form.is_valid():    
            form.save()
            return redirect('/')
    else:
        form = Register(instance=item)  
        
    return render(request, 'base/register.html', {'form': form})



@login_required(login_url='/login/') 
def profile(request):
        item = Users.objects.get(pk = request.user.id)
        return render(request, 'base/profile.html', {'item': item})



@login_required(login_url='/login/') 
def signout(request):
    logout(request)
    return redirect('/')
    

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            form = Register()
            return render(request, 'base/register.html', {'form': form} )
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'base/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'base/login.html', {'form': form})
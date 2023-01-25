from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
#from django.shortcuts import HttpResponseRedirect
#from django.http import HttpResponse

from .forms import Register, ChoreForm
from .models import Users, Chore
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
        #initial_data = {'remaining_hours':'250'}
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
                item = Users(request.user.id, first_name, last_name, email, type, birth_date, description, address, profile_pic)
                item.save(); 
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

# def delete_profile(request, pk):
#     item = Users.objects.get(id=pk)
#     form = Register(request.POST, request.FILES, instance=item) 
#     item.is_delete = True
#     item.save()
#     return redirect('faculty-list')


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

inc=0
@login_required(login_url='/login/') 
def create_chore(request):
        print("not valid")
        if request.method == 'POST':
            form = ChoreForm(request.POST)
            print(request.user.id)
            if form.is_valid():
                print(" valid")
                title = form.cleaned_data['title']
                description = form.cleaned_data[ 'description']
                date= form.cleaned_data['date']
                start_hour= form.cleaned_data['start_hour']
                time = form.cleaned_data['time']
                global inc
                inc+=3
                chore = Chore(request.user.id,1,inc, title, description, date, start_hour, time)
                chore.save(); 
                return redirect('/')
            else:
                return render(request, 'base/signup.html')
        else:
            form = ChoreForm(request.POST)
        return render(request, 'base/create_chore.html', {'form': form})



@login_required(login_url='/login/') 
def my_chores(request):
    #item = Users.objects.get( pk = request.user.id)
    chore = Chore.objects.all()
    #context = {'item': item, 'chore': chore}     
    return render(request, 'base/my_chores.html', {'chore': chore})

        # chores = Chore.objects.filter(user_id = int(request.user.id))
        # item = Users.objects.get(pk = request.user.id)
        # context = {'chores': chores, "item": item}
        # return render(request, 'base/my_chores.html', context)
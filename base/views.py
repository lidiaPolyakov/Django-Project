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



# def home(request):
#     return render(request, 'base/home.html')


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
                user = Users(request.user.id, first_name, last_name, email, type, birth_date, description, address, profile_pic)
                user.save()
                return redirect('/')
            else:
                return render(request, 'base/signup.html')
        else:
            form = Register(request.POST, request.FILES)
            item = Users.objects.get(pk = request.user.id)
            context =  {'item': item, 'form': form}
        return render(request, 'base/register.html', context)

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
def view_elder_profile(request, pk):
        item = Users.objects.get(pk = request.user.id)
        elder = Users.objects.get(pk = pk)
        context = {'item': item, 'elder': elder}
        return render(request, 'base/view_elder_profile.html', context)



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
        item = Users.objects.get( pk = request.user.id)
        if request.method == 'POST':
            form = ChoreForm(request.POST)
            print(request.user.id)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data[ 'description']
                date= form.cleaned_data['date']
                start_hour= form.cleaned_data['start_hour']
                time = form.cleaned_data['time']
                status = form.cleaned_data['status']
                chore = Chore(request.user.id,1, title, description, date, start_hour, time, status)
                chore.save()
                return redirect('/')
            else:
                return render(request, 'base/signup.html')
        else:
            form = ChoreForm(request.POST)
        context = {'item': item, 'form': form}
        return render(request, 'base/create_chore.html',context)

@login_required(login_url='/login/')
def delete_chore(request,pk):
    chore = Chore.objects.all().filter(creation_time=pk).delete()
    return redirect('/')


@login_required(login_url='/login/')
def edit_chore(request, pk):
    chore = Chore.objects.get(pk = pk)
    Chore.objects.all().filter(creation_time=pk).delete()
    if (request.method == 'POST'):
        form = ChoreForm(request.POST, instance=chore)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChoreForm(instance=chore)
    item = Users.objects.get(pk = request.user.id)
    context = {'item': item, 'form': form} 
    return render(request, 'base/create_chore.html', context)


@login_required(login_url='/login/')
def done_chore(request,pk):
    chore = Chore.objects.get(pk = pk)
    chore.status = 'Done'
    chore.save()
    return redirect('/')

@login_required(login_url='/login/')
def my_chores(request):
    item = Users.objects.get( pk = request.user.id)
    chore = Chore.objects.all().filter(user_id=request.user.id).order_by('creation_time').values()
    context = {'item': item, 'chore': chore}
    return render(request, 'base/my_chores.html', context)


@login_required(login_url='/login/')
def chores_feed(request):
    item = Users.objects.get( pk = request.user.id)
    chore = Chore.objects.all().filter(status='Pending').order_by('creation_time').values()
    context = {'item': item, 'chore': chore}
    return render(request, 'base/chores_feed.html', context)


@login_required(login_url='/login/')
def register_chore(request, pk):
    chore = Chore.objects.get(pk = pk)
    student=Users.objects.get( pk = request.user.id)
    chore.status = 'Registed'
    chore.student_id=student.user_id
    chore.save()
    return redirect('/')

@login_required(login_url='/login/')
def my_registrations(request):
    item = Users.objects.get( pk = request.user.id)
    chore = Chore.objects.all().filter(student_id=request.user.id).order_by('creation_time').values()
    context = {'item': item, 'chore': chore}
    return render(request, 'base/my_registrations.html', context)


@login_required(login_url='/login/')
def unregister(request,pk):
    chore = Chore.objects.get(pk = pk)
    chore.status = 'Pending'
    student=Users.objects.get( pk =1)
    chore.student_id=student.user_id
    chore.save()
    return redirect('/')
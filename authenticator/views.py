from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.contrib import messages
from .models import User
from .forms import UserForm

# Create your views here.

def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
     
    return render(request, 'authentication/login.html', {'form': form,"value": 'Register'})       

def login(request):
    form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        form_class = UserForm
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print(user.username)
            return redirect('home')
        else:
            messages.error(request,"there was an error")
    return render(request, 'authentication/login.html', {'form':form,"value": 'Login'})

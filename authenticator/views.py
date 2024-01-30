from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages


from .forms import RegisterForm


# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
        else:   
            print(form.errors)
            return render(request,'authentication/register.html',{'form':form,'value':'register'})
    else:
	    
        return render(request,'authentication/register.html',{'form':form,'value':'register'})        


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username = username,password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
             
             messages.error(request,"there was an error")
             return render(request,'authentication/login.html',{'form':form,'value':'login'})        
  
    else:
        return render(request,'authentication/login.html',{'form':form,'value':'login'})        
    
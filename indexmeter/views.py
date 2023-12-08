from django.shortcuts import render
from .models import Emergencies
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import UserForm
# Create your views here.

def calculateSaveIndex(request):
    if request.method == 'POST':
    #   user = request.POST.get('User')
      Emergencies = Emergencies.objects.filter(user= request.user).all()
      print(Emergencies)

     
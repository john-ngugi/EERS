from django.shortcuts import render
from .models import Emergencies
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import requests
from django.http import JsonResponse


# from .forms import UserForm
# Create your views here.

def calculateSaveIndex(request):
    emergencies = Emergencies.objects.filter(user=request.user).values_list()
    print(emergencies)
    emergency_list = list(emergencies)
    print(emergency_list)

    print(emergency_list)
    if request.method == 'POST':
    #   user = request.POST.get('User')
      emergencies = Emergencies.objects.filter(user= request.user).all()
      print(list(emergencies))

      # return render(request,)
    return JsonResponse(emergency_list,safe=False)
  

     
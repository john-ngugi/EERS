from django.shortcuts import render #Used to render HTML templates and return them as HTTP responses.
import json 
from django.http import JsonResponse
from .models import *
# Create your views here.

# View function for the index page
def index(request):
    # Render the "home_main_content.html" template and return it as an HTTP response
    return render(request,"home/home_main_content.html")
# View function for the emergencies page
def emergencies(request):
    # Render the "emergencies.html" template and return it as an HTTP response
    return render(request,"home/emergencies.html")

def ongoingEmergencies(request):
    # Render the "emergencies.html" template and return it as an HTTP response
    return render(request,"home/ongoing_summary.html")

def dataRetriever(request):
    if request.method == 'POST':
       data = json.loads(request.body).get('data')
       x_coords =json.loads(request.body).get('coordinates_x')
       y_coords =json.loads(request.body).get('coordinates_y')
       print(x_coords,y_coords)
       if x_coords and y_coords:
           Coordinates.save(x_coordiante = x_coords, y_coordinate = y_coords)
           
       return JsonResponse({'data':data},safe=False)
    return render(request,"collectorapp/collector.html")



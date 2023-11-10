from django.shortcuts import render #Used to render HTML templates and return them as HTTP responses.
import json 
from django.http import JsonResponse
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
       return JsonResponse({'data':data},safe=False)
    return render(request,"collectorapp/collector.html")



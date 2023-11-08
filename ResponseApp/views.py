from django.shortcuts import render #Used to render HTML templates and return them as HTTP responses.

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
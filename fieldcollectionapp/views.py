from django.shortcuts import render

# Create your views here.

def collector(request):
    # Render the "collector.html" template and return it as an HTTP response
    return render(request,"collectorapp/collector.html")
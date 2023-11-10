from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from ResponseApp.views import dataRetriever

# Define URL patterns for the "ResponseApp" app
urlpatterns=[
    path("field-collector/",views.collector,name="collector"),
    path("/fc/field-collector/",dataRetriever,name="data-retriever"),
    
]
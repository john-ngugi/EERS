from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns for the "ResponseApp" app
urlpatterns=[
    # Define a URL pattern for the root URL (home page)
    path("",views.index,name="home"),
    # Define a URL pattern for the "emergencies" page
    path("emergencies/",views.emergencies,name="emergencies"),
    path("ongoing-emergencies/",views.ongoingEmergencies,name="ongoing-emergencies"),
    path("data-retriever",views.dataRetriever,name="data-retriever"),
]
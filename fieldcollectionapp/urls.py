from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define URL patterns for the "ResponseApp" app
urlpatterns=[
    path("field-collector/",views.collector,name="collector"),
]
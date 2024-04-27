from django.urls import path

from poiapp.views import homepage



urlpatterns = [
    path('', homepage,name='home'),
]
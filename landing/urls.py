from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingInfo.as_view(), name='home')
]

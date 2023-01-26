from django.urls import path
from .views import *

urlpatterns = [
    path('sendemail/',SendEmail,name="sendemail")
]


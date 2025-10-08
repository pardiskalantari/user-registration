from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', UserregistrationView.as_view(), name='create-user'),
]
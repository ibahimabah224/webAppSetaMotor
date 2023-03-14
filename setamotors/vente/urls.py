from django.urls import path 
from vente.views import index

urlpatterns=[
    path('', index , name='Home'),
]
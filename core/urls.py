from django.urls import path
from .views import *
urlpatterns = [
   path('', home, name="Home"),
   path('filter-data', filterProduct, name="filterProduct"),
]
    
from django.urls import path
from .views import *
urlpatterns = [
    path('<str:category>/',foodView,name="food"),
]

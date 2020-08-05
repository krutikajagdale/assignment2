from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("BMI.urls")),
    path('BMI/', include("BMI.urls")),
]

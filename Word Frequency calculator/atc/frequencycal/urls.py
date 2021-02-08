from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.frequency,name = 'frequency'),
    path('result/', views.result, name='result'),
]
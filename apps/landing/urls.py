from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('webapp-form/', views.webapp_form, name='webapp_form'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),  # Update the name to 'calculator'
    path('submit_query/', views.submit_query, name='submit_query'),

]

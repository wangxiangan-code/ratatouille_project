from django.urls import path
from . import views

urlpatterns = [
    path('select_ingredients/', views.select_ingredients, name='select_ingredients'),
    path('select/', views.select_ingredients, name='select_ingredients'),
    path('result/', views.recipe_results, name='recipe_results'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]


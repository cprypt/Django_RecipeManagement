from django.urls import path

from .views import base_views, recipe_views, element_views, cooking_views, detail_views

app_name = 'recipe'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:recipe_id>/', base_views.detail, name='detail'),

    # recipe_views.py
    path('recipe/create/', recipe_views.recipe_create, name='recipe_create'),
    path('recipe/modify/<int:recipe_id>/', recipe_views.recipe_modify, name='recipe_modify'),
    path('recipe/delete/<int:recipe_id>/', recipe_views.recipe_delete, name='recipe_delete'),
    
    # element_views.py
    path('element/create/<int:recipe_id>/', element_views.element_create, name='element_create'),
    path('element/delete/<int:element_id>/', element_views.element_delete, name='element_delete'),
    
    # cooking_views.py
    path('cooking/create/<int:recipe_id>/', cooking_views.cooking_create, name='cooking_create'),
    path('cooking/delete/<int:cooking_id>/', cooking_views.cooking_delete, name='cooking_delete'),

    # detail_views.py
    path('detail/create/<int:recipe_id>/', detail_views.detail_create, name='detail_create'),
    path('detail/modify/<int:detail_id>/', detail_views.detail_modify, name='detail_modify'),
    path('detail/delete/<int:detail_id>/', detail_views.detail_delete, name='detail_delete'),
]
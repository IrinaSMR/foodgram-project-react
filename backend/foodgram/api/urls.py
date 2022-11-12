from django.urls import include, path
from rest_framework import routers

from .views import (IngredientViewSet, RecipeViewSet, TagViewSet,
                    UsersViewSet, download_shopping_cart)

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'users', UsersViewSet, basename='users')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('recipes/download_shopping_cart/', download_shopping_cart),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]

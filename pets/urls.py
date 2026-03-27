from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BreedViewSet, OwnerViewSet, PetViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

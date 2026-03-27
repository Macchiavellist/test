from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Breed, Owner, Pet
from .serializers import CategorySerializer, BreedSerializer, OwnerSerializer, PetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.select_related('category').all()
    serializer_class = BreedSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name']


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.select_related('breed', 'breed__category', 'owner').all()
    serializer_class = PetSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'breed__name', 'breed__category__name']
    ordering_fields = ['name', 'price', 'age', 'created_at']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'])
    def available(self, request):
        pets = self.queryset.filter(status='available')
        serializer = self.get_serializer(pets, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_status(self, request):
        status = request.query_params.get('status', 'available')
        pets = self.queryset.filter(status=status)
        serializer = self.get_serializer(pets, many=True)
        return Response(serializer.data)

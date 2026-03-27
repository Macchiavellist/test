from rest_framework import serializers
from .models import Category, Breed, Owner, Pet


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BreedSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'category', 'category_name', 'description']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'created_at']
        read_only_fields = ['created_at']


class PetSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    category_name = serializers.CharField(source='breed.category.name', read_only=True)
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = [
            'id', 'name', 'breed', 'breed_name', 'category_name',
            'owner', 'owner_name', 'age', 'status', 'price',
            'description', 'photo', 'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_owner_name(self, obj):
        if obj.owner:
            return f'{obj.owner.first_name} {obj.owner.last_name}'
        return None

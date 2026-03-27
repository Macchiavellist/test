from django.contrib import admin
from .models import Category, Breed, Owner, Pet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'owner', 'age', 'status', 'price', 'created_at']
    list_filter = ['status', 'breed__category']
    search_fields = ['name', 'breed__name']
    ordering = ['-created_at']

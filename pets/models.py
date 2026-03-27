from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='breeds')
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ]

    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, related_name='pets')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True, related_name='pets')
    age = models.PositiveIntegerField(help_text='Age in months')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='pets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.breed})'

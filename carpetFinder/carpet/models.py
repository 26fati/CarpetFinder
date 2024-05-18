from django.db import models
from django.contrib.auth.models import User

class Carpet(models.Model):
    STYLE_CHOICES = [
        ('herringbone', 'Herringbone'),
        ('saxony', 'Saxony'),
        ('twist', 'Twist'),
        ('woven', 'Woven'),
        ('velvet', 'Velvet'),
    ]

    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('black', 'Black'),
        ('white', 'White'),
    ]

    SUITABILITY_CHOICES = [
        ('living_room', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('dining_room', 'Dining Room'),
        ('bathroom', 'Bathroom'),
        ('hallway', 'Hallway'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carpets')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=50, null=True, blank=True)
    style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    suitability = models.CharField(max_length=20, choices=SUITABILITY_CHOICES)
    image = models.ImageField(upload_to='carpet_images', blank=True)
    is_sold = models.BooleanField(default=False)
    location = models.CharField(max_length=100, default='algeria')

    def __str__(self):
        return self.name
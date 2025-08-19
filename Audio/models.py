from django.db import models
from .models import *
from django.utils.safestring import mark_safe

# Create your models here.
class register_view(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    cpass=models.CharField(max_length=8)
    
class login_view(models.Model):
    name=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=8)

class contact_us(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message=models.CharField(max_length=500)

class Audio(models.Model):
    title = models.CharField(max_length=255, default="Untitled")
    artist = models.CharField(max_length=255, default="Unknown Artist")
    file_path = models.FileField(upload_to='audio/', null=True, blank=True)

    def __str__(self):
        return self.title

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    image = models.ImageField(upload_to='city_images/') 
    rating = models.FloatField(default=0)
    reviews = models.IntegerField(default=0)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    days_open = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Booking(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    member = models.PositiveIntegerField()
    price = models.ImageField()



class Rating(models.Model):
    PLACE_CHOICES = [
        ("adalaj-stepwell", "Adalaj Stepwell"),
        ("rani-ki-vav", "Rani Ki Vav"),
        ("vintage-car-museum", "The Vintage Car Museum"),
        ("sabarmati-aashram", "Sabarmati Aashram"),
        ("hutheesing-jain-temple", "Hutheesing Jain Temple"),
        ("jama-masjid", "Jama Masjid"),
        ("jhulta-minar", "Jhulta Minar"),
        ("kankaria-lake", "Kankaria Lake"),
        ("lal-darvaja", "Lal Darvaja"),
        ("sabarmati-riverfront", "Sabarmati Riverfront"),
    ]

    place = models.CharField(max_length=50, choices=PLACE_CHOICES)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.get_place_display()} - {self.rating}/10"

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(register_view)
admin.site.register(login_view)
admin.site.register(contact_us)


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'file_path')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'reviews', 'contact_number')



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'member', 'price')



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('place', 'rating')

from django.contrib import admin
from app.models import Car

# Register your models here.
ADMIN_TITLE = 'Showroom Admin'

class CarProfile(admin.ModelAdmin):
    
    model = Car,
    list_display = ['year', 'make', 'model']
    exclude = []

admin.site.register(Car, CarProfile)
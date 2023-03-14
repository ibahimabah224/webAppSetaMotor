from django.contrib import admin
from .models import category, vehicule

# Register your models here.
class adminCategory(admin.ModelAdmin):
    list_display=('name','date_add')

class adminVehicule(admin.ModelAdmin):
    list_display=('immatriculation','mark','price','category','date_add')

admin.site.register(category,adminCategory)
admin.site.register(vehicule,adminVehicule)

from django.contrib import admin

# Register your models here.
from .models import *  # Import your model
admin.site.register(menuitem)
admin.site.register(Reservation)
admin.site.register(Review)
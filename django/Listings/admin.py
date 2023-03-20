from django.contrib import admin
from .models import Listing,ListingImage

# Register your models here.

admin.site.register(ListingImage)
admin.site.register(Listing)

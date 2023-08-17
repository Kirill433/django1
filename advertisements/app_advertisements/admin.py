from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_date', 'updated_date', 'auction', 'image_admin']
    list_filter = ['auction']
    pass

admin.site.register(Advertisement, AdvertisementAdmin)

# Register your models here.

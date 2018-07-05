from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['photo_tag','name','amount',]

    def photo_tag(self, item):
        if item.photo:
            return mark_safe('<img src = "{}" style="width: 75 px" />'.format(item.photo.url))
        return None

@admin.register(models.order)
class orderAdmin(admin.ModelAdmin):
    pass
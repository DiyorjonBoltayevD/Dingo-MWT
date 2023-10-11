from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(FoodModel)
class FoodModelAdmin(admin.ModelAdmin):
    list_display = ("title", "about", "price", "exclusive")
    list_display_plural = ("title", "about")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "created"]


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))
    list_display = ["full_name"]


@admin.register(ChefLevel)
class ChefLevelAdmin(admin.ModelAdmin):
    list_display = ["ch_level"]


@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ["name", 'phone_number', "num_of_g", "date", "time"]
    list_display_plural = ["name", "date", "time"]
    search_fields = ["name"]


admin.site.register(TagModel)
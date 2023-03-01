from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django_select2.forms import Select2Widget

from .models import Category, Cars, PartCard, Photo

admin.site.register(Category)


class PhotoInline(admin.TabularInline):
    model = Photo

    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Изображение'


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')
    ordering = ('id',)
    list_filter = ('name',)


@admin.register(PartCard)
class PartCardAdmin(admin.ModelAdmin):
    list_display = ('category', 'car', 'car_year', 'price')
    inlines = [PhotoInline]
    search_fields = ('category__name', 'car__name', 'car__model', 'article')
    list_filter = ('car__name', )
    formfield_overrides = {
        models.ForeignKey: {'widget': Select2Widget},
    }


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('part_card', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


admin.site.site_title = 'RD-Motors'
admin.site.site_header = 'RD-Motors'

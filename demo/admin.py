from django.contrib import admin

# Register your models here.

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title']

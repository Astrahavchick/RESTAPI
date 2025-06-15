from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
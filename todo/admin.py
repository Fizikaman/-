from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    """Наследуемся от ModelAdmin чтобы кастомизировать модель
    для отображения в админке"""
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
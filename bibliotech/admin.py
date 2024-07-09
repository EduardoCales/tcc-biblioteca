from django.contrib import admin
from .models import Category, Livro

class CategoryAdmin(admin.ModelAdmin):
    ...

class LivroAdmin(admin.ModelAdmin):
    ...

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
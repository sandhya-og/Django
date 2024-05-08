# accounts/admin.py
from django.contrib import admin
from .models import Category, Tag, Comment, Like

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Tag)

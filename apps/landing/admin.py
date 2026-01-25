from django.contrib import admin
from .models import Application, BlogPost

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'credit_amount', 'region', 'collateral', 'source', 'created_at')
    list_filter = ('source', 'region', 'collateral', 'created_at')
    search_fields = ('full_name', 'phone_number')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'summary')

from django.contrib import admin
from .models import MenuItem

# Register your models here.
class memberAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "url")
admin.site.register(MenuItem, memberAdmin )

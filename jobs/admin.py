from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','role')
    list_display_links = ('id', 'title')
    # list_filter = ('creator' ,) 
    search_fields = ('title','role')
    list_per_page = 20

admin.site.register(Job , JobAdmin)
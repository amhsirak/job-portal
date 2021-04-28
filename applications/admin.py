from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'job', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'job')
  list_per_page = 20

admin.site.register(Application, ApplicationAdmin)



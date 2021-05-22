from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
  
  exclude = ('creator',)
  list_display = ('id', 'name', 'job', 'email', 'contact_date')
  list_display_links = ('id', 'name')

  def get_queryset(self, request, *args, **kwargs):
    if request.user.is_superuser:
      return Application.objects.all()
    else:
      return Application.objects.filter(creator=request.user)

  def get_list_display(self, request, *args, **kwargs):
    if request.user.is_superuser:
      return ('id', 'name', 'job', 'email', 'contact_date')
    else:
      return ('id', 'name', 'job', 'email', 'contact_date')

  def save_model(self, request, obj, form, change):
    obj.creator = request.user
    obj.save()
  
admin.site.register(Application, ApplicationAdmin)




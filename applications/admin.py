from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
  exclude = ('job',)
  list_display = ('id','job_id','resume', 'contact_date')

  def get_queryset(self, request, *args, **kwargs):
    if request.user.is_superuser:
      return Application.objects.all()
    else:
      return Application.objects.filter(job=request.user)

  def get_list_display(self, request, *args, **kwargs):
    if request.user.is_superuser:
      return ('id','job','job_id','resume', 'contact_date')
    else:
      return ('id','job_id','resume', 'contact_date')

def save_model(self, request, obj, form, change):
  obj.creator = request.user
  obj.save()


  
admin.site.register(Application, ApplicationAdmin)

# list_display = ('id', 'name', 'job', 'email', 'contact_date')
#   list_display_links = ('id', 'name')
#   search_fields = ('name', 'email', 'job')
#   list_per_page = 20



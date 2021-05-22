from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    list_display = ('title','role', 'company', 'location')

    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creator=request.user)

    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('title','role', 'company', 'location')
        else:
            return ('title','role', 'location')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

admin.site.register(Job , JobAdmin)



    # list_display = ('id', 'title','role')
    # list_display_links = ('id', 'title')
    # list_filter = ('creator' ,) 
    # search_fields = ('title','role')
    # list_per_page = 20
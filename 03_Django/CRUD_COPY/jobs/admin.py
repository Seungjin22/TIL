from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'past_job',)

admin.site.register(Job, JobAdmin)
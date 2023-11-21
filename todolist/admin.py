from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display=('id','name','description','is_completed')
    list_filter=('is_completed',)
    search_fields=('name',)
    list_editable=('name',)
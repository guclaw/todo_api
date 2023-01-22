from django.contrib import admin
from . import models


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'body'
    )


admin.site.register(models.Todo, TodoAdmin)

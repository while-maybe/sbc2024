from django.contrib import admin

# Register your models here.
from .models import Task

# this enables the model to be managed by the admin site
admin.site.register(Task)

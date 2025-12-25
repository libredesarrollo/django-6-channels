from django.contrib import admin

from .models import Alert

# Register your models here.

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    pass
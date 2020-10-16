from django.contrib import admin
from .models import Timer 
# Register your models here.

class TimerAdmin(admin.ModelAdmin):
    list_display = ('user', 'register_date')

admin.site.register(Timer, TimerAdmin)
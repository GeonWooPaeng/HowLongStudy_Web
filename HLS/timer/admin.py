from django.contrib import admin
from .models import Timer 
# Register your models here.

class TimerAdmin(admin.ModelAdmin):
    list_display = ('user', 'study_time')

admin.site.register(Timer, TimerAdmin)
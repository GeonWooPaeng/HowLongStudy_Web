from django.shortcuts import render
from .forms import SaveForm 
# from django.views.generic import ListView
# from .models import Timer
# Create your views here.


class SaveTime(Formview):
    template_name = 'timer.html'
    form_class = SaveForm
    success_url = '/'

# class timerRank(ListView):
#     model = Timer
#     template_name = 'timer_rank.html'
#     context_object_name = 'timer_list'
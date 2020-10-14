from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Timer
# Create your views here.

def timer(request):
    return render(request, 'timer.html')


# class TimerRank(ListView):
#     model = Timer
#     template_name = 'timer_rank.html'
#     context_object_name = 'timer_list'
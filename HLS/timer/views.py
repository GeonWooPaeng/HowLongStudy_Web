from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.generic import ListView,FormView 
from django.core.paginator import Paginator
from user.decorators import login_required
from user.models import User
from .models import Timer


def SaveTime(request):
    if not request.session.get('user'):
        return redirect('/login')

    if request.method == 'POST':
        prod = User.objects.get(email=request.session.get('user'))
        shour = int(request.POST.get('study_hour_input',""))
        smin = int(request.POST.get('study_min_input', ""))
        ssec = int(request.POST.get('study_sec_input',""))
        timer = Timer(
            user=prod,
            study_day = request.POST.get('study_day',0),
            study_hour= shour,
            study_min= smin,
            study_sec = ssec
            )

        if shour > 24:
            prod.study_day += 1 
            shour = 0

        timer.save()
    
    return render(request, 'timer.html')


def board_list(request):
    boards_all = Timer.objects.all().order_by('-id')
    page = int(request.GET.get('p',1))
    paginator = Paginator(boards_all, 5) 
    boards = paginator.get_page(page)
    return render(request, "timer_rank.html",{"boards":boards})


class TimerList(ListView):
    template_name = 'timer_rank.html'
    context_object_name= 'timers'
    
    def get_queryset(self):
        timer_all = Timer.objects.all().order_by('-id')
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(timer_all,5)
        queryset = paginator.get_page(page)
        return queryset

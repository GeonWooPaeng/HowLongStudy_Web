from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from user.decorators import login_required
from django.views.generic import ListView 
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
        if ssec > 60:
            prod.study_min += 1
            smin = 0 
        
        elif smin > 60:
            prod.study_hour += 1 
            smin = 0

        elif shour > 24:
            prod.study_day += 1 
            shour = 0

        timer.save()
    
    return render(request, 'timer.html')


# @method_decorator(login_required, name='dispatch')
class TimerList(ListView):
    template_name = 'timer_rank.html'
    context_object_name= 'timer_list'

    # def get_queryset(self, **kwargs):
    #     queryset = Timer.objects.filter(user_email=self.request.session.get('user'))
    #     return queryset 
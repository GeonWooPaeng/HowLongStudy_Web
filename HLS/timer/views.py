from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from user.models import User
from .models import Timer
# from .forms import SaveForm 

# from user.decorators import login_required
# from django.views.generic import ListView
# from .models import Timer
# Create your views here.

# @method_decorator(login_required, name='dispatch')
# class SaveTime(FormView):
#     template_name = 'timer.html'
#     form_class = SaveForm
#     success_url = '/'

#     def form_valid(self, form):
#         timer = Timer(
#             user=form.data.get('user'),
#             study_hour=form.data.get('study_hour'),
#             study_min=form.data.get('study_min'),
#             study_sec=form.data.get('study_sec')
#         )
#         timer.save() 
#         return super().form_valid(form)

# class timerRank(ListView):
#     model = Timer
#     template_name = 'timer_rank.html'
#     context_object_name = 'timer_list'

def SaveTime(request):
    if not request.session.get('user'):
        return redirect('/login')

    if request.method == 'POST':
        timer = Timer(
            user=User.objects.get(email=request.session.get('user')),
            study_day = request.POST.get('study_day',0),
            study_hour=request.POST.get('study_hour',0),
            study_min=request.POST.get('study_min', 0),
            study_sec = int(request.POST.get('study_sec',0))
            )
        timer.save()
    
    return render(request, 'timer.html')

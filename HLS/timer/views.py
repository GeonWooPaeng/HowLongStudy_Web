from django.shortcuts import render
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
# from .forms import SaveForm 
# from .models import Timer

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
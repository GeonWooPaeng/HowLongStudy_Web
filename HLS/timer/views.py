from django.shortcuts import render

# Create your views here.

def timer(request):
    return render(request, 'timer.html')
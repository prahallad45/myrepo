from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from home.models import task
# Create your views here.
def home(request):
    if request.method == "POST":
        task.tasktitle = request.POST.get('title')
        task.taskdesc = request.POST.get('desc')
        task.save()

    return render(request,'index.html')

def task(request):
    return render(request,'task.html')
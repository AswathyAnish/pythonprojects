from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('classdetailview',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classview')
# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority,date=date)
        task.save()
    return render(request, 'home.html', {'task1': task1})


# def details(request):
#    return render(request, 'details.html',)
def delete(request, taskid):
    if request.method == 'POST':
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')

    return render(request, 'delete.html' )

def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,request.FILES,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
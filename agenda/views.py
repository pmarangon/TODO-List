from django.shortcuts import render
from agenda.models import Task
import datetime #
from agenda.forms import  TaskModelForm


hoje = datetime.date.today().strftime("%Y-%m-%d")

def agenda_view(request):
    compromissos = Task.objects.filter(deadline__lte=hoje)
    return render(
    request, 
    'agenda.html',
    {'compromisso':compromissos}
    )  
    
    
    def new_task_view(request):
        if request.method=='POST':
         new_task_form = TaskForm(request.POST)
         if  new_task_form is valid():
             new_task_form.save()
             return redirect('task_list')
        else:
             new_task_form = TaskModelForm()
        return render(request, 'new_task.html',{'new_task_form':new_task_view})

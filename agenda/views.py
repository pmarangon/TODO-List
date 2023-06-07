from django.shortcuts import render
from agenda.models import Task
import datetime #


hoje = datetime.date.today().strftime("%Y-%m-%d")

def agenda_view(request):
    compromissos = Task.objects.filter(deadline__lte=hoje)
    return render(
    request, 
    'agenda.html',
    {'compromisso':compromissos}
    )  

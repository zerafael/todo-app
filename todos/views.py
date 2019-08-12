from django.shortcuts import render
from .models import ToDo

def todo_list(request):
    todos = ToDo.objects.order_by('created_at')
    return render(request, 'todo_list.html', {'todos': todos})

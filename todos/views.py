from django.shortcuts import render, get_object_or_404
from .models import ToDo

def todo_list(request):
    todos = ToDo.objects.order_by('created_at')
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})
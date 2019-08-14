from django.shortcuts import render, get_object_or_404, redirect

from .models import ToDo
from .forms import ToDoForm

def todo_list(request):
    todos = ToDo.objects.order_by('created_at')
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

def todo_new(request):

    if request.method == "POST":
        form = ToDoForm(request.POST)

        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)

    else:
        form = ToDoForm()

    return render(request, 'todo_edit.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)

    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)

        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)

    else:
        form = ToDoForm(instance=todo)

    return render(request, 'todo_edit.html', {'form': form})
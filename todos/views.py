from django.shortcuts import render

def todo_list(request):
    return render(request, 'todo_list.html', {})

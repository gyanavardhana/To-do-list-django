from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def index(request):
    todo = Todo.objects.all()
    context = {
        'todos':todo
    }
    if request.method=='POST':
        title = request.POST['title']
        if title!='':
            new_todo = Todo(
                title=title
            )
            new_todo.save()
        else:
            return redirect('/')

        
        return redirect('/')
        
    return render(request, 'index.html', context)
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
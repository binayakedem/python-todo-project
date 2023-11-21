from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.


# function based view
def home(request):
    obj=Task.objects
    tasks=obj.all()
    tatal_tasks=tasks.count()
    completed_tasks=obj.filter(is_completed=True).count()
    value="this is me binaya limbu"
    data={
        'tasks':tasks,
        'total_tasks':tatal_tasks,
        'completed_tasks':completed_tasks,   
        'value':value
    }
      
    return render(request,'index.html',data)
    
#     data={
#         "users" : [
#     {'id': 1, 'name': 'Binaya', 'address': 'Kathmandu', 'age': 25, 'email': 'binaya@example.com'},
#     {'id': 2, 'name': 'Sara', 'address': 'New York', 'age': 28, 'email': 'sara@example.com'},
#     {'id': 3, 'name': 'Raj', 'address': 'Mumbai', 'age': 30, 'email': 'raj@example.com'},
#     {'id': 4, 'name': 'Anna', 'address': 'London', 'age': 22, 'email': 'anna@example.com'},
#     {'id': 5, 'name': 'Juan', 'address': 'Barcelona', 'age': 35, 'email': 'juan@example.com'},
#     {'id': 6, 'name': 'Aisha', 'address': 'Dubai', 'age': 27, 'email': 'aisha@example.com'},
#     {'id': 7, 'name': 'Takashi', 'address': 'Tokyo', 'age': 32, 'email': 'takashi@example.com'},
#     {'id': 8, 'name': 'Elena', 'address': 'Paris', 'age': 29, 'email': 'elena@example.com'},
#     {'id': 9, 'name': 'Carlos', 'address': 'Mexico City', 'age': 31, 'email': 'carlos@example.com'},
#     {'id': 10, 'name': 'Lila', 'address': 'Sydney', 'age': 26, 'email': 'lila@example.com'},
#     {'id': 11, 'name': 'Ahmed', 'address': 'Cairo', 'age': 33, 'email': 'ahmed@example.com'}
# ]
#     }
    

def contact(request):
    return render(request,"contact.html")

def about(request):
    return HttpResponse("Hi i am from about us")

def create(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        if name is None and description is None:
            context={
                "error":"Both fields are required"
            }
        Task.objects.create(
            name=name,
            description=description,
        )
        return redirect('/')
        
    return render(request,'create.html')


def mark(request,pk):
    task=Task.objects.get(pk=pk)
    task.is_completed=True
    task.save()
    return redirect("/")


def edit(request,pk):
    task=Task.objects.get(pk=pk)
    context={
        "task":task
    }
    return render(request,"edit.html",context)


def update(request,pk):
    name=request.POST.get('name')
    description=request.POST.get('description')
    task=Task.objects.get(pk=pk)
    
    task.name=name
    task.description=description
    task.save()
    return redirect("/")

def delete(request, pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    return redirect("/")
    
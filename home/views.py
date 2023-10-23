from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDo
from .forms import updateForm
from .forms import Form
from django.contrib import messages

def homePage(request):
    return render(request, 'home.html')
    
def helloPage(request):
    p= ToDo.objects.all()
    return render(request, 'hello.html', {'p':p})

def showinfo(request, x):
    p=ToDo.objects.get(pk=x)
    return render(request, 'showinfo.html', {'p':p})

def delete(request, id):
    ToDo.objects.get(pk=id).delete()
    messages.success(request, 'با موفقیت حذف شد', 'success')
    return redirect('hello')


def create(request):
    if request.method == 'POST':
        form1=Form(request.POST)
        if form1.is_valid():
            cd= form1.cleaned_data
            ToDo.objects.create(title=cd['title'],body=cd['body'],dateCreate=cd['dateCreate'])
            messages.success(request, 'با موفقیت اضافه شد', 'success')
            return redirect('hello')
    else:
        form1=Form()
    return render(request, 'create.html', {'form1':form1})


def update(request, id):
    Todo= ToDo.objects.get(id=id)
    if request.method == "POST":
        form= updateForm(request.POST, instance=Todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'با موفقیت آپدیت شد', 'success')
            return redirect('showinfo',id)
    else:
        form=updateForm(instance=Todo)
    return render(request, 'update.html', {'form':form})
    
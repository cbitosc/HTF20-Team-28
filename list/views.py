from django.shortcuts import render,redirect
from .models import Tasks
from .forms import task_form
# Create your views here.

def mhome(request):
	return render(request,'list/mhome.html')

	
def home(request):
	tasks=Tasks.objects.all()
	form=task_form()

	if request.method=='POST':
		form=task_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={'tasks':tasks,'form':form}

	return render(request,'list/home.html',context)


def update(request,pk):
	task=Tasks.objects.get(id=pk)
	form=task_form(instance=task)

	if request.method=='POST':
		form=task_form(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={'form':form}
	return render(request,'list/update.html',context)


def delete(request,pk):
	task=Tasks.objects.get(id=pk)
	
	if request.method=='POST':
		task.delete()
		return redirect('/')

	context={'task':task}
	return render(request,'list/delete.html',context)

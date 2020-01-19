from django.shortcuts import render,redirect

from .models import List
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
				
		all_items = List.objects.all
		return render(request,'home.html',{'all_items':all_items})

def delete(request,list_id):
	item=List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('item has been deleted'))
	return redirect('home')

def edit (request,list_id):
	if request.method == "POST":
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)
	else:
		item=List.objects.get(pk=list_id)
		return render(request,'edit.html',{'item':item})

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from myapp.models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def home(request):
	return HttpResponse('Home')

def shopping_list(request):
	context = {'items':ShoppingListItem.objects.all()}
	return render(request, 'myapp/shopping_list.html', context)

@csrf_exempt 
def receive_shopping_list_add(request):
	if request.method=='POST':
		item_name = request.POST['add'].capitalize()
		if (ShoppingListItem.objects.filter(name = item_name)):
			messages.warning(request, 'There is already an input with the name "' + item_name + '"')
		else:
			item = ShoppingListItem()
			item.name = item_name.capitalize()
			item.save()	
	return HttpResponseRedirect(reverse('myapp:shopping_list'))


@csrf_exempt 
def receive_shopping_list_delete(request):
	if request.method=='POST':
		item_name = request.POST['delete'].capitalize()


		if (ShoppingListItem.objects.filter(name = item_name)):
			item_to_delete = ShoppingListItem.objects.get(name = item_name)
			item_to_delete.delete()

		else:
			messages.error(request, 'Sorry, there is no item with the name "' + item_name + '"')

		
	return HttpResponseRedirect(reverse('myapp:shopping_list'))


@csrf_exempt 
def receive_shopping_list_clear(request):
	if request.method=='POST':
		ShoppingListItem.objects.all().delete()
		
	return HttpResponseRedirect(reverse('myapp:shopping_list'))



@csrf_exempt 
def read_shopping_list(request):

	current_shopping_list = list(ShoppingListItem.objects.values('name'))
	print (ShoppingListItem.objects.values('name'))
	print (list(ShoppingListItem.objects.values('name')))


		
	return JsonResponse(current_shopping_list, safe = False)




#Reminders



def reminders(request):
	context = {'items':Reminder.objects.all()}
	return render(request, 'myapp/reminders.html', context)




@csrf_exempt 
def receive_reminders_add(request):
	if request.method=='POST':
		item_text = request.POST['add']   #.capitalize()
		item = Reminder()
		item.text = item_text
		item.save()	
	return HttpResponseRedirect(reverse('myapp:reminders'))


@csrf_exempt 
def receive_reminders_delete(request):
	if request.method=='POST':
		item_id = request.POST['delete']


		if (Reminder.objects.filter(id = item_id)):
			item_to_delete = Reminder.objects.get(id = item_id)
			item_to_delete.delete()

		else:
			messages.error(request, 'Sorry, there is no reminder with the id "' + item_id + '"')

		
	return HttpResponseRedirect(reverse('myapp:reminders'))


@csrf_exempt 
def receive_reminders_clear(request):
	if request.method=='POST':
		Reminder.objects.all().delete()
		
	return HttpResponseRedirect(reverse('myapp:reminders'))



@csrf_exempt 
def read_reminders(request):

	current_reminders = list(Reminder.objects.values('text'))
		
	return JsonResponse(current_reminders, safe = False)
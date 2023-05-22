from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_pizza(request):
    if request.method == "POST":
				# create a new copy of the form with the data the user
				# entered , it is stored in request.POST
        form = PizzaForm(request.POST)
        if form.is_valid():
            emp = form.save() # create the Employee object and save it
						# send the user to a confirmation page saying
						# confirming that they filled in the form and the data was saved
            return redirect('/deliverypayment')
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'createpizza.html', {'form': form})
    else:
        # normal get reuqest, user wants to see the form
        form = PizzaForm()
        return render(request, 'createpizza.html', {'form': form})

def delivery(request):
    if request.method == "POST":
				# create a new copy of the form with the data the user
				# entered , it is stored in request.POST
        form = DeliveryForm(request.POST)
        if form.is_valid():
            deli = form.save() # create the Employee object and save it
						# send the user to a confirmation page saying
						# confirming that they filled in the form and the data was saved
            return redirect('/done')
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'delivery.html', {'form': form})
    else:
        # normal get reuqest, user wants to see the form
        form = DeliveryForm()
        return render(request, 'delivery.html', {'form': form})

def success(request):
    most_recent_pizza = Pizza.objects.latest('id')
    most_recent_del = Delivery.objects.latest('id')


    context = {
        'most_recent_pizza': most_recent_pizza,
        'most_recent_del': most_recent_del
    }

    return render(request, 'success.html', context)
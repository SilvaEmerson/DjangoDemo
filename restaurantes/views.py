from django.shortcuts import render
from .models import Restaurant
from .forms import RestaurantNew
from django.shortcuts import redirect
# Create your views here.

def rests_list(request):
	restaurants = Restaurant.objects.all()
	return render(request, 'restaurantes/rests_list.html',
			{'restaurants': restaurants})

def restaurant_new(request):
	if request.method == "POST":
		form = RestaurantNew(request.POST)
		if form.is_valid():
			restaurant = form.save(commit=False)
			# restaurant.name = request.name
			# restaurant.owner = request.owner
			# restaurant.adress = request.adress
			# restaurant.fund_date = request.fund_date
			# restaurant.speciality = request.speciality
			restaurant.save()

			return redirect('rests_list')
	else:
		form = RestaurantNew()

	return render(request, 'restaurantes/form_create_restaurant.html',
		{'form': form})

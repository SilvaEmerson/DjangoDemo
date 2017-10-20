from django.shortcuts import render
from .models import Restaurant

# Create your views here.

def rests_list(request):
	restaurants = Restaurant.objects.all()
	return render(request, 'restaurantes/rests_list.html',
			{'restaurants': restaurants})
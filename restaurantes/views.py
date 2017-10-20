from django.shortcuts import render

# Create your views here.

def rests_list(request):
	return render(request, 'restaurantes/rests_list.html',{})
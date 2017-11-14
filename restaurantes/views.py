from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Restaurant
from .forms import RestaurantNew
# Create your views here.

satisfations = {'sentiment_very_dissatisfied': 'vote0',
                'sentiment_dissatisfied': 'vote1',
                'sentiment_neutral': 'vote2', 'sentiment_satisfied': 'vote3',
                'sentiment_very_satisfied': 'vote4'}


def rests_list(request):
    global satisfations
    satisfations_icons = list(satisfations.keys())
    urls = list(satisfations.values())
    urls.sort()
    numbers = [i for i in range(5)]
    restaurants = Restaurant.objects.order_by('name')
    return render(request, 'restaurantes/rests_list.html',
                  {'restaurants': restaurants,
                   'satisfations': satisfations,
                   'urls': urls,
                   'numbers': numbers})


def restaurant_new(request):
    if request.method == "POST":
        form = RestaurantNew(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('rests_list')
    else:
        form = RestaurantNew()

    return render(request, 'restaurantes/form_create_restaurant.html',
                  {'form': form})


def restaurant_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        form = RestaurantNew(request.POST, instance=restaurant)
        print(form)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('rests_list')
    else:
        form = RestaurantNew(instance=restaurant)

    return render(request, 'restaurantes/form_edit_restaurant.html',
                  {'form': form, 'restaurant': restaurant})


def restaurant_delete(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return redirect('rests_list')


def vote0(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.votes += 1
    return redirect('rests_list')


def vote1(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.votes += 1
    restaurant.total_points += 1
    return redirect('rests_list')


def vote2(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.votes += 1
    restaurant.total_points += 2
    return redirect('rests_list')


def vote3(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.votes += 1
    restaurant.total_points += 3
    return redirect('rests_list')


def vote4(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.votes += 1
    restaurant.total_points += 4
    return redirect('rests_list')

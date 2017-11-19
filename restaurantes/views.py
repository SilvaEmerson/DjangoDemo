from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Restaurant, Comments
from .forms import RestaurantNew, RestaurantFeed
# Create your views here.


def rests_list(request):
    restaurants = Restaurant.objects.order_by('name')
    return render(request, 'restaurantes/rests_list.html',
                  {'restaurants': restaurants})


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


def do_feedback(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        print('post')
        feedback = RestaurantFeed(request.POST)
        if feedback.is_valid():
            feed = feedback.cleaned_data['feed']
            newComment = Comments(comment=feed)
            newComment.save()
            restaurant.comments = newComment
            restaurant.save()
            return redirect('rests_list')
    else:
        print('get')
        rest_feedbacks = Comments.objects.filter(id=pk)
    return render(request, 'restaurantes/feedback.html',
                  {'rest_feedbacks': rest_feedbacks})


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

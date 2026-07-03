from django.shortcuts import render
from django.http import HttpResponse
from random import sample


# Create your views here.
def index(request):
    print(request)
    return HttpResponse("Hello Client,Welcome to index page")


def show_fruits(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]

    selected_fruits = sample(fruits, 5)

    return render(request,"fruits.html",{"fruits":selected_fruits})

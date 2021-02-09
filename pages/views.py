from listings.models import Listings
from django.shortcuts import render
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listings.objects.all()
    context = {
        'title': 'Homepage',
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': listings
    }
    return render(request, "pages/home/index.html", context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, "pages/about/about.html", context)

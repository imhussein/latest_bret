from listings.search import apply_search
from listings.models import Listings
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from listings.choices import bedroom_choices, price_choices, state_choices


def listings(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, per_page=2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'title': 'Listings',
        'listings': paged_listings,
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context = {
        'title': 'Listing',
        'listing': listing,
    }
    return render(request, "listings/listing.html", context)


def search(request):
    keywords = request.GET.get('keywords')
    state = request.GET.get('state')
    price = request.GET.get('price')
    bedrooms = request.GET.get('bedrooms')
    city = request.GET.get('city')
    search_fields = {
        "description__icontains": keywords,
        "state": state,
        "price__gte": price,
        "bedrooms__lte": bedrooms,
        "city__iexact": city
    }
    queryset_listings = None
    for key, value in search_fields.items():
        if not (value is None or value == ''):
            current = {}
            current[key] = value
            queryset_listings = apply_search(
                Listings, request, 'keywords', **current)
    context = {
        'title': 'Homepage',
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_listings,
        'values': request.GET
    }
    return render(request, "listings/search.html", context)

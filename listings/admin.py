from listings.models import Listings
from django.contrib import admin


class AdminListing(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'address',
                    'list_date', 'city', 'state', 'zipcode', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ("id", "title", "city")
    list_per_page = 25
    list_filter = ("id", "title", "list_date")


admin.site.register(Listings, AdminListing)

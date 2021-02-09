from contacts.models import Contact
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "message", "user_id")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)

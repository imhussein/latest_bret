from realtors.models import Realtor
from django.contrib import admin


class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_mvp")
    list_display_links = ("id", "name")
    list_filter = ("id", "name")
    list_editable = ("is_mvp",)
    search_fields = ("id", "name")
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)

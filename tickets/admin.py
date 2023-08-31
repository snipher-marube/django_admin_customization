from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter
from import_export.admin import ImportExportActionModelAdmin
from djangoql.admin import DjangoQLSearchMixin

from tickets.models import Venue, ConcertCategory, Concert, Ticket
from tickets.forms import TicketAdminForm

class SoldOutFilter(SimpleListFilter):
    title = "sold out"
    parameter_name = "sold_out"

    def lookups(self, request, model_admin):
        return(
            ("yes", "Yes"),
            ("no", "No"),
        )
    
    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(tickets_left=0)
        elif self.value() == "no":
            return queryset.exclude(tickets_left=0)
        else:
            return queryset

class ConcertInline(admin.TabularInline):
    model = Concert
    fields = ["name", "starts_at", "price", "tickets_left"]

    # optional: make the inline read-only
    readonly_fields = ["name", "starts_at", "price", "tickets_left"]
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True

class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "capacity"]
    inlines = [ConcertInline]


class ConcertCategoryAdmin(admin.ModelAdmin):
    pass


class ConcertAdmin(admin.ModelAdmin):
    list_display = ["name", "venue", "starts_at", "tickets_left", "display_sold_out", "display_price", "display_venue"]
    list_select_related = ["venue"] # this is a list of foreign keys that will be fetched in one query to avoid N+1 problem
    list_filter = ["venue", SoldOutFilter]
    search_fields = ["name", "venue__name", "venue__address"]

    def display_sold_out(self, obj):
        return obj.tickets_left == 0
    
    display_sold_out.short_description = "Sold out"
    display_sold_out.boolean = True

    def display_price(self, obj):
        return f"${obj.price:.2f}"
    
    display_price.short_description = "Price"
    display_price.admin_order_field = "price"

    def display_venue(self, obj):
        link = reverse("admin:tickets_venue_change", args=[obj.venue.id])
        return format_html('<a href="{}">{}</a>', link, obj.venue)
    
    display_venue.short_description = "Venue"

@admin.action(description="Activate selected tickets")
def activate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Deactivate selected tickets")
def deactivate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=False)

class TicketAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin):
    list_display = ["concert", "customer_full_name", "payment_method", "paid_at", 'is_active']
    list_select_related = ["concert", "concert__venue"] # this is a list of foreign keys that will be fetched in one query to avoid N+1 problem
    list_filter = ["concert__venue", "payment_method", "is_active"]
    actions = [activate_tickets, deactivate_tickets]
    form = TicketAdminForm

admin.site.register(Venue, VenueAdmin)
admin.site.register(ConcertCategory, ConcertCategoryAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Ticket, TicketAdmin)

from django.contrib import admin

from insurance.models import Customer, Policy, PolicyState


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "dob")
    search_fields = ("first_name", "last_name", "dob")
    list_filter = ("dob",)


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ("customer", "type", "premium", "cover", "state")
    search_fields = (
        "customer__first_name",
        "customer__last_name",
        "customer__dob",
        "type",
    )
    list_filter = ("state", "type")


@admin.register(PolicyState)
class PolicyStateAdmin(admin.ModelAdmin):
    list_display = ("policy", "state", "timestamp")

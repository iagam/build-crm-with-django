from django.contrib import admin
from .models import User, Agent, Lead


class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_staff")


class LeadAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "agent")


admin.site.register(User, UserAdmin)
admin.site.register(Agent)
admin.site.register(Lead, LeadAdmin)

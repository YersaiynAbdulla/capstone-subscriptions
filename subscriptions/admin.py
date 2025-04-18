from django.contrib import admin
from .models import User, SubscriptionPlan, UserSubscription, SubscriptionAnalytics, Notification
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    model = User
    list_display = ('email', 'full_name', 'role', 'is_active')
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'role')}),
    )
    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'role')}),
    )

admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(SubscriptionAnalytics)
admin.site.register(Notification)

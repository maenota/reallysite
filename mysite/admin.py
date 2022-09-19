from operator import indexOf
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.forms import UserCreationForm
from mysite.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields': ('email','password',)}),
        (None, {'fields':('is_active','is_admin',)})       
    ]

    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal =()

    add_fieldsets = [
        (None, {'fields': ('email','password'),}),
    ]
    add_form = UserCreationForm

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)

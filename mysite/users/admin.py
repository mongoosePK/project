from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Profile
# Register your models here.

# define an inline admin descriptor for profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# define a new user admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
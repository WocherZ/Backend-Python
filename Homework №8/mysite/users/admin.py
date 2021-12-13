from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    list_filter = ('first_name',)


admin.site.register(User, UserAdmin)

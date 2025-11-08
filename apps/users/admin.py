from django.contrib import admin
from .models import CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined')
    list_display_links = ('username',)
    ordering = ('date_joined', 'last_login',)
    readonly_fields = ('last_login', 'date_joined',)
    exclude = ()

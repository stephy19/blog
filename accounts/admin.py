from django.contrib import admin
from accounts.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'date_of_birth', 'photo']
    list_filter = ['user', 'bio', 'date_of_birth', 'photo']
    search_fields = ['user', 'bio', 'date_of_birth', 'photo']
    
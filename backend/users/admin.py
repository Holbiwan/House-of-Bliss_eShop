from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date', 'gender', 'online_status')
    list_filter = ('gender', 'online_status')
    search_fields = ('user__username', 'phone')

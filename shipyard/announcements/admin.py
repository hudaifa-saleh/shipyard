from django.contrib import admin

from .models import Announcements


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'expires_at', )
    date_hierarchy = 'expires_at'

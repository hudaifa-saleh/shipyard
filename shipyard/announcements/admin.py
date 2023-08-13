from django.contrib import admin

from .models import Announcements


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'expired_at', )
    date_hierarchy = 'expired_at'

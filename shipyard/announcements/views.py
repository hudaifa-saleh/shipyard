from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from shipyard.announcements.models import Announcements


class AnnouncementListView(ListView):
    def get_queryset(self):
        return Announcements.objects.filter(expires_at__gte=timezone.now())


class AnnouncementFeedView(Feed):
    """Generate an RSS feed that Mailchimp (or any feed reader) can import."""
    title = "Shipyard Announcements"
    link = "/announcements/"
    description = "Shipyard Announcements."

    def items(self):
        return Announcements.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("announcements:list") + f"announcements-{item.id}"

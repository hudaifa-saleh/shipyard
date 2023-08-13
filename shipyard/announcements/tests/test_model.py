import datetime

from django.utils import timezone
from test_plus.tests import TestCase

from shipyard.announcements.models import Announcements
from shipyard.announcements.tests.factories import AnnouncementFactory


class TestAnnouncements(TestCase):
    def test_factory(self):
        announcements = AnnouncementFactory()

        assert announcements.title
        assert announcements.description
        assert announcements.expires_at

    def test_str(self):
        announcements = AnnouncementFactory()

        assert str(announcements) == announcements.title

    def test_ordering(self):
        now = timezone.now()
        original_announcements = AnnouncementFactory(expires_at=now + datetime.timedelta(days=7))
        newest_announcements = AnnouncementFactory(expires_at=now + datetime.timedelta(days=14))
        newer_announcements = AnnouncementFactory(expires_at=now + datetime.timedelta(days=10))
        announcements = Announcements.objects.all()

        assert list(announcements) == [newest_announcements, newer_announcements, original_announcements]

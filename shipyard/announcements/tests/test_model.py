from test_plus.tests import TestCase
from shipyard.announcements.tests.factories import AnnouncementFactory


class TestAnnouncements(TestCase):
    def test_factory(self):
        announcements = AnnouncementFactory()

        assert announcements.title
        assert announcements.description
        assert announcements.expired_at

    def test_str(self):
        announcements = AnnouncementFactory()

        assert str(announcements) == announcements.title

from test_plus.tests import TestCase

from shipyard.announcements.tests.factories import AnnouncementFactory


class TestAnnouncementFeed(TestCase):
    def setUp(self):
        announcement = AnnouncementFactory()
        response = self.get('announcements:feed')
        self.assertResponseContains(announcement.title, response, html=False)
        self.assertResponseContains(announcement.description, response, html=False)

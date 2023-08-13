import factory


class AnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'announcements.Announcements'

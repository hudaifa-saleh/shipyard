import datetime

import factory
from django.utils import timezone


class AnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'announcements.Announcements'

    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    expired_at = factory.LazyFunction(lambda: timezone.now() + datetime.timedelta(days=14))

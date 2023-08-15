from test_plus.tests import TestCase

from shipyard.service.models import ServiceCategory
from shipyard.service.tests.factories import ServiceCategoryFactory, ServiceFactory


class TestIndex(TestCase):
    def test_ok(self):
        self.get_check_200('service:index')

    def test_has_categories(self):
        """This service categories are rendered on the page."""
        category = ServiceCategoryFactory()
        response = self.get('service:index')
        self.assertContains(response, category.name)

    def get_check_200(self, param, slug):
        pass


class TestServiceCategoryDetailView(TestCase):
    def test_ok(self):
        category = ServiceCategoryFactory()
        self.get_check_200('service:service-category-detail', slug=category.slug)

    def test_has_services(self):
        category = ServiceCategoryFactory()
        service = ServiceFactory(category=category)
        ServiceFactory()
        assert ServiceCategory.objects.count() == 2
        self.get('service:service-category-detail', slug=category.slug)
        services = self.get_context('services')
        assert list(services) == [service]

    def get_check_200(self, param, slug):
        pass


class TestServiceDetailView(TestCase):
    def test_ok(self):
        service = ServiceFactory()
        self.get_check_200('service:service-detail', pk=service.pk)

    def get_check_200(self, param, pk):
        pass

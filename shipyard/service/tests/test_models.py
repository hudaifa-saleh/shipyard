from test_plus.tests import TestCase

from shipyard.service.tests.factories import ServiceCategoryFactory, ServiceFactory


class TestServiceFactory(TestCase):
    def test_factory(self):
        category = ServiceCategoryFactory()
        assert category.name
        assert category.slug
        assert category.description
        # assert category.icon
        assert category.color

    def test_str(self):
        category = ServiceCategoryFactory()
        assert str(category) == category.name


class TestService(TestCase):
    def test_factory(self):
        service = ServiceFactory()
        assert service.name
        assert service.organization_name
        assert service.description
        assert service.website
        assert service.street_address
        assert service.city
        assert service.state
        assert service.zip_code
        assert service.latitude
        assert service.longitude
        assert service.operation_hours
        assert service.category
        assert service.phone_number
        assert service.email

    def test_str(self):
        category = ServiceFactory()
        assert str(category) == category.name

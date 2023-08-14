import factory


class ServiceCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'service.ServiceCategory'


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'service.Service'

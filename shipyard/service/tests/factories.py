import factory


class ServiceCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'service.ServiceCategory'

    name = factory.Sequence(lambda n: f"Service Category {n}")
    slug = factory.Sequence(lambda n: f"service-category-{n}")
    description = factory.Faker("paragraph")


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'service.Service'

    name = factory.Sequence(lambda n: f"Service {n}")
    organization_name = factory.Faker("company")
    description = factory.Faker("paragraph")
    website = factory.Faker("url")
    street_address = factory.Faker("street_address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zip_code = factory.Faker("zip_code")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    location = factory.Faker("location")
    operation_hours = factory.Faker("operation_hours")
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("email")
    category = factory.SubFactory(ServiceCategoryFactory)

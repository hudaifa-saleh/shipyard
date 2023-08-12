from django.db import models


class ServiceCategory(models.Model):
    """Each service must belong to a category for easy browsing."""
    name = models.CharField(max_length=255)
    slug = models.SlugField(help_text="This is the unique name that will display in the URL.")

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    """A community service that is available to homepage citizens."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    operation_hours = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=35)
    email = models.EmailField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name

from django.db import models


class ServiceCategory(models.Model):
    """Each service must belong to a category for easy browsing."""
    name = models.CharField(max_length=255, default="")
    slug = models.SlugField(help_text="This is the unique name that will display in the URL.")
    description = models.TextField(default="")
    icon = models.CharField(max_length=128,
                            help_text="Upload a 300x300 px to the 'static' directory. Add file path here", default="")
    COLOR_CHOICES = (
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
        ('pink', 'Pink'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
    )
    color = models.CharField(max_length=8, choices=COLOR_CHOICES, default='gray')

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    """A community service that is available to homepage citizens."""
    name = models.CharField(max_length=255, default="")
    organization_name = models.CharField(max_length=128, default="")
    description = models.TextField(default="")
    website = models.URLField(blank=True, default="")
    street_address = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=128, default="")
    state = models.CharField(max_length=128, default="")
    zip_code = models.CharField(max_length=128, default="")
    latitude = models.CharField(max_length=18, blank=True, default="")
    longitude = models.CharField(max_length=18, blank=True, default="")

    location = models.CharField(max_length=255, default="")
    operation_hours = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=35, default="")
    email = models.EmailField(default="")
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name

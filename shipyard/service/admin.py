from django.contrib import admin

from shipyard.service.models import ServiceCategory, Service

admin.site.register(ServiceCategory)
admin.site.register(Service)

from django.views.generic import ListView, DetailView

from shipyard.service.models import ServiceCategory, Service


class IndexView(ListView):
    queryset = ServiceCategory.objects.all()
    template_name = 'service/index.html'


class ServiceCategoryDetailView(DetailView):
    model = ServiceCategory

    # template_name ='service/servicecategory_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceCategoryDetailView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(category=self.object)
        return context


class ServiceDetailView(DetailView):
    model = Service

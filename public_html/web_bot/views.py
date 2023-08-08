from django.views.generic import TemplateView, ListView
from .models import CarBrand, Car


class Index(ListView):
    template_name = 'web_bot/index.html'
    context_object_name = 'brands'
    model = CarBrand


class CarsView(ListView):
    template_name = 'web_bot/cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(brand=CarBrand.objects.get(pk=self.kwargs.get('pk')))

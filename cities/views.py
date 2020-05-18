from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import City
from .forms import CityForm


def home(request):
    """функция отображения списка городов"""
    print(request.POST)
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'object_list': cities})


class CityDetailView(DetailView):
    """ Пишем класс отображения"""
    queryset = City.objects.all()
    context_object_name = "object"  # ЕСЛИ ИМЯ НЕ ЗАДАВАТЬ ОНО БУДЕТ OBJECT ПО УМОЛ
    template_name = 'cities/detail.html'


class CityCreateViews(CreateView):
    model = City
    template_name = 'cities/create.html'
    form_class = CityForm
    success_url = reverse_lazy("city:home")


class CityUpdateViews(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')


class CityDeleteViews(DetailView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')

from django.shortcuts import render
from .models import City
# Create your views here.


def home(request):
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'object_list': cities})



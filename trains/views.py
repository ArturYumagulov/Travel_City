from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Train


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 5)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'object_list': trains})

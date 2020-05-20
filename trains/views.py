from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Train
from .forms import TrainForm


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 5)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'object_list': trains})


class TrainCreateViews(CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:add')

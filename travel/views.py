from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    name = "Bob"
    context = {'company_name': 'Travelling', "name": name}
    return render(request, 'home.html', context)

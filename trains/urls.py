from django.urls import path
from .views import home, TrainCreateViews

urlpatterns = [
    path('add/', TrainCreateViews.as_view(), name='add'),
    path('', home, name="home")
]
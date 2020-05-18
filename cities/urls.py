from django.urls import path
from .views import home, CityDetailView, CityCreateViews, CityUpdateViews, CityDeleteViews


urlpatterns = [
    path('delete/<int:pk>/', CityDeleteViews.as_view(), name='delete'),
    path('update/<int:pk>/', CityUpdateViews.as_view(), name='update'),
    path('add/', CityCreateViews.as_view(), name='add'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('', home, name='home'),
]

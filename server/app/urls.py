from django.urls import path

from . import views

app_name = 'showroom'
urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.carlist, name='car_list'),
    path('cars/<int:car_id>', views.carDetail, name='car_detail')
]
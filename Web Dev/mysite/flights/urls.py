from django.urls import path

from . import views

app_name= 'flights'
urlpatterns = [
   # ex: /flights/
    path('', views.index, name='index'),
    # ex: /flights/1
    path("<int:flight_id>", views.flight, name='flight'),

    path("<int:flight_id>/book", views.book, name="book"),
]
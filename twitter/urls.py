from django.urls import path

from . import views

app_name='twitter'
urlpatterns = [
    path('', views.index, name='index'),
]

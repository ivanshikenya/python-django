from django.urls import path
from . import views
from .views import Second

urlpatterns = [
    path('first', views.first),
    path('second', Second.as_view())
]

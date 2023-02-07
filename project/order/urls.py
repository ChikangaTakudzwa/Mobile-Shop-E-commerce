from django.urls import path
from .views import start_order

urlpatterns = [
    path('start-order/', start_order, name="start_order"),
]
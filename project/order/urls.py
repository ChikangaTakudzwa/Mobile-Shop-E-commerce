from django.urls import path
from .views import start_order
from cart.views import success

urlpatterns = [
    path('start-order/', start_order, name="start_order"),
    # path('success/', success, name="success"),
]
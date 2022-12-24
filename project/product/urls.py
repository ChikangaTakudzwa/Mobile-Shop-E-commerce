from django.urls import path
from app.views import shop
from . import views

urlpatterns = [
    path('', views.product, name="product"),
    # path('product/<slug:slug>/', views.product, name="item")

]

from django.urls import path
from app.views import index, shop, my_account

urlpatterns = [
    path('', index, name="home"),
    path('shop/', shop, name="shop"),
    # path('myaccount/', my_account, name="myaccount"),
    # path('shop/<id:id>/', views.product, name="product"),
]

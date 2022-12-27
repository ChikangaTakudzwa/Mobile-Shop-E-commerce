from django.urls import path
from django.contrib.auth import views
from app.views import index, shop, signup
from product.views import product

urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('shop/', shop, name="shop"),
    path('shop/<slug:model>/', product, name="product"),
]

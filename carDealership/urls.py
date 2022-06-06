
from django.contrib import admin
from django.urls import path
from user import views as views_user
from car import views as views_car
from dealer import views as views_dealer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views_user.user),
    path('login/', views_user.login),
    path('logout/', views_user.logout),
    path('registration/', views_user.registration),
    path('car/', views_car.car),
    path('car/create/<int:product_id>/', views_car.car_create),
    path('car/<int:car_id>/', views_car.car_id),
    path('car/info/<int:car_info_id>/', views_car.car_info),
    path('dealer/', views_dealer.dealer),
    path('dealer/<int:dealer_id>/', views_dealer.dealer_id),
    path('dealer/name', views_dealer.dealer_name)
]

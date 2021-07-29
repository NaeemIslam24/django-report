from django.urls import path
from . import views
app_name = 'sales'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sale_list/', views.sale_list_view, name='sale_list'),
    path('sale_detail/<int:pk>/', views.sale_detail_view, name='sale_detail'),



]

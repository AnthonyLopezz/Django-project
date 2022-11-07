from django.urls import path
from django.contrib.auth.views import login_required, logout_then_login
from . import views


urlpatterns = [
    path('dashboard/', views.admon, name='admon'),

    # Products
    path('dashboard/add/', views.add_Product, name='add'),
    path('dashboard/list/', views.list, name='list'),
    path('dashboard/delete/<int:product_id>', views.delete, name='delete'),
    path('dashboard/modify/<int:product_id>/', views.modify_product, name='modify'),

    # Users
    path('dashboard/list_users/', views.list_users, name='listUser'),
]

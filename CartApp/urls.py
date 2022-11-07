from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name='Add'),
    path('delete/<int:product_id>/', views.delete_product, name='Delete'),
    path('rest/<int:product_id>/', views.rest_product, name='Rest'),
    path('empty/', views.empty_car, name='Empty'),
]
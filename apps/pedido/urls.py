from django.urls import path
from . import views

urlpatterns = [
    path('new-pedido/', views.create_pedido, name="new-pedido"),
    path('edit-pedido/<int:pk>', views.create_pedido, name="edit-pedido"),
    path('list-pedido/', views.list_pedidos, name="list-pedido"),
]
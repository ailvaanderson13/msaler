from django.urls import path
from . import views

urlpatterns = [
    path('new-produto/', views.create_update_item, name="new-produto"),
    path('edit-produto/<int:pk>', views.create_update_item, name="edit-produto"),
    path('list-produto/', views.list_item, name="list-produto")
]

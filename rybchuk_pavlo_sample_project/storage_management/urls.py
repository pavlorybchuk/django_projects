from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("add/", views.ProductCreateView.as_view(), name="product_add"),
    path("edit/<pk>/", views.ProductUpdateView.as_view(), name="product_edit"),
    path("delete/<pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("inventory/", views.InventoryListView.as_view(), name="inventory_list"),
    path("inventory/replenish/<int:count>", views.replenish_inventory, name="replenish_inventory"),
    path("product/replenish/<int:count>", views.replenish, name="replenish_products"),
    path("inventory/edit/", views.edit_inventory_record, name="inventory_edit"),
    path("inventory/add/", views.create_inventory_record, name="inventory_add"),
    path("inventory/delete/", views.delete_inventory_record, name="inventory_delete"),
    path("inventory/alerts/", views.InventoryListView.as_view(), name="alerts_list"),
]
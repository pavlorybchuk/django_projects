import uuid
from django.db import models as m


class BaseTrackedModel(m.Model):
    uuid = m.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Category(BaseTrackedModel):
    name = m.CharField(max_length=60)
    parent = m.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=m.SET_NULL,
        related_name="children"
    )

    def __str__(self):
        return self.name

    def full_path(self):
        names = [self.name]
        parent = self.parent

        while parent is not None:
            names.append(parent.name)
            parent = parent.parent

        return " → ".join(names[::-1])
    
class Warehouse(BaseTrackedModel):
    title = m.CharField(max_length=100)
    address = m.CharField(max_length=255)
    manager_name = m.CharField(max_length=50)

class Product(BaseTrackedModel):
    name = m.CharField(max_length=50)
    age_category = m.IntegerField()
    material = m.CharField(max_length=100)
    brand = m.CharField(max_length=50)
    price = m.IntegerField()
    category = m.ForeignKey(Category, on_delete=m.PROTECT)
    warehouses = m.ManyToManyField(
        Warehouse,
        through="InventoryRecord"
    )

    def __str__(self):
        return self.name + ' - ' + self.brand
    
    class Meta:
        unique_together = ("name", "category")



class InventoryRecord(BaseTrackedModel):
    product = m.ForeignKey(
        Product,
        on_delete=m.CASCADE,
        related_name="inventory_records"
    )
    warehouse = m.ForeignKey(
        Warehouse,
        on_delete=m.CASCADE,
        related_name="inventory_records"
    )

    quantity = m.IntegerField(default=0)
    last_restock = m.DateTimeField(null=True, blank=True)
    min_required = m.IntegerField(default=0)

    class Meta:
        unique_together = ("product", "warehouse")

    def is_below_minimum(self):
        return self.quantity < self.min_required

    def __str__(self):
        return f"{self.product.name} @ {self.warehouse.name}: {self.quantity}"
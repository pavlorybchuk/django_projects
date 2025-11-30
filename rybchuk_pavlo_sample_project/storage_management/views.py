from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
import random
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Product, Warehouse, InventoryRecord, Category
from django.db.models import Count, F

def replenish(request, count):
    toy_names = ["Плюшевий ведмедик", "Конструктор LEGO", "Машинка HotWheels", "Лялька Barbie", "М’яч", "Гелікоптер", "Настільна гра UNO", "Кубик Рубіка"]
    brands = ["LEGO", "Mattel", "Hasbro", "Fisher-Price", "Chicco", "Playmobil"]
    materials = ["Пластик", "Тканина", "Гума", "Дерево"]
    ages = [3, 5, 7, 10, 12]
    categories = Category.objects.annotate(child_count=Count("children")).filter(child_count=0)

    for _ in range(count):
        Product.objects.get_or_create(
            category= random.choice(categories),
            name=random.choice(toy_names),
            defaults={
                "brand": random.choice(brands),
                "material": random.choice(materials),
                "age_category": random.choice(ages),
                "price": round(random.uniform(150, 1200), 2),
            }
        )
    messages.success(request, "Продукти були успішно створені!")
    return redirect("product_list")

def replenish_inventory(request, count):
    products = list(Product.objects.all())
    warehouses = list(Warehouse.objects.all())
    print(list(Warehouse.objects.all()))

    if not products or not warehouses:
        messages.error(request, "Немає продуктів або складів!")
        return redirect("inventory_list")

    for _ in range(count):
        p = random.choice(products)
        w = random.choice(warehouses)

        record, created = InventoryRecord.objects.get_or_create(
            product=p,
            warehouse=w,
            defaults={
                "quantity": random.randint(1, 50),
                "last_restock": timezone.now(),
                "min_required": random.randint(2, 10),
            }
        )

        if not created:
            record.quantity = random.randint(1, 50)
            record.last_restock = timezone.now()
            record.min_required = random.randint(2, 10)
            record.save()

    messages.success(request, "Інвентаризація пройшла успішно!")
    return redirect("inventory_list")

@require_POST
def create_inventory_record(request):
    product = request.POST.get("product")
    warehouse = request.POST.get("warehouse")
    quantity = request.POST.get("quantity")
    min_required = request.POST.get("min_required")
    try:
        InventoryRecord.objects.create(
            product=product,
            warehouse=warehouse,
            quantity=quantity,
            last_restock=timezone.now(),
            min_required=min_required,
        )
    except Exception:
        messages.error(request, "Неправильні дані або такий запис уже існує!")
        return redirect("inventory_list")
    messages.success(request, "Новий запис створено успішно!")
    return redirect("inventory_list")

@require_POST
def edit_inventory_record(request):
    record_id = request.POST.get("rec_id")
    quantity = request.POST.get("quantity")
    min_required = request.POST.get("min_required")
    last_restock = request.POST.get("last_restock")
    record = get_object_or_404(InventoryRecord, pk=record_id)
    if quantity:
        try:
            record.quantity = int(quantity)
        except ValueError:
            messages.error(request, "Неправильне значення quantity!")
            return redirect("inventory_list")
    if min_required:
        try:
            record.min_required = int(min_required)
        except ValueError:
            messages.error(request, "Неправильне значення min_required!")
            return redirect("inventory_list")
    if last_restock:
        try:
            record.last_restock = timezone.datetime.fromisoformat(last_restock)
        except ValueError:
            messages.error(request, "Неправильний формат дати!")
            return redirect("inventory_list")
    record.save()

    messages.success(request, "Запис було успішно змінено!")
    return redirect("inventory_list")

@require_POST
def delete_inventory_record(request):
    record_id = request.POST.get("del_rec_id")

    record = get_object_or_404(InventoryRecord, pk=record_id)
    record.delete()

    messages.warning(request, "Запис було видалено!")
    return redirect("inventory_list")

class InventoryListView(ListView):
    model = InventoryRecord
    template_name = "storage_management/inventory.html"
    context_object_name = "records"

class InventoryAlertsView(ListView):
    model = InventoryRecord
    template_name = "storage_management/inventory_alerts.html"
    context_object_name = "alerts"

    def get_queryset(self):
        return InventoryRecord.objects.filter(quantity__lt=F("min_required"))

class ProductListView(ListView):
    model = Product
    template_name = "storage_management/index.html"
    context_object_name = "products"

class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "age_category", "material", "brand", "price"]
    success_url = reverse_lazy("product_list")
    
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'POST':
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "age_category", "material", "brand", "price"]
    success_url = reverse_lazy("product_list")
    
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'POST':
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product_list")
    
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'POST':
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
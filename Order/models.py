from django.db import models
from products.models import CreateatModel
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(CreateatModel):
    STATUS = Choices(
        "In progress",
        "Canceled",
        "Finished",
    )
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField('products.Product', through = 'OrderItem')
    order_status = StatusField()

    class Meta:
        ordering = ['-created']
        db_table = 'order'

    def __str__(self):
        return f"Заказ № {self.id} от {self.created.strftime('%d-%m-%Y %H:%M')}"

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete = models.CASCADE, related_name = 'items'
    )
    product = models.ForeignKey(
        'products.Product', on_delete = models.RESTRICT, related_name = 'order_items'
    )
    quantity = models.PositiveIntegerField(
        default = 1
    )

    class Meta:
        db_table = 'order_items'

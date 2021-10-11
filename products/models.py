from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from model_utils.fields import StatusField

User = get_user_model()


class CreateatModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        abstract = True


class Product(CreateatModel):
    STATUS = Choices('Available', 'Not existed')
    title = models.CharField(max_length=50, unique=True )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products_image', null=True, blank=True)
    status = StatusField


from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from model_utils.fields import StatusField
<<<<<<< HEAD
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like
=======
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a

User = get_user_model()


<<<<<<< HEAD
class CreatedatModel(models.Model):
=======
class CreateatModel(models.Model):
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
    created = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        abstract = True


<<<<<<< HEAD
class Product(CreatedatModel):
=======
class Product(CreateatModel):
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
    STATUS = Choices('Available', 'Not existed')
    title = models.CharField(max_length=50, unique=True )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specification = models.TextField()
    image = models.ImageField(upload_to='products_image', null=True, blank=True)
    status = StatusField
<<<<<<< HEAD
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()


class ProductReview(CreatedatModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
=======

class ProductReview(CreateatModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
    rating = models.PositiveBigIntegerField(default=1)
from rest_framework import viewsets
<<<<<<< HEAD
from likes.mixins import LikedMixin
=======
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
<<<<<<< HEAD
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class ProductViewSet(LikedMixin,viewsets.ModelViewSet):
=======
from rest_framework import permissions


class ProductViewSet(viewsets.ModelViewSet):
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter
    ]
    filter_fields = ['price', 'title']
    search_fields = ['title', 'id', 'specification']
<<<<<<< HEAD
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []
=======
    

    # def get_permissions(self):
    #     if self.
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
<<<<<<< HEAD
    permission_classes = [IsAuthenticatedOrReadOnly, ]
=======
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a



    def get_serializer_context(self):

        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):

        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

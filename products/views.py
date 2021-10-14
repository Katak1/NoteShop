from rest_framework import viewsets
from likes.mixins import LikedMixin
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

class ProductViewSet(LikedMixin,viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter
    ]
    filter_fields = ['price', 'title']
    search_fields = ['title', 'id', 'specification']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


    def get_serializer_context(self):

        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):

        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

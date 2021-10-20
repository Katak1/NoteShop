from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework import filters as rest_filter
from rest_framework import permissions
from django_filters import rest_framework as filters



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filter.SearchFilter,
    ]
    filterset_fields = ['order_status']
    search_fields = ['id']
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):

        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):

        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

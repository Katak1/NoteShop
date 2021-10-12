from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):

    product_title = serializers.SerializerMethodField("get_product_title")
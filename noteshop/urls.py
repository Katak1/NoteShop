from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from products.views import ProductViewSet, ProductReviewViewSet
from django.conf import settings
from django.conf.urls.static import static 
from Order.views import OrderViewSet

=======
from products.views import ProductViewSet
from django.conf import settings
from django.conf.urls.static import static 
>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a


router = DefaultRouter()
router.register('products', ProductViewSet)
<<<<<<< HEAD
router.register('reviews', ProductReviewViewSet)
router.register('order', OrderViewSet)
"""
URL для лайков указанны в .likes/urls.py
"""
=======

>>>>>>> e6c35691a81bc41017155fd9eaac78025b720a2a
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

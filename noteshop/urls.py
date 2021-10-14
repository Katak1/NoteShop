from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, ProductReviewViewSet
from django.conf import settings
from django.conf.urls.static import static 
from Order.views import OrderViewSet
from .yasg import urlpatterns as doc_urls




router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('reviews', ProductReviewViewSet)
router.register('order', OrderViewSet)
# router.register('cart', CartViewSet)

"""
URL для лайков указанны в .likes/urls.py
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/', include('cart.urls')),

]

urlpatterns += doc_urls

if settings.DEBUG:
	static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

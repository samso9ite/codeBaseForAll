from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'giftcard', GiftCardViewSet)
router.register(r'crypto', CryptoViewSet)
router.register(r'testimonial', TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
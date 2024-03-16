from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, PolicyViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'quote', PolicyViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

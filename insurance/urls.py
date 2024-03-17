from django.urls import path, include
from rest_framework.routers import DefaultRouter
from insurance.views import CustomerViewSet, PolicyViewSet

urlpatterns = [
    path('api/v1/create_customer/', CustomerViewSet.as_view(), name='customer-create'),
    path('api/v1/quote/', PolicyViewSet.as_view(), name="create-quote")
]
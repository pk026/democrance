from rest_framework import generics
from .models import Customer, Policy
from .serializers import CustomerSerializer, PolicySerializer


class CustomerViewSet(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PolicyViewSet(generics.CreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

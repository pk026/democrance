from rest_framework import serializers
from insurance.models import Customer, Policy, PolicyState


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'


class PolicyStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyState
        fields = '__all__'
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from insurance.models import Customer, Policy, PolicyState
from insurance.serializers import (
    CustomerSerializer,
    PolicySerializer,
    PolicyStateSerializer,
)


class CustomerViewSet(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned policies to a given customer,
        by filtering against a `customer` query parameter in the URL.

        Another way of filtering policies is fetch customer_id of logged in user
        return only his/her policies,
        When we implement authentication we can check if looged user is staff
        then we get the customer_id from query param, else we fatch from db for logged in user.
        """
        queryset = Policy.objects.all()
        customer_id = self.request.query_params.get("customer_id")
        if customer_id is not None:
            queryset = queryset.filter(customer_id=customer_id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            policy = serializer.save()
            # Automatically log the 'quoted' state
            PolicyState.objects.create(policy=policy, state=policy.state)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        policy = self.get_object()
        previous_state = policy.state
        kwargs["partial"] = True
        response = self.update(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            policy.refresh_from_db()
            new_state = policy.state

            # Check if the state has changed
            if previous_state != new_state:
                # Record the state change
                PolicyState.objects.create(policy=policy, state=new_state)

        return response


class PolicyHistoryView(generics.ListAPIView):
    serializer_class = PolicyStateSerializer

    def get_queryset(self):
        """
        This view should return a list of all the policy states
        for the policy as determined by the policy_id portion of the URL.
        """
        policy_id = self.kwargs["policy_id"]
        return PolicyState.objects.filter(policy_id=policy_id).order_by("-timestamp")

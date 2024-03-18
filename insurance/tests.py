import pytest
from rest_framework.test import APIClient

from .models import Customer, Policy


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_customer(db):
    def make_customer(**kwargs):
        return Customer.objects.create(**kwargs)

    return make_customer


@pytest.fixture
def create_policy(db, create_customer):
    customer = create_customer(name="Test Customer", other_fields="...")

    def make_policy(**kwargs):
        defaults = {"customer": customer, "policy_details": "Sample Policy"}
        defaults.update(kwargs)
        return Policy.objects.create(**defaults)

    return make_policy


@pytest.mark.django_db
def test_customer_list(api_client, create_customer):
    customer = create_customer(name="John Doe")
    response = api_client.get("/customers/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "John Doe"


@pytest.mark.django_db
def test_policy_list(api_client, create_policy):
    policy = create_policy(policy_details="Test Policy")
    response = api_client.get("/policies/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["policy_details"] == "Test Policy"

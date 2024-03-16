from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Customer, Policy


class CustomerAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_customer_url = reverse('create_customer')  # Adjust based on your url name

    def test_create_customer_success(self):
        """Test the API can successfully create a customer."""
        data = {'first_name': 'John', 'last_name': 'Doe', 'dob': '1990-01-01'}
        response = self.client.post(self.create_customer_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'John')

    def test_create_customer_invalid_data(self):
        """Test the API with invalid customer data."""
        data = {}  # Empty data should not be valid
        response = self.client.post(self.create_customer_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class QuoteAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.quote_url = reverse('create_quote')  # Adjust based on your url name
        # Creating a test customer to associate with a policy
        self.test_customer = Customer.objects.create(
            first_name="Jane",
            last_name="Doe",
            dob="1991-02-01"
        )

    def test_create_quote_success(self):
        """Test the API can successfully create a quote."""
        data = {
            'customer_id': self.test_customer.id,
            'policy': {
                'type': 'personal-accident',
                'premium': 200,
                'cover': 200000,
                'state': 'quoted'
            }
        }
        response = self.client.post(self.quote_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Policy.objects.count(), 1)
        self.assertEqual(Policy.objects.get().state, 'quoted')

    def test_create_quote_no_customer(self):
        """Test the API with a non-existent customer."""
        data = {
            'customer_id': 999,  # Assuming this customer does not exist
            'policy': {
                'type': 'personal-accident',
                'premium': 200,
                'cover': 200000,
                'state': 'quoted'
            }
        }
        response = self.client.post(self.quote_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

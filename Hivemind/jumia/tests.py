from django.test import TestCase,Client,  SimpleTestCase
from .models import Categories, Product, Type
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from jumia.views import *

class ModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.category = Categories.objects.create(category_name='Test Category')
        self.product = Product.objects.create(categories=self.category, name='Test Product')
        self.type = Type.objects.create(
            business=None,
            product=self.product,
            name='Test Type',
            description='Test Description',
            price=10.0,
            is_available=True,
            product_by=User.objects.create_user(username='test_user', password='password')
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')


class ViewTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.category = Categories.objects.create(category_name='Test Category')
        self.product = Product.objects.create(categories=self.category, name='Test Product')
        self.type = Type.objects.create(
            business=None,
            product=self.product,
            name='Test Type',
            description='Test Description',
            price=10.0,
            is_available=True,
            product_by=self.user
        )

    def test_items_view(self):
        response = self.client.get(reverse('items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jumia/item.html')

    def test_detail_view(self):
        response = self.client.get(reverse('detail', args=[self.type.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jumia/detail.html')

    def test_cart_view(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jumia/cart.html')

    def test_checkout_view(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jumia/checkout.html')

class UrlsTestCase(SimpleTestCase):
    def test_items_url_resolves(self):
        url = reverse('items')
        self.assertEqual(resolve(url).func, items)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=[1])  # Assuming an ID of 1 for testing purposes
        self.assertEqual(resolve(url).func, detail)

    def test_cart_url_resolves(self):
        url = reverse('cart')
        self.assertEqual(resolve(url).func, cart)

    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)
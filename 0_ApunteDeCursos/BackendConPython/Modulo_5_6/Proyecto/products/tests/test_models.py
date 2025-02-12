from django.test import TestCase
from django.utils import timezone
from django_dynamic_fixture import G
from unicodedata import category

from ..models import Products, Brand

class ProductModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.product = Products.objects.create(
            name='Test Product',
            price=1000,
            sku='SKU123',
            category='Test Category',
            brand=self.brand,
            discount=15,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def test_product_str_method(self):
        expected_str = f'{self.product.name} | {self.product.brand.name}'
        self.assertEqual(str(self.product), expected_str)

    def test_product_attributes(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 1000)
        self.assertEqual(self.product.sku, 'SKU123')
        self.assertEqual(self.product.category, 'Test Category')
        self.assertEqual(self.product.brand, self.brand)
        self.assertEqual(self.product.discount, 15)
        self.assertIsNotNone(self.product.created_at)
        self.assertIsNotNone(self.product.updated_at)


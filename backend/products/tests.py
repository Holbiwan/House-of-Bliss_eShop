from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Lavender Oil",
            category="essential_oil",
            price=19.99,
            stock=100,
            features="Relaxing fragrance",
            contents="100% pure lavender oil"
        )

    def test_product_str(self):
        """Products are correctly identified by their name and category."""
        lavender_oil = Product.objects.get(name="Lavender Oil")
        self.assertEqual(str(lavender_oil), "Essential Oil - Lavender Oil")

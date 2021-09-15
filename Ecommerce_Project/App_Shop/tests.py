from django.test import TestCase, Client
from django.urls import reverse
from App_Shop.models import Category, Product

# Create your tests here.

#There isn't any method in my view.py file though I have 2 classes for initializing fields. As there is no method, I am not writing any test for views.py file

#Testing models classes
class CategoryrTest(TestCase):
    def test__str__(self):
        category=Category(title="Shirt")
        self.assertEqual(category.__str__(),"Shirt")

class ProductTest(TestCase):
    def test__str__(self):
        category=Category(title="shirt")
        category.save()
        item = Product(name="Cotton White Casual Shirt", price=1000, category = category)
        item.save()
        self.assertEqual(item.__str__(),"Cotton White Casual Shirt")

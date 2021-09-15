from django.test import TestCase
from django.urls import reverse
from App_Payment.models import BillingAddress
from App_Login.models import User, Profile
from App_Payment.forms import BillingForm
# Create your tests here.

#There isn't any class in my views.py file and so I have added all the test functions for views.py file in the class below
class ViewsTest(TestCase):
    def test_checkout(self):
        response = self.client.get(reverse('App_Payment:checkout'))
        self.assertEqual(response.status_code, 302)

    def test_payment(self):
        response = self.client.get('GatewayPageURL')
        self.assertEqual(response.status_code, 404)

    def test_complete(self):
        response = self.client.get(reverse('App_Payment:complete'))
        self.assertEqual(response.status_code, 200)

    def test_purchase(self):
        response = self.client.get(reverse('App_Shop:home'))
        self.assertEqual(response.status_code, 200)

    def test_order_view(self):
        response = self.client.get(reverse('App_Shop:home'))
        self.assertEqual(response.status_code, 200)





#Testing models classes
class BillingAddressTest(TestCase):
    def setUp(self) -> None:
        user = User(email="1239@gmail.com")
        user.save()
        profile = Profile(username="Shamim")
        self.billingAddress=BillingAddress(user=user)
        self.billingAddress.user.profile=profile

    def test__str__(self):
        self.assertEqual(self.billingAddress.__str__(), "Shamim's billing address")

    def test_is_fully_filled(self):
        self.assertIs(self.billingAddress.is_fully_filled(),False)





#Testing froms classes
class BillingFormTests(TestCase):
    def test_meta_class(self):
        form = BillingForm(data={})
        self.assertTrue(form.is_valid())

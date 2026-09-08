from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class SignatureFormPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/signature/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("signature_form"))
        self.assertEqual(response.status_code, 200)

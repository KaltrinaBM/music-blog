from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm


class ContactUsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_us_post_valid(self):
        """
        Test that the contact_us view handles valid POST data and redirects.
        """
        form_data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'subject': 'Inquiry',
            'message': 'I would like to know more about your services.',
            'phone_number': '1234567890',
        }
        # Send a POST request
        response = self.client.post(reverse('contact_us'), data=form_data)
        # Follow the redirect
        self.assertEqual(response.status_code, 302)  # 302 means a redirect occurred
        redirected_response = self.client.get(response['Location'])  # Follow the redirect
        # Now check if the final response has the expected status code and content
        self.assertEqual(redirected_response.status_code, 200)  # Ensure the status code is OK
        self.assertContains(redirected_response, 'Thank You for Contacting Us!')  # Confirm success content

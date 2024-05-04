from django.test import TestCase
from .forms import ContactForm
from .models import ContactFormEntry


class ContactFormTest(TestCase):
    def test_valid_contact_form(self):
        """
        Test that a valid ContactForm is considered valid.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'subject': 'Inquiry',
            'message': 'Hello, I have a question about your blog.',
            'phone_number': '1234567890',
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid(), "ContactForm should be valid with correct data.")

    def test_invalid_contact_form(self):
        """
        Test that an invalid ContactForm is considered invalid.
        """
        form_data = {
            'name': '',
            'email': 'invalid-email',  # Invalid email format
            'subject': 'Inquiry',
            'message': '',  # Message is required
            'phone_number': '1234567890',
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid(), "ContactForm should be invalid with incorrect data.")

    def test_form_saves_to_database(self):
        """
        Test that a valid ContactForm saves data to the database.
        """
        form_data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'subject': 'Question',
            'message': 'I have a question about your services.',
            'phone_number': '0987654321',
        }
        form = ContactForm(data=form_data)

        if form.is_valid():
            contact_entry = form.save()
            self.assertEqual(contact_entry.name, 'Jane Doe', "The saved name should match the form data.")
            self.assertEqual(contact_entry.email, 'jane.doe@example.com', "The saved email should match the form data.")
            self.assertEqual(contact_entry.subject, 'Question', "The saved subject should match the form data.")
        else:
            self.fail("Form should be valid and save to the database.")

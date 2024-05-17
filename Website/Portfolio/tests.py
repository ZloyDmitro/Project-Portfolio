from django.test import TestCase
from django.urls import reverse
from .models import Contact

class ContactModelTest(TestCase):
    def test_contact_creation(self):
        # Testet die Erstellung eines Kontakts
        contact = Contact.objects.create(
            name='John Doe',
            email='john@example.com',
            phone='1234567890',
            message='Test message'
        )
        self.assertEqual(contact.name, 'John Doe')
        self.assertEqual(contact.email, 'john@example.com')
        self.assertEqual(contact.phone, '1234567890')
        self.assertEqual(contact.message, 'Test message')

class ContactViewsTest(TestCase):
    def test_contact_form_view(self):
        # Testet die Anzeige des Kontaktformulars
        response = self.client.get(reverse('contact_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


class ContactFormSubmissionTest(TestCase):
    def test_contact_form_submission(self):
        # Testet die erfolgreiche Einreichung des Kontaktformulars
        response = self.client.post(reverse('contact_form'), {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'message': 'Test message'
        })
        self.assertEqual(response.status_code, 302)  # Weiterleitung nach erfolgreicher Einreichung
        # Überprüfen Sie, ob der Kontakt in der Datenbank erstellt wurde
        self.assertTrue(Contact.objects.filter(name='John Doe').exists())


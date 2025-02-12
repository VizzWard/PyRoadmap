from django.test import TestCase
from django.urls import reverse
from django_dynamic_fixture import G
from django.contrib.auth.models import User

# Create your tests here.
class SignupViewTestCase(TestCase):
    def setUp(self) -> None:
        self.valid_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

        self.bad_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'wrongpassword',
        }

    def test_signup_successful(self):
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(response.status_code, 302)

    def test_signup_invalid(self):
        response = self.client.post(reverse('signup'), self.bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())



class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@mail.com',
            password='testpassword123'  # Usa create_user para manejar la encriptación
        )

        self.valid_data = {
            'username': 'testuser',
            'password': 'testpassword123',  # Asegúrate de que coincide con la real
        }

        self.bad_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }

    def test_login_successful(self):
        response = self.client.post(reverse('login'), self.valid_data)

        # Verificar que redirige correctamente después del login
        self.assertRedirects(response, reverse('index'))  # Ajusta la URL si es diferente

        # Refrescar el usuario desde la base de datos
        self.user.refresh_from_db()

        # Verificar que el usuario está autenticado
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)

    def test_login_invalid(self):
        response = self.client.post(reverse('login'), self.bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
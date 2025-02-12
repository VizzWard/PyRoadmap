# Tests en Django

Para esto se usa el proyecto del modulo 5 y 6.

---

### Nuevos comandos

Tests:
```commandline
python manage.py test --settings=settings.local
```

Test one:
```commandline
python manage.py test $(TEST_NAME) --settings=settings.local
```

shellplus:
```commandline
python manage.py shell_plus --ipython --settings=settings.local
```

---

## 1. Test a la app accounts

El código implementa tests unitarios para la funcionalidad de registro (`signup`) e inicio de sesión (`login`) en una aplicación Django. Se usa `TestCase` de `django.test` para simular peticiones HTTP y validar respuestas, además de verificar la persistencia de los datos en la base de datos.


### **Clase `SignupViewTestCase`**

```python
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


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
```

Esta clase prueba la funcionalidad de registro de usuarios.

1. **`setUp(self) -> None`**
   - Define dos conjuntos de datos:
     - `valid_data`: Contiene credenciales correctas.
     - `bad_data`: Contiene credenciales con contraseñas que no coinciden.

2. **`test_signup_successful(self)`**
   - Envía una petición `POST` con datos válidos al endpoint de registro (`signup`).
   - Verifica que la respuesta sea una redirección (`302`) hacia la página de `index`.
   - Confirma que el usuario fue creado en la base de datos.

3. **`test_signup_invalid(self)`**
   - Envía una petición `POST` con datos inválidos (contraseñas que no coinciden).
   - Verifica que la respuesta no redirige (`status_code 200`, manteniéndose en la página actual).
   - Asegura que el usuario no fue creado en la base de datos.

### **Clase `LoginViewTests`**

```python
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


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
```

Esta clase prueba la funcionalidad de inicio de sesión.

1. **`setUp(self)`**
   - Crea un usuario ficticio usando `django_dynamic_fixture.G()`.
   - Define datos válidos (`valid_data`) e inválidos (`bad_data`) para las pruebas.

2. **`test_login_successful(self)`**
   - Django redirecciona después de un login exitoso, generalmente a una vista de inicio (index) o a la página definida en `LOGIN_REDIRECT_URL` en `settings.py`.
   - En lugar de `assertEqual(response.status_code, 200)`, usamos `assertRedirects(response, reverse('index'))`, que comprueba la redirección correctamente.
   - `refresh_from_db()` asegura que estamos trabajando con la última versión del usuario en la base de datos.

3. **`test_login_invalid(self)`**
   - Envía una petición `POST` con credenciales incorrectas.
   - Verifica que el usuario no haya iniciado sesión (`is_authenticated` es `False`).

---

# 2. Test a la app products


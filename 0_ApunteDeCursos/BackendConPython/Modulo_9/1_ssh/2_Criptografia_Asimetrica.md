# Criptografía Asimétrica

## ¿Qué es la criptografía asimétrica?
La criptografía asimétrica es un método de encriptación que utiliza un par de claves: una clave pública y una clave privada. A diferencia de la criptografía simétrica, donde se usa una sola clave para cifrar y descifrar, en la asimétrica la clave pública se usa para cifrar los datos y la clave privada para descifrarlos.

## Características de la criptografía asimétrica
- **Seguridad mejorada**: La clave privada nunca se comparte, lo que dificulta su interceptación.
- **Autenticación**: Permite verificar la identidad del remitente mediante firmas digitales.
- **Intercambio seguro de claves**: Facilita el establecimiento de canales seguros de comunicación.
- **Computacionalmente más costosa**: Requiere más recursos que la criptografía simétrica.

## Ejemplos de algoritmos de criptografía asimétrica
1. **RSA (Rivest-Shamir-Adleman)**: Uno de los algoritmos más utilizados, basado en la dificultad de factorizar números grandes.
2. **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Usa curvas elípticas para ofrecer la misma seguridad con claves más pequeñas.
3. **Ed25519**: Una variante eficiente y segura basada en curvas elípticas.

## Generación de claves para conexión con servidores
Para generar un par de claves en Linux/macOS/Windows con OpenSSH:
```sh
ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
```
Esto genera dos archivos:
- `id_rsa` (clave privada, debe mantenerse segura).
- `id_rsa.pub` (clave pública, se comparte con el servidor).

## Autenticación por llaves
La autenticación basada en llaves permite acceder a un servidor sin necesidad de una contraseña, lo que mejora la seguridad.

### Mover la clave pública al servidor
Se puede copiar la clave pública al servidor con:
```sh
ssh-copy-id usuario@servidor.com
```
Si el comando no está disponible, puedes hacer lo siguiente manualmente:
```sh
scp ~/.ssh/id_rsa.pub usuario@servidor.com:~
ssh usuario@servidor.com
cat id_rsa.pub >> ~/.ssh/authorized_keys
rm id_rsa.pub
```

### Añadir las llaves al servidor
Para asegurarnos de que la clave se usa correctamente, debemos verificar los permisos:
```sh
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```
Ahora puedes conectarte sin necesidad de ingresar una contraseña:
```sh
ssh usuario@servidor.com
```
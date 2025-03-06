# SSH: Secure Shell

## ¿Qué es SSH?
SSH (Secure Shell) es un protocolo de red utilizado para acceder de manera segura a sistemas remotos a través de una conexión cifrada. Se usa comúnmente para la administración de servidores, la transferencia segura de archivos y la ejecución remota de comandos.

## Características de SSH
- **Cifrado de extremo a extremo**: Protege la información transmitida contra escuchas no autorizadas.
- **Autenticación segura**: A través de contraseñas o llaves criptográficas.
- **Redirección de puertos**: Permite acceder a servicios remotos de manera segura.
- **Compresión de datos**: Mejora la velocidad de transmisión en conexiones lentas.
- **Compatibilidad con múltiples algoritmos de cifrado**: RSA, ECDSA, ED25519, entre otros.

## ¿Cómo se asegura que alguien es quien dice ser?
SSH autentica a los usuarios y servidores mediante:
1. **Intercambio de claves públicas**: El cliente y el servidor verifican sus identidades con claves criptográficas.
2. **Fingerprint del servidor**: Cuando te conectas por primera vez a un servidor SSH, su clave pública se almacena localmente en `~/.ssh/known_hosts`. Si la clave cambia, SSH lanza una advertencia.
3. **Autenticación de usuario**:
   - **Contraseña**: Menos segura, vulnerable a ataques de fuerza bruta.
   - **Clave pública y privada**: Más segura, requiere que el cliente tenga la clave privada correspondiente a la clave pública almacenada en el servidor.

## Conexiones con servicios remotos
SSH permite conectarse a servidores de manera segura:
```sh
ssh usuario@servidor.com
```
Para conexiones en un puerto distinto al predeterminado (22):
```sh
ssh -p 2222 usuario@servidor.com
```

## Claves públicas y privadas
SSH usa criptografía de clave pública para autenticar usuarios y servidores.
### Generación de un par de claves
```sh
ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
```
Esto genera dos archivos:
- `id_rsa` (clave privada, debe mantenerse segura).
- `id_rsa.pub` (clave pública, se coloca en `~/.ssh/authorized_keys` en el servidor remoto).

Para copiar la clave pública al servidor:
```sh
ssh-copy-id usuario@servidor.com
```

## Túneles SSH
Permiten redirigir tráfico de red de forma segura.
- **Túnel local**:
  ```sh
  ssh -L 8080:localhost:80 usuario@servidor.com
  ```
- **Túnel remoto**:
  ```sh
  ssh -R 9000:localhost:22 usuario@servidor.com
  ```

## Uso de SSH con agentes de autenticación
Para evitar escribir la contraseña repetidamente, se puede usar `ssh-agent`:
```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

## Configuración avanzada en `~/.ssh/config`
Podemos definir configuraciones personalizadas para accesos rápidos:
```sh
Host servidor_alias
    HostName servidor.com
    User usuario
    Port 2222
    IdentityFile ~/.ssh/id_rsa
```
Esto permite conectarse con un simple:
```sh
ssh servidor_alias
```
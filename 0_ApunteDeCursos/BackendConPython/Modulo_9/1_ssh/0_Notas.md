# Comandos

## Server side

Conexion a servidor:

```bash
ssh <user>@<ip>
```

Crear nuevo usuario:

```bash
adduser <username>
```

Darle permisos:

```bash
usermod -aG sudo <username>
```

Cambiar entre usuarios:

```bash
su <username>
```

---

## Generar llaves ssh

Ruta a la carpeta (local):

```bash
cs ~/.ssh
```

Generar llaves:

```bash
ssh-keygen
```

Mover llaves al servidor:

```bash
ssh-copy-id <user>@<ip>
```

Modificar/Mover/Añadir llaves al servidor:

```bash
cs /home/<user>/.ssh
nano authorized_keys
```

---

## Transferencia de archivos

Subir archivos:

```bash
scp /local/file/path <user>@<ip>:/path/file
```

Descargar archivos:

```bash
scp <user>@<ip>:/path/file /local/file/path
```

---

## Asignar un alias a los aervidores (local)

Ruta:

```bash
cd ~/.ssh
```

Crear/Modificar archivo de configuracion:

```bash
nano config
```

Dentro del archivo, por cada servidor agregar:

```txt
Host <alias>
Hostname <direccion_ip>
User <usuario>
PubKeyAuthentication yes
IdentityFile ~/.ssh/<ssh_file>
```
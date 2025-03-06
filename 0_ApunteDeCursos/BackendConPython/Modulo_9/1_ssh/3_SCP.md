# SCP (Secure Copy Protocol)

## ¿Qué es SCP?
SCP (Secure Copy Protocol) es un protocolo que permite la transferencia segura de archivos entre un sistema local y un sistema remoto utilizando SSH (Secure Shell) para la autenticación y la protección de los datos en tránsito.

## Características de SCP
- **Seguridad**: Usa SSH para cifrar la comunicación.
- **Simplicidad**: Comando fácil de usar basado en la sintaxis de `cp`.
- **Eficiencia**: Copia archivos de manera rápida y segura.
- **Compatibilidad**: Funciona en sistemas Unix/Linux y en Windows mediante herramientas como PuTTY o OpenSSH.

## Sintaxis básica de SCP
La estructura básica del comando SCP es:
```sh
scp [opciones] origen destino
```

## Ejemplos de uso

### 1. Copiar un archivo de local a un servidor remoto
```sh
scp archivo.txt usuario@servidor:/ruta/destino/
```
Esto copia `archivo.txt` al directorio `/ruta/destino/` del servidor remoto.

### 2. Copiar un archivo de un servidor remoto a local
```sh
scp usuario@servidor:/ruta/remota/archivo.txt /ruta/local/
```
Esto descarga `archivo.txt` del servidor remoto al sistema local.

### 3. Copiar un directorio de local a remoto (modo recursivo)
```sh
scp -r carpeta/ usuario@servidor:/ruta/destino/
```
La opción `-r` indica que se debe copiar todo el contenido del directorio de manera recursiva.

### 4. Copiar archivos con un puerto SSH diferente
Si el servidor usa un puerto SSH distinto al predeterminado (22), usa `-P`:
```sh
scp -P 2222 archivo.txt usuario@servidor:/ruta/destino/
```

### 5. Copiar múltiples archivos a un servidor remoto
```sh
scp archivo1.txt archivo2.txt usuario@servidor:/ruta/destino/
```
Esto sube ambos archivos al servidor en la misma operación.

### 6. Copiar archivos entre dos servidores remotos
```sh
scp usuario1@servidor1:/ruta/archivo.txt usuario2@servidor2:/ruta/destino/
```
Esta operación transfiere un archivo directamente entre dos servidores sin pasar por la máquina local.

## Opciones comunes de SCP
| Opción  | Descripción |
|---------|-------------|
| `-r`    | Copiar carpetas recursivamente |
| `-P`    | Especificar puerto SSH |
| `-C`    | Habilitar compresión de datos |
| `-i`    | Especificar un archivo de clave privada SSH |
| `-v`    | Modo verbose (para depuración) |

## Consideraciones de seguridad
- **Autenticación por clave SSH**: Para mayor seguridad, usa autenticación con claves en lugar de contraseñas.
- **Evitar conexiones inseguras**: SCP cifra la transferencia, pero si necesitas mayor flexibilidad, considera `rsync` sobre SSH.
- **Verifica los permisos**: Asegúrate de que los archivos copiados mantengan los permisos correctos en el servidor de destino.

## Alternativas a SCP
- **rsync**: Proporciona sincronización de archivos con optimización en la transferencia de datos.
- **sftp**: Utiliza SSH para transferencias de archivos de manera más interactiva y con mayor control.

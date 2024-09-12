# DDl - Creación de otros objetos

## Triggers

Script para la creación de un trigger el cual va a ejecutar automaticamente justo antes de insertar un registro en la tabla Usuario, va a verificar si en el registro que se esta insertado, el campo Email esta vacio (NULL) o no, si esta vacio entonces va a asignarle un estado inactivo (Activo = 0).

- DELIMITER Sirve para indicarle a MySQL donde finaliza el bloque de código.

```sql
DELIMITER $$

CREATE TRIGGER BI_Usuario
    BEFORE INSERT ON Usuario 
	FOR EACH ROW
BEGIN
    IF (NEW.Email IS NULL) THEN
		SET NEW.Activo = 0;
	ELSE
		SET NEW.Activo = 1;
	END IF;
END$$
```

El funcionamento del trigger puede ser probado con la ejecución de estos scripts. Al no especificar el campo Email, el trigger va a asignar un valor 0 al campo Activo. Cuando el campo Email si se especifica entonces el campo Activo tendrá valor 1.

```sql
INSERT INTO Usuario (Nombre, Apellido)
VALUES ('Tu_Nombre', 'Tu_Apellido')

INSERT INTO Usuario (Nombre, Apellido, Email)
VALUES ('Tu_Nombre', 'Tu_Apellido', 'nombre@gmail.com')
```

Luego se comprueba el resultado con un query SELECT en la tabla Usuario.

```sql
SELECT *
FROM Usuario;
```

El cual generará un resultado similar al siguiente:

| ID  | Nombre    | Apellido    | Email            | Fecha_Nacimiento | Activo |
|-----|-----------|-------------|------------------|------------------|--------|
| 1   | Tu_Nombre | Tu_Apellido | NULL             | NULL             | 0      |
| 2   | Tu_Nombre | Tu_Apellido | nombre@gmail.com | NULL             | 1      |

## Funciones

Script para la creación de una función la cual va a concatenar el nombre y apellido del usuario en un solo campo y lo convertirá a mayusculas. El parametro de entrada es el ID de la tabla Usuario.

La función podrá ser invocada desde cualquier consulta DML, por ejemplo una consulta `SELECT`.

- `DELIMITER` Sirve para indicarle a MySQL donde finaliza el bloque de código.
- `DROP FUNCTION IF EXISTS` borrará la función si es que ya existe, para luego crearla nuevamente. Sin esta instrucción, el script CREATE FUNCTION solo funcionaría una vez y para modificaciones posteriores sería necesario utilizar un ALTER FUNCTION.
- `RETURNS VARCHAR(101)` indica que el tipo de dato del resultado de la función será una cadena de texto de longitud maxima 101 caracteres.
- `READS SQL DATA` sin esta instrucción la instrucción `SELECT` daría error.
- El parametro de entrada va dentro de parentesis justo despues del nombre la función.
- `DECLARE` permite declarar la variable que será utilizada para almacenar el nombre completo del usuario.
- `CONCAT` concatena el primer nombre, un espacio en blanco y el appelido del usuario en un solo campo.
- `UPPER` convierte el resultado de la concatenación en mayusculas.
- `INTO` permiate almacenar el resultado del select en la variable declarada.
- `RETURN` la última instrucción de una función debe ser devolver el resultado generado.

```sql
DELIMITER $$

DROP FUNCTION IF EXISTS Fn_Nombre_Completo;
CREATE FUNCTION Fn_Nombre_Completo(
    ID_Usuario INT
)
RETURNS VARCHAR(101)
READS SQL DATA
BEGIN
	DECLARE Nombre_Completo VARCHAR(101);
	
	SELECT UPPER(CONCAT(Nombre, ' ', Apellido))
	INTO Nombre_Completo
	FROM Usuario
	WHERE ID = ID_Usuario;

	RETURN Nombre_Completo;
END $$
```

En el siguiente ejemplo, la función es invocada desde la instrucción SELECT y el resultado se verá desplegado como cualquier campo.

- Nombre_Completo es un alias, los alias son opcionales, pero mejoran la visualización de los datos.

```sql
SELECT ID, Fn_Nombre_Completo(id) Nombre_Completo
FROM Usuario;
```

El cual generará un resultado similar al siguiente:

| ID | Nombre_Completo |
|----|-----------------|
| 1  | MAY CODE        |

## Procedimientos (Stored Procedures)

Script para la creación de un procedimiento, parentesis vacios indica que no recibe parametros. Cada vez que se ejecute, leerá la tabla Historial_conexion, filtará las filas que tengan el campo IP con valor NULL y les asignará el valor '0.0.0.0'.

- `DELIMITER` Sirve para indicarle a MySQL donde finaliza el bloque de código.
- `DROP PROCEDURE IF EXISTS` borrará el procedimiento si es que ya existe, para luego crearla nuevamente. Sin esta instrucción, el script `CREATE PROCEDURE` solo funcionaría una vez y para modificaciones posteriores sería necesario utilizar un `ALTER PROCEDURE`.

```sql
DELIMITER //

DROP PROCEDURE IF EXISTS SP_Actualizar_IP_Vacia;
CREATE PROCEDURE SP_Actualizar_IP_Vacia()
BEGIN
	UPDATE Historial_conexion
	SET IP = '0.0.0.0'
	WHERE IP IS NULL;
END //
```

- `CALL` ejecuta el procedimiento, entre los parentesis se especificarían los parametros, si los hubiera.

```sql
CALL SP_Actualizar_IP_Vacia();
```
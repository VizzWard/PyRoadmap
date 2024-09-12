# DCL (Data Control Language)

Creación de 3 usuarios, el proposito del usuario WebSite es ser utilizado desde un API o sistema que se conecte a la base de datos. El proposito de los usuarios Developer1 y Developer2 es ser utilizados por 2 personas distintas y de acuerdo a sus responsabilidades serán asignados sus permisos. `CREATE USER` son sentencias DDL, es necesario que existan usuarios previo a asignarles permisos.

## Asignación de permisos

- Al usuario WebSite, el usuario tendrá todos los permisos sobre las tablas, excepto la tabla Usuario, sobre la tabla Usuario no podrá eliminar usuario.
- Al usuario Developer1 se la asignará todos los permisos sobre las tablas Menu y Menu_Usuario, sobre las tablas Usuario y Historial_Conexion solo tendrá permiso de lectura, para evitar que Developer1 haga modificaciones sobre esas tablas.
- Al usuario Developer2 solo se le asignará permiso de lectura sobre las tablas Menu y Menu_Usuario, sobre las tablas Usuario y Historial_Conexion no tendrá ningun acceso.
- `GRANT` sentencia para otorgar permisos.
- `SELECT` para asignar permiso de lectura sobre la tabla especificada.
- `INSERT` para asignar permiso de inserción sobre la tabla especificada.
- `UPDATE` para asignar permiso de actualización sobre la tabla especificada.
- `DELETE` para asignar permiso de eliminación sobre la tabla especificada.
- `ON` luego de este texto se indica el nombre de la tabla a la cual se le quiere asignar los permisos.
- `TO` luego de este texto se indica el nombre del usuario al cual se le quiere asignar los permisos.

```sql
GRANT SELECT, INSERT, UPDATE ON Usuario TO WebSite;
GRANT SELECT, INSERT, UPDATE, DELETE ON Historial_Conexion TO WebSite;
GRANT SELECT, INSERT, UPDATE, DELETE ON Menu TO WebSite;
GRANT SELECT, INSERT, UPDATE, DELETE ON Menu_Usuario TO WebSite;

GRANT SELECT ON Usuario TO Developer1;
GRANT SELECT ON Historial_Conexion TO Developer1;
GRANT SELECT, INSERT, UPDATE, DELETE ON Menu TO Developer1;
GRANT SELECT, INSERT, UPDATE, DELETE ON Menu_Usuario TO Developer1;

GRANT SELECT ON Menu TO Developer2;
GRANT SELECT ON Menu_Usuario TO Developer2;
```

- Al usuario WebSiste se le quitará el acceso de eliminar sobre la tabla Menu.
- `REVOKE` sentencia para revocar o quitar permisos.
- `SELECT` para quitar permiso de lectura sobre la tabla especificada.
- `INSERT` para quitar permiso de inserción sobre la tabla especificada.
- `UPDATE` para quitar permiso de actualización sobre la tabla especificada.
- `DELETE` para quitar permiso de eliminación sobre la tabla especificada.
- `ON` luego de este texto se indica el nombre de la tabla a la cual se le quiere quitar los permisos.
- `FROM` luego de este texto se indica el nombre del usuario al cual se le quiere quitar los permisos.

```sql
REVOKE DELETE ON Menu FROM WebSite;
```


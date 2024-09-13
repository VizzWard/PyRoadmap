# Cardinalidad

La cardinalidad de la correspondencia indica el número de entidades con las que puede estar relacionada una entidad dada.

- Uno a Uno: (1:1) Un registro de una entidad A se relaciona con solo un registro en una entidad B.
- Uno a Muchos: (1:N) Un registro en una entidad en A se relaciona con uno o muchos registros en una entidad B. Pero los registros de B solamente se relacionan con un registro en A.
- Muchos a Muchos: (N:M) Una entidad en A se puede relacionar con 1 o con muchas entidades en B y viceversa.
- "0" si cada instancia de la entidad no está obligada a participar en la relación.
- "1" si toda instancia de la entidad está obligada a participar en la relación y, además, solamente participa una vez.
- "N" , "M", ó "*" si cada instancia de la entidad no está obligada a participar en la relación y puede hacerlo cualquier número de veces.
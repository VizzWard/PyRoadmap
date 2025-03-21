
# Modelado de Microservicios

## 📌 Definición de un Servicio
### ¿Qué es un servicio?
Un servicio es una unidad independiente de software que realiza una función específica dentro de un sistema más amplio. En el contexto de microservicios, un servicio es autónomo y responsable de una tarea claramente definida.

### Responsabilidades y límites del servicio
- Cada servicio debe tener una **responsabilidad única** y bien definida (Principio de Responsabilidad Única).
- Los límites del servicio se establecen según el **contexto funcional o lógico** al que pertenece.
- Los servicios deben ser **independientes entre sí** para permitir un desarrollo, despliegue y escalado autónomos.

---

## 📌 DDD (Domain-Driven Design)
### Principios básicos de Domain-Driven Design
- **Entidad:** Objeto con identidad única y ciclo de vida.
- **Value Object:** Objeto que no tiene identidad propia, solo se define por sus atributos.
- **Aggregate:** Conjunto de entidades y objetos de valor relacionados, tratados como una unidad.
- **Repository:** Mecanismo para acceder a objetos de dominio persistidos.
- **Bounded Context:** Límites conceptuales dentro de los cuales un modelo específico es válido.

### Pros vs Contras
#### ✅ Pros:
- Facilita la creación de servicios con un propósito claro.
- Mejora la organización y mantenibilidad del código.
- Claramente define responsabilidades.

#### ❌ Contras:
- Puede ser complejo de implementar en sistemas grandes.
- Requiere un buen entendimiento del dominio del problema.

---

## 📌 Acoplamiento alto vs bajo
### ¿Qué es acoplamiento?
El acoplamiento se refiere al grado de dependencia entre diferentes servicios o componentes. Un acoplamiento alto significa que dos o más servicios dependen fuertemente uno del otro, mientras que un acoplamiento bajo implica que pueden operar de manera independiente.

### Importancia en microservicios
El acoplamiento bajo es esencial para microservicios porque:
- Facilita la escalabilidad y despliegue independiente de servicios.
- Permite a cada equipo trabajar en sus propios servicios sin interferir con otros.

### Pros y contras del acoplamiento alto
#### ✅ Pros:
- Comunicación directa y rápida entre servicios.
- Implementación inicial más sencilla.

#### ❌ Contras:
- Difícil de escalar y mantener.
- Cambios en un servicio afectan a otros.

### Pros y contras del acoplamiento bajo
#### ✅ Pros:
- Mayor flexibilidad y escalabilidad.
- Despliegue independiente de servicios.

#### ❌ Contras:
- Comunicación más compleja (normalmente a través de APIs).
- Mayor sobrecarga en el diseño.

### Tips para lograr un acoplamiento bajo
- Usar APIs bien definidas para la comunicación entre servicios.
- Aplicar patrones de diseño como **Event-Driven Architecture (EDA)**.
- Evitar compartir bases de datos entre servicios.

---

## 📌 Cómo descomponer un monolito
### Razones para migrar un monolito
- Dificultad para escalar aplicaciones grandes.
- Baja flexibilidad para agregar nuevas funcionalidades.
- Tiempo prolongado de despliegue debido a la dependencia entre módulos.

### Estrategias para descomponer un monolito
1. **Identificar contextos delimitados (Bounded Contexts):**
   - Aplicar conceptos de DDD para definir áreas lógicas independientes.
   
2. **Dividir la aplicación por funcionalidades:**
   - Crear servicios independientes para cada funcionalidad importante (usuarios, productos, pagos, etc.).

3. **Migración incremental:**
   - Descomponer partes críticas del sistema una a la vez para no interrumpir la operación.

4. **Pruebas exhaustivas:**
   - Asegurar que cada servicio nuevo funciona correctamente antes de desconectarlo del monolito principal.

5. **Implementar comunicación asíncrona:**
   - Facilita la comunicación entre servicios independientes usando colas de mensajes o eventos.
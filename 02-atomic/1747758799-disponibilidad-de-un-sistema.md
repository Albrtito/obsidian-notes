---
id: 1747758799-disponibilidad-de-un-sistema
aliases:
  - Disponibilidad de un sistema
tags:
  - #Distri
---

# Disponibilidad de un sistema
Se define la disponibilidad de un sistema como la probabilidad de que el sistema este funcionando correctamente en un instante t. Se nombra como $A(t)$

A diferencia de la fiabilidad, la disponibilidad considera un instante concreto de tiempo.Se calcula usando el tiempo medio hasta fallo y el tiempo medio de reparación. 
$$
A(t) = \frac{TMF}{TMF+TMR}
$$
**Donde:** 
- TMF: Tiempo medio hasta fallo
- TMR: Tiempo medio de reparación

> ej: Una disponibilidad del 99% aún no es buenísima para un sistema constante pues son 3.65 días no disponible al año

### Up
- [[1747756642-sistema-tolerante-a-fallos|Sistema tolerante a fallos]]
### Down
- [[1747756890-sistemas-fiables|Fiabilidad de un sistema]]


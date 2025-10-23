---
id: 1747756642-sistema-tolerante-a-fallos
aliases:
  - Sistema tolerante a fallos
tags:
  - #Distri
---

# Sistema tolerante a fallos
El objetivo de un sistema tolerante a fallos es el de **que sea ALTAMENTE FIABLE** aún con fallos de software o hardware. Esto significa **evitar que los fallos produzcan averías**.
Cuando hablamos de tolerancia a fallos otra cosa importante a tener en mente es que el sistema ya esta en marcha, tolerancia quiere decir que el fallo va a pasar, y que se hace después es la pregunta.

## Conceptos básicos:
### Como se producen las averías:
- Si un sistema se desvía e su especifiacion aparece una **avería o defecto** 
- La cause del defecto se denomina **fallo** 
- Una avería se manifiesta de forma externa pero es un resultado de algo interno **errores** 

Estas tres cosa pasan en orden.
1. Fallo
2. Error
3. Avería/Defecto

### Reparación de averías:
Un sistema siempre estará funcionando o parado por causas de reparacion. Entonces podemos distinguir entre:
1. Mantenimiento correctivo: Debido a fallos se ha parado el sistema
2. Mantenimiento preventivo: Antes de que ocurran los fallos paramos el sistema

Según eltiempo de mantenimiento necesario bajará la disponibilidad del sistema

## Tolerancia a fallos:
La tolerancia a fallos se basa en la **redundancia**, mucho de todo. Esto tiene el inconveniente de que **se aumenta la complejidad del sistema y puede introducir fallos adicionales**. Se divide en grados según lo mucho que se redunde. 
1. **Tolerancia completa:** Todo sigue igual, al menos durante un tiempo
2. **Degradación aceptable:** Falllan cosas pero no todo
3. **Parada segura:** Se para el sistema pero rompiéndose mucho menos de lo que se podría haber roto
### Fases:
1. **Detección de errores:** Algo va mal
2. **Confinamiento y diagnóstico de daños:** Que va mal, que deje de ir mal
3. **Recuperación de errores:** Que hacemos para recuperar al sistema, recuperación hacia delante o hacia atrás
4. **Tratamiento de fallos y servicio continuado:** Que hacemos para seguir dando servicio


***
### Up
- [[Distribuidos]]
### Down
- [[1747756890-sistemas-fiables|Sistemas fiables]]
- [[1747757386-tipos-de-fallos-en-sistemas|Tipos de fallos en sistemas]]
- [[1747758799-disponibilidad-de-un-sistema|Disponibilidad de un sistema]]
- 


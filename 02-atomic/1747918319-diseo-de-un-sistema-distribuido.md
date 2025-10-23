---
id: 1747918319-diseo-de-un-sistema-distribuido
aliases:
  - Diseño de un sistema distribuido
tags:
  - #Distri
---

# Diseño de un sistema distribuido
A la hora de diseñar un sistema distribuido se realizarán los siguientes pasos. 

1. Estructura del sistema: Aquií se ha de definir 
    - Que máquinas haciendo que cosas existen
    - Que protocolo de comunicación se va a usar y pq
    - Se usará concurrencia? 
        - En caso de que se use, como se van a crear threads y pq
        > [!NOTE]
        > Normalmente se utilizará hilos a demanda pues es más util y eficiente si no se conoce la cantidad de clientes que hay
        
    - Suposiciones que se hacen sobre el sistema, su red, etc.

2. Interfaces y protocolos para cada sistema:
    - Que interfaces hacen falta y que tienen que hacer
    - Que pasa si error
    - Como tienen que hacer las cosas, en que orden
    - Como se van a mandar las cosas, en que orden
    - Como se van a mandar las cosas, con que formato

**Remarks:** 
- En general esta bien ir dividiento cada apartado por cliente/servidor o tipos de clietes y tipos de servidores para que se entienda mejor


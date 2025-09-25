---
aliases:
  - Sustitución polialfabética periódica
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2025-02-27
sr-interval: 98
sr-ease: 249
---
# Sustitución polialfabética periódica.

> [!Quote] Remember: 
> Decimos que algo es **polialfabético** cuando el alfabeto cifrado generado no es isomorfo al alfabeto original.
> Cuando los alfabetos que utilizamos **se repiten** de forma periódica lo llamamos sustitución poli-periódica. 

Dividimos entre la creación de alfabetos lineales y alfabetos progresivos:
## Alfabetos lineales:
Definimos el cifrado tal y como lo definió Vigenère en el 1500:
$$
\boxed{E(m_j) = (m_j + k_{(j \mod m)}\mod n)}
$$
+ Estos alfabetos son lineales
>p.e: Si a cada letra del abecedario le doy una constante $b_i$ y hago una [[1726494310 - Sustitución monoalfabeto monográfica|Sustitución monoalfabeto monográfica]] para cada una de ellas. Estoy generando un alfabeto nuevo por cada uno de los grafos.


## Alfabetos progresivos: 

> [!NOTE] Alfabeto progresivo: 
> Esto quiere decir que cada nuevo grafo cifrado **depende del anterior grafo**. (El nuevo alfabeto depende de algo anterior)

> p.e: La máquina enigma

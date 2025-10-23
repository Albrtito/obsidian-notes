---
aliases:
  - Cifrado asimetrico
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# Cifrado asimetrico

> [!quote] Remember: 
> Recordamos todas las bases de la aritmética modular para exponer la siguiente teoría del cifrado asimétrico:
> + [[20240520 - 171554 - Definition - Modular arithmetics - Multiplicative inverse of x|Modular arithmetics - Multiplicative inverse of x]]
> + [[1727100415 - Theorem - Indicador de Euler|Theorem - Indicador de Euler]]
> + [[20240519 - 232552 - Definition - Relatively prime numbers|Relatively prime numbers]]

## Más bases matemáticas: 
+ [[1728916836 - Restos potenciales|Restos potenciales]]
+ [[1728917414 - Orden gaussiano|Orden gaussiano]]

### [[1728919808 - Logaritmos discretos|Logaritmos discretos]]

> [!attention] IMPORTANTE:
> Los logaritmos discretos son **lo que hace que podamos cifrar de forma pública**. 
> Para una equacion basada en uno de estos algoritmos:
> $$
> x = log_a b \mod n
> $$
> + x será igual al número que tenemos que elevar a para que de b. 
>   **LA UNICA FORMA DE ENCONTRARLO ES BUSCAR LOS POSIBLES VALORES DE A**

 
  **Remarks:**
  No solo tenemos esta propiedad sino que además se cumple: 

+ **Si a es una ==raiz primitiva== de n, el logarimo siempre existe, x existe**. 


## Modelo de los criptosistemas asimétricos:

### Contexto histórico:
Antes de idear el modelo de criptosistema asimétrico se creía que **sería imposible pasar claves de forma seguro por un canal no seguro**. El concepto que se explica a continuación fue ideado por la inteligencia británica aunq se conoce por un paper publicado algo después: 
> [New Directions in Cryptography, Martin E. Hellman, Diffe. Noviembre 1976](https://www-ee.stanford.edu/~hellman/publications/24.pdf)
+ Lo de los ingleses se supo más tarde pq era confidencial
### Idea fundamental:

> [!BUG]  Problema:
> El problema que nos encontramos en el cifrado simétrico es que **el intercambio de claves se ha de hacer por un medio seguro**.

> [!check] Solución: 
> La solución está en que cada cliente de un servicio de cifrado(que es tanto receptor como emisor) posea un **par de claves** relacionadas entre ellas de forma que conociendo una el cliente sabe obtener la otra pero para cualquiera que no sea el obtenerla será computacionalmente imposible.
+ Con esta idea, el cliente compartirá una de las dos claves a todo el mundo, cualquiera que quisiese mandarle información habrá de hacerlo cifrándola con esa clave (pública) y solo podrá ser descifrada con la segunda clave (privada)
#### Aplicación con aritmética modular:
Este concepto explicado se implmenta utilizando las propiedades de la aritmética modular, de esta forma la clave privada y la pública se **relacionan en que son una la inversa de la otra**.

+ D : Clave privada
+ E: Clave pública
+ C: Texto cifrado => $C = E(k_u, M) = E_{ku}(M)$
+ M: Texto en claro => $M= D(k_v,C) = D_{kv}(C)$

#### Sketch:

![[1728912947 - Cifrado asimetricoj.png]]
+ Alice cifra con la clave pública de Bob 
+ Bob descifra con su clave privada
***

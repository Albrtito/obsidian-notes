---
aliases:
  - Cuerpos de Galois
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# Cuerpos de Galois
Existe un cuerpo de Galois $CG(q^n)$ formado por polinomios a(x) de grado (n-1) o menos cuyos coeficientess $a_1 \in Z_q$ 
$$\boxed{ CG(q^n) \Rightarrow a(x) = a_{n-1}x^{n-1}+a_{n-2}x^{n-2} + ... + a_1x+ a_0 \mod p(x)}$$
+ $a_1 \in Z_q$ donde q es primo
+ $\mod p(x)$ es un polimonio de grado n y es un polinoio irreducible: Se suele utilizar $p(x) = x^n + x + 1: n = 1,2,3,4,5…$ 
Los cuerpos de Galois tienen **operaciones de suma, multiplicacion, división, etc…**


## En criptografía: 
Para usos criptográficos trataremos con un cuerpo de Galois en concreto: 
$$
CG(2^n)
$$
+ $a_i \in Z_2 = {0,1}$
+ Solemos representar este polinomio como: $a(x) \in CG(2^n)$ / $(a_{n-1}, a_{n-2}, …, a_1, a_0)$/ $(a_{n-1} a_{n-2} … a_1 a_0)$ 

Al utilizar este polinomio específico, obtendremos básicamente **strings de bits** con una longitud igual a n.

### Operaciones con el cuerpo $CG(2^n)$: 

> [!quote] Recuerda: 
> Como estamos en un cuerpo con módulo 2 todas las operaciones se hacen acorde. 

+ Al terminar las operaciones siempre hemos de **reducir** los polinomios[^2]

**Remark:**
+ Esto lo que va a significar es que realizaremos operaciones binarias utilizando la representación binaria de los polinómios
#### Suma y resta:
+ **Sumar y restar:** Sumar y restar (si, **ambas**) es equivalente a realizar un **XOR**[^3]
$$
\boxed{
C = a + b = a_i \oplus b_i}
$$

#### Multiplicación: 
Habrá que utilizar el $\mod p(x)$ : 
$$
\boxed{C = a\cdot b , C = \sum_{i= 1}^n(a_i\cdot b)xî \mod p(x)}
$$
$$
a_i \cdot b = \begin{cases} b - b_{n-1} + ...+ b_0&& si: a_i = 1 \\0&&si : a_i = 0\end{cases}$$
+ $a_i \cdot b$ es un **AND** 
#### División: 
+ Es lo mismo que **calcular el inverso**
Aunq en este caso estamos calculando inversos de polinomios, podemos utilizar los mismos métodos que utilizábamos para cualquier x.[^1]

Necesitamos saber cual es el indicador de euler del polinomio $p(x)$. 

Para ello tenemos que obtener el número de polinomios coprimos. Como es un coeficiente primo y estamos tratando como en binario. Podemos obtener **todos** los polinomios menos el final con la exprsión $2^n - 1$ 

+ El indicador de euler de ul polinomio **con coeficiente primo igual a 2** será igual a. 
$$
\boxed{\Phi(p(x)) = 2^n - 1}
$$
Entonces para calcular el inverso de un polinomio: 
$$
\boxed{a^-1 \mod p(x) = a^{2^n -1-1} \mod p(x) = a^{2^n-2} \mod p(x)}
$$


***

[^1]: [[20240520 - 171554 - Definition - Modular arithmetics - Multiplicative inverse of x|Modular arithmetics - Multiplicative inverse of x]]
[^2]: Cuado hablamos de reducir polinomios, lo que significa es calcular el módulo con respecto a otro polinomio. Igual que reduciríamos (7 mod 2) a (1 mod 2)
[^3]: La operación XOR se **ha de realizar siempre** **ENTRE DOS SUMANOS**. Hay que operar en grupos de dos. 

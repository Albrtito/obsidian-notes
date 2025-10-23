---
aliases:
  - Exercises - Resolucion gráfica y modelado de programacion lineal
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-25
sr-interval: 53
sr-ease: 292
---
# Exercises - Resolucion gráfica y modelado de programacion lineal
## Modelado:
### Problema de ejemplo::
La empresa UniZumo fabrica y distribuye zumos de piña en las presentaciones Néctar de Piña y Unizumo de Piña. Ambos zumos se fabrican a base de concentrado de piña, de modo que en cada litro de zumo hay un 20 % y un 50 % de concentrado respectivamente. Para la fabricación del año se dispone de 2,4 millones de litros de concentrado de piña y se ha pactado con los mayoristas un precio de 1,25 euros por tetra brik (con una capacidad de un litro) de Néctar de Piña y 2,05 euros por el de Unizumo de Piña, bajo la condición de que no se saquen al mercado más de 6 millones de litros de zumo. 
Se pide: 
1. Modelar el problema como un problema de Programación Lineal para obtener las cantidades de cada producto que UniZumo debe fabricar para maximizar los ingresos por ventas. 
2. Resolver gráficamente el problema. 
3. Representar el problema en forma estándar

**Variables:**
m.l → Millones de Litros
+ $x_1$: m.l. Néctar
+ $x_2$ : m.l. Unizumo
**Función:**
$$
f_o = \max z = 1.25 x_1 + 2.05 x_2
$$
**Restricciones:**
$$
\begin{gather}
0.2x_1 + 0.5x_2 \le 2.4\\\\
x_1 +x_2 \leq 6\\\\
x_1, x_2 \geq 0\\\\
x_1, x_2 \in \mathbb{N} \cup \{0\}
\end{gather}
$$

**Sistemas de ecuaciones:**
Se han de solucionar utilizando el [[1729167814 - Resolucion de sistemas lineales#Usando el método de la inversa|método de la matriz inversa]]

$$
\begin{gather}
AX = b\\
X = A^{-1}b
\end{gather}
$$
+ Para ello debemos de calcular la matriz inversa. Lo haremos a través del siguiente método: 
$$
A^{-1} = \frac{(adj(A))^T}{det(A)}
$$

**Trabajo con números enteros y racionales:** 
Trabajaremos usando números racionales para **prevenir la pérdida de error**. 
> p.e: Usaremos $1 \over 5$ en vez de $0.2$

**Implementación de condicionales:**
>Si una variable toma un valor entonces la otra toma otro **en consecuencia**

**Representación en forma estandar:**
Parar representar un problema de forma estandar hemos de representar las desigualdades de las restricciones como igualdades en las que todos los valores de la parte derechas son positivos. 
+ Para esto introducimos **variables de holgura**
> p.e: Transformamos $0.2x_1 + 0.5x_2 \leq 2.4$ en $0.2x_1 + 0.5x_2 + x_3 = 2.4$. Dnd $x_3$ es la variable de holgura. 



## Ejemplo de prueba evaluación 30min: 

> [!ATTENTIon] Examen 
> En la primera prueba de evaluación no entra un SIMPLEX, se hará la resolución de un modelo de forma gráfica 100% 


### Modelado:
**Función objetivo:**
$$ \min z = x_1 + x_2$$
**Variables:**
$x_1 : \text{H. Primer trabajo}$
$x_2: \text{h. Segundo trabajo}$

**Restricciones:**
$\text{1) } 20 \geq x_1 + x_2$
$\text{2) } x_1 \leq x_2$
$\text{3) }150 \leq x_1\cdot 15  +  x_2\cdot 10$

**Representación en forma canónica:**
$$
\begin{gather}
\text{Función objetivo: }\\
\max z' = -x_1 - x_2\\\\

\text{Restricciones:}\\\\
 20 \leq x_1 + x_2\\\\
 0\leq x_2-x_1\\\\
150 \leq x_1\cdot 15  +  x_2\cdot 10\\\\
xi\geq 0
\end{gather}
$$
### Resolución gráfica:
1. **Obtenemos la región factible**
![[1728047794 - Ejemplos SIMPLEXj.png]]

2. **Obtenemmos el valor de -x-y para un z arbitrario y comprobamos:**
	1. En este caso hemos comprobado con z = -10. 

![[1728047794 - Ejemplos SIMPLEXj-1.png]]
3. **Vemos que la solución es el punto: (10,0)**
   
   Entonces nuestra solución que minimiza las horas  será:
   $x_1 = 10$ , $x_2 = 0$ 
***


## Tips: 
+ Cuidado con **unidades horarias** pues no se representan los minutos como porcentajes como en otros casos.  
	  → Calcular la equación en minutos o en horas
+ Para ejercicios con expresiones condicionales ver [[1727968107 - Expresiones condicionales en programación lineal|Expresiones condicionales en programación lineal]]

***

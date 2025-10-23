---
id: 1726759457-programacionlineal
aliases:
  - Programacion Lineal
tags:
  - heuri
sr-due: 2025-03-05
sr-ease: 272
sr-interval: 109
---
# Programación Lineal

> [!NOTE] Intro:
> La programación lineal tiene como objetivo la resolución de problemas que pueden ser expresados como **una relación lineal entre sus variables**,sujetas a unas restricciones. 
> $$
> \begin{gather}
> f: (\max/\min) z = c^Tx\\
> \text{sujeto a}: Ax = b\\ 
> \text{con}: x \geq 0
\end{gather}
> $$
> Donde: 
> + z : es el valor a maximizar/minimizar
> + $c^T$: es el vector de coeficientes(racionales), transpuesto para que la multiplicación sea posible.
> + $x$ : es el vector de variables/incognitas del problema
> + A: Es la matriz de costes (coeficientes de las variables para cada restricción)
> + $b$ : es el vector de recursos que imponen las restricciones
>
>Además, el problema define **restricciones que se aplican a las variables de la función.**

+ En resumen: Los problemas de programación lineal se definen con **variables, función y restricciones**


> [!done] Solución:
> Damos entonces las siguientes definiciones de los **tipos de soluciones**:
> 
> + Un vector X que resuelve Ax =b se llama **solución**
> + Un vector X≥ 0 que resuelve Ax = b se llama **solución factible**
> + Un vector $X_B \geq 0$ que resuelve $B_{mxm} X_b = b$ se llama **solución factible básica**
> +  Un vector $X^*$ es una **solución factible básica y óptima** si y solo si:
> 		$$C_B^TX^* \geq C_B^TX, \forall x \in F$$
> 
>+ La solución óptima puede ser única o no. 
>+ En este segundo caso decimos que existen **soluciones óptimas alternativas**
>+ Podría **no existir solución factible y óptima**. En estos casos parece que la solución óptima siempre puede mejorar. → Esto nunca pasa
>
>**La condiciones para que un problema sea resoluble serán:**
>+ Se sabe si algo tiene solución al resolver el sistema algebráico. **Se puede resolver un sistema algebráico siempre y cuando A sea invertible: [[1729167252 - Cálculo de la matriz inversa|Inverse matrix]]**
>
>$$
>Ax_A = b \Rightarrow x_A= A^{-1}b
>$$
>
> + Debido  a esto u**n cambio en b no afectará a la resolución del sistema**

## Formas del modelo en programación lineal:
Según la forma en la que se exprese la función y las restricciones podemos representar el problema de forma **canónica o de forma estandar**
+ [[1727270318 - Forma canónica|Forma canónica]]
+ [[1727270366 - Forma estandar|Forma estandar]]

### Transformaciones:
Para transformar el problema a forma canónica/estandar, utilizamos las siguientes transformaciones:

+ Para convertir una función de minimización en otra de maximización **multiplicamos por -1**

$$
\min z = c^TX \triangleq \max z' = -c^TX
$$

[^1]

+ Cambiar de signo al vector de recursos es lo mismo que multiplicar por -1. Lo que le da la vuelta a la inequality.
+ Para convertir una igualdad en desigualdad debemos de **introducir una variable de holgura** (sumando o restando).

$$
\begin{gather}
\sum_{j=1}^{n}a_{ij}x_j \leq b_i  \triangleq \sum_{j=1}^{n}a_{ij}x_j + s_i = b_i\\
\sum_{j=1}^{n}a_{ij}x_j \geq b_i  \triangleq \sum_{j=1}^{n}a_{ij}x_j - s_i = b_i\\
\end{gather}
$$

+ $s_i$ es una **variable más**: Normalmente no pondremos s sino $x_i$ donde i será la siguiente variable usable. 

+ Si una variable de decisión $x_i$ **puede tomar valores negativos** se pone entonces como la diferencia de dos variables no negativas restringidas: 

$$
x_i = x'_i − x'_i , x'_i , x ''_i ≥ 0
$$
+ Para modelar una condicion condicional usamos el siguiente [[1727968107 - Expresiones condicionales en programación lineal|método]].

+ Para convertir una restricción definida por un igual en otras definidas a partir de inequaciones realizamos la siguiente transformación:
  
$$\sum_{j=1}^na_{ij}x_j=b_i \Rightarrow $$

$$
\begin{gather}
\sum_{j=1}^na_{ij}x_j\leq b_i\\-\sum_{j=1}^na_{ij}x_j\leq-b_i
\end{gather}
$$

  
## Resolución de problemas lineales reales: 
Los ejercicios de programación lineal se resuelven a trozos:
1. Primero se debe de [[1726759568 - Creación de modelos en programación lineal|crear un modelo]] que contenga la función objetivo, restriciones y variables. 
2. Una vez creado el modelo debemos de aplicar un método para resolverlo. 
	+ [[1726835656 - Method - Resolución gráfica de modelos lineales|Method - Resolución gráfica de modelos lineales]]
	+ [[1727270270 - Method - Algorithm - SIMPLEX|SIMPLEX]]

### Creación de informes: 
Una vez terminado un problema de programación lineal, tanto el problema primal como el dual hemos de crear el informe que de información analizada de los resultados obteneidos: 
+ [[1729087121 - Creación de informes en programación lineal|Creación de informes en programación lineal]]

## Resolución de problemas lineales ENTEROS:
Cuando resolvemos problmeas lineales podemos querer que los valores que tomen $x_i$ sean enteros, en estos casos estaremos trbajando con un problema de programación lineal entera. Usamos los siguientes métodos para resolverlos: 
+ [[1729088215 - Method - Ramificación y acotación en profundidad|Method - Ramificación y acotación en profundidad]]
******
[^1]: El símbolo de igualdad con el triángulo encima significa igual **por definición.** Es matemáticamente un **axioma.**

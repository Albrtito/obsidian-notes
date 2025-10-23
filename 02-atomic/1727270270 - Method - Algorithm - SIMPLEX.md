---
id: 1727270270 - Method - Algorithm - SIMPLEX
aliases:
  - Method - SIMPLEX
  - SIMPLEX
  - Algorithm - SIMPLEX
tags:
  - heuri
sr-due: "2024-11-23"
sr-ease: 130
sr-interval: 1
---
# Method - SIMPLEX:

> [!NOTE] Definition: 
> El método simplex se usa para **econtrar soluciones a problemas lineales**. Para ello, recorre las aristas de la región de soluciones factibles buscando puntos que resuelvan el problema. 
> Una vez encontrado un punto comprueba si existe algún otro punto con el que se consiga una mejor solución (la solución será un valor mayor para la función objetivo), si existe lo busca, en caso contrario finaliza habiendo encontrado 

**Remark:**
+ Aunq esta nota recoge los pasos a seguir y la realización. Para realmente saber hacer simplex mirar [[1728047794 - Ejemplos SIMPLEX|Ejemplos SIMPLEX]], en los que se explica con ejemplos y detenidamente cada paso. 
	
Si representásemos lo que hace el algoritmo en un plano bidimensional veríamos que se van encontrando soluciones hasta llegar a la solución óptima.
![[1727270270 - Method - SIMPLEXj.png|center|350]]

> [!quote] Remember: 
> Recordemos que un problema lineal en forma estandar está definido de la siguiente forma:
> $$\begin{gather}
> f: \max z = C^T x\\\\
> \text{sujeto a: } Ax = b\\\\
> \text{con: } x \geq 0
>
>\end{gather}$$

***
## Nomenglatura:
Las nomenglatura básica del simplesx, para no perderse entre tanto vector, matriz y algebra.

+ **z:** Valor de la función objetivo. **z’** es lo mismo pero teniendo en cuenta que ha sido transformada de minimización a maximización.
+ **x** → **Vector**: Vector de incógnitas/variables, al darle valor a estas incógnitas/variable encontramos posibles soluciones.
+ **$C^T$ → Vector**: Vector de coeficientes de las incógnitas/variables. Se transpone para que se obtenga una solución no vectorial (z).
+ **A → Matriz:** Matriz de costes. Creada por los coeficientes de cada variable en cada una de las restricciones.

  >ej: Para un problema con restricciones
  > $$\begin{gather} x_1 + x_2 + 4x_3 = 2 \\ 2x_1 -3x_2 + x_3 = 3\end{gather}$$
  > Tendremos la matriz A: 
 >$$\begin{pmatrix} 1 & 1 & 4 \\ 2 & -3 & 1\end{pmatrix}$$
  
  
+ **$B_i$ → Base(Matriz)**: Base que se usa en la iteración i del simplex. Compuesta por  coeficientes de las variables en la matriz de costes(A)

  > ej: (Siguiendo con el ejemplo anterior) Una base creada por las variables $x_1$ y $x_3$ sería:
>$$B=\begin{pmatrix} 1 & 4 \\ 2 & 1\end{pmatrix}$$
  
  
+ **$C_{B_i}$ → Vector**: Vector de coeficientes reducido, solo tendrá aquellos coeficientes de las variables que componen la base $B_i$.
	+ $C_B^T$ → **Vector:** Este mismo vector pero transpuesto
***
## Pasos:

Una vez tenemos **el problema en [[1727270366 - Forma estandar|Forma estandar]]**

### Base y solución:
1. Definimos una base con la que realizar la iteración. 
   + En la **primera iteración** escogeremos las variables que permitan crear la **matriz identidad** como base. 
     + Si no existen estas variables **crearemos una variable artificial que permita la creación de la identidad**. Esta variable artificial tendra un coeficiente negativo y suficientemente grande (al menos igual a la suma de todos los coficientes de las incógnitas.)

2. Calculamos el **valor de la función objetivo** para esa base. 
   1. Calcular el **valor de cada incógnita como el vector $x_B$:** Estos valores serán una **solución factible** 
      $$x_B = B^-b$$
      - **Remark:** Las variables que no aparezcan en la base tomarán un valor de 0.
	2. Calcular el **valor de la función objetivo:**
	   $$z = C_B^T \cdot x_B$$

### Regla de entrada:

3. ==**Regla de entrada:** En este paso calcularemos cual de las variables que no se encuentra en la base aporta mas entrando en ella. Esto lo sabremos calculando:==
   $$\min \{z_j-C_j\}$$
   + Donde: 
	  $$z_j = C_B^Ty_j \rightarrow y_j = B^-A_j$$
   Entonces la j para la que se obtenga el minimo valor de esta expresión será el índice de la variable que entra $x_j$

   + Probamos **solo con las variables que no están ya dentro de la base**
   + **Una variable que acaba de salir no va a volver a entrar,** pero podemos calcular igualmente el valor de la exprsión para asegurarnos de que da positivo. (si da positivo significa que estamos haciendo las cosas bien)

	**CONDICIÓN PARA IR AL PASO 4:**
	+ **HALT:** Si todas las variables toman valores positivos la solución actual será la final y óptima. En este caso también se ha de cumplir que **todas las variables artificiales toman valor 0**
		  
	+ **CONTINUE:** En cuanto una de las variables tome valor negativo pasamos al paso 4

### Regla de salida:

4. **Regla de salida:** En este paso calculamos que variable de las que están en la base tiene que salir para que la variable que encontramos en el paso 2 entre. Saldrá la variable que cumpla: 
   $$ \min\{\frac{x_{i}}{y_{ji'}}\} \forall i \in B$$
#duda: Pq importa el orden de las variables $x_i$ → Esto es lo que significa coger la variables i’ verdad?
   + Aquí $y_{ji}$ se refiere a la posición i (incrementando empezando en 1, por eso lleva la prima) del vector $y_j$ calculado en el paso 2
   + $x_i$ será el valor de la incognita para la solución factible propuesta en esta iteración.

**IR AL PASO 1:**
    + Decidida cual es la variable de entrada(paso 2) y cual es la de salida (paso 3) se vuelve al paso 1 con la nueva base. 
      **Recomendación:** En la nueva base poner las variables en orden según su i.

***

**HERRAMIENTAS:**
+ Se puede usar la herramienta [[1729586318 - Tool - Gilp|Tool - Gilp]] para visualizar resoluciones del simplex en hasta 3 dimensiones.

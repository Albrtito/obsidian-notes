---
aliases:
  - Ejemplos SIMPLEX
tags:
  - heuri
References: 
cssclasses:
---
# Ejemplos SIMPLEX
Ejemplos del algoritmo  bien resueltos (con seguidad  de que no hay errres). Se imlementa el algorimo [[1727270270 - Method - Algorithm - SIMPLEX|SIMPLEX]]
## Ejemplo clase magistral:

$$
\begin{gather}
\max z = 2x_1 - 3x_2\\\\
\text{Restricciones:}\\
-x_1 + x_2 \leq 2\\
x_1 + x_2 \leq 4\\
x_1 - 2x_2 \leq 1\\
x\geq 0
\end{gather}
$$

**SIMPLEX:**
Antes de empezar con el algoritmo hemos de pasar el problema a forma estandar: 

Aplicamos las [[1726759457-programacionlineal#Transformaciones|transformaciones necesarias]]. En este caso **eliminando las desigualdades**
$$
\begin{gather}
\text{Restricciones:}\\
-x_1 + x_2 + x_3 = 2\\
x_1 + x_2 +  x_4 = 4\\
x_1 - 2x_2 + x_5 = 1\\
x\geq 0
\end{gather}
$$
+ A la hora de realizar este tipo de ejercicios, **separar por columnas para evitar errores.**
+ Las variables que “nos importan” son $x_1$ y $x_2$. El resto son variables de holgura, auxiliares, útiles solo para la resolución.

**Obtenemos los siguientes valores para $C^T$, C, A y b**
$$
\begin{gather}
C^T = (2,-3,0,0,0)\\\\

X = \begin{pmatrix}
x_1\\x_2\\x_3\\x_4\\x_5
\end{pmatrix}
\\\\

A = \begin{pmatrix}
-1 & 1 & 1 & 0 & 0\\
1 & 1 & 0 & 1 & 0\\
1 & -2 & 0 & 0 & 1\\
\end{pmatrix}
\\\\

b = \begin{pmatrix}
2\\4\\1
\end{pmatrix}
\end{gather}
$$
**Remarks:**
+ Vease que se añaden columnas en A para las variables de holgura. 
+ Se añaden **coeficientes en C para las variables de holgura**



### Primera iteración:

   
1. **Cálculo de las variables básicas:** 
Creamos una solución factible básica utilizando la base  $B_0 = I_{3x3}$. Esta base la generamos utilizando únicamente las columnas para variables $x_3, x_4, x_5$. 
	   $$
		B_0 = I_3= \{x_3,x_4,x_5\} =
		
		\begin{pmatrix}
		1 & 0 & 0 \\
		0 & 1 & 0 \\
		0 & 0 & 1 \\
		\end{pmatrix}
	  $$

Esta nueva base nos genera una solución factible básica que obtenemos resolviendo la equación algebráica. 
	  
$$
	  B_0 x_{B_0} = b
$$
Entonces:
$$
	  x_{B_0} = B_0^- b = (0,0,2,4,1)^T
 $$

1.1.  **Obtener valor de la función objetivo**: 

Calculamos el valor de la función objetivo con las variales básicas obtenidas. 

Aplicamos directamente la definición del problema lineal.
	$$ z_{B_0} = C_{B_0}^T X_{B_0} = (0,0,0)(2,4,1)^T = 0$$
Este primer punto que hemos encontrado será la **primera solución del problema lineal**. Esta solución estará en el punto: (0,0,2,4,1), aunq para obtener la solución bidimensional solo nos quedamos con las primeras dos variables, obteniendo (0,0)

	
> [!check] Duda: **Como es que obtenemos la solución multiplicando por la base y no por A?** 
>La base se obtiene directamente desde A, es un trozo de la matriz A (matriz de costes). Al utilizar solo m (3 en este caso) columnas de la matriz asumimos que el valor para las variables de las otras n columnas (en este caso 2) es 0.




2. **Regla de entrada:** 
Utilizamos el subindice i para referirnos a las variables básicas. Mientras que se usa el subindice j para las variables nuevas que entren(variables no básicas)

> [!NOTE] Regla de entrada:
> Ahora que hemos obtenido una posible solución tenemos que comprobar si esta solución **mejorará en caso de que introdujamos alguna otra variable**. 
> 	

**Remarks:**
En este ejemplo se va a explicar **como se obtiene el método que utilizaremos:**

Actualmente la forma en la que estamos calculando la función objetivo (su valor) es la siguiente.
$$ z = \sum_{i\in B} C_i X_i$$
 En el paso uno las nuevas variables eran 0 y no teníamos que tenerlas en cuenta, introducimos una nueva variable de aquellas que noeran básicas y comprobamos si el valor de la función objetivo aumenta. 

$$ z = \sum_{i\in B} C_i \hat X_i + c_j \sigma $$
+ **sigma:** Es la variable nueva.
+ $c_j$: Es el coeficiente de la variable nueva


> [!bug] Problema: 
> Al añadir una nueva variable con otro coeficiente la función objetivo z no puede mantenerse con el mismo valor. 
> $$
> \sum_{i\in B} C_i X_i = \sum_{i\in B} C_i \hat X_i + c_j \sigma 
> $$


> [!check] Solution:
> Se marca a las variables X con un sombrerito. Esto quiere decir que se **acomodan, cambiando su valor para que la igualdad se mantenga** 

+ Obtenemos el valor de una variable acomodada como el siguiente:

$$ \boxed{\hat x_i. = x_i - \sigma y_{ji'}}$$
#duda: Como se obtiene el coste reducido a través de la definición de una variable básica acomodada.

**Utilizando esta nueva definición obtenemos el coste reducido de una nueva variable no básica.**
$$z - \sigma(z_j - c_j)$$
+ El objetivo será **minimizar este coste**, queremos encontrar el máximo valor negativo (**el mínimo de los costes reducidos**)

Para cada variable no básica que podamos introducir a la base tendremos que calcular su coste reducido y compararlos. 

**En este caso:**
Tenemos dos opciones, una por variable nueva: 
$$z_1 - c_1 = C_B^Ty_1 - C_1 = -2$$
$$z_2 - c_2 = C_B^Ty_2- C_2 = 3$$

El mayor número negativo será -2 así que **incluimos a $x_1$ en la base** y pasamos al siguiente paso. 

3. **Regla de salida**:

> [!bug] Problema:
> Ahora el problema es que tenemos **una variable de más en la base** 


> [!check] Sol 
> La solución obvia, **saquemos la variable que peor nos venga de la base.**  

Este problema se representa en que tenemos una base tridimensional igualada a otra cuatridimensional. 
  $$a_3x_3 + a_4x_4 + a_5x_5 = a_3\hat x_3 + a_3\hat x_3 + a_3\hat x_3 + a_3\hat x_3 + a_1 \theta$$

Resolvemos la equación algebráica: 
#duda: Cooooomo? Necesito una explicación de esto tmb
$$ B_0 y_1 = a_1$$ 
Y obtenemos la igualdad: 
$$ \boxed{a_1 = a_3y_{11} + a_4y_{12} + a_5y_{13} }$$

Lo que nos permite reformular utilizando la nueva definicón de a1:

$$a_3x_3 + a_4x_4 + a_5x_5 = a_3(\hat x_3 + \theta y_{11}) + a_4(\hat x_4+ \theta y_{12})  + a_5(\hat x_5 + \theta y_{13})$$
Que podemos simplificar como: 
$$x_i = \hat x_i + \theta y_{ii'}$$
Y de aquí obtenemos el cambio de valor para la variable de decisión: 
	
	$$\hat x_i =  x_i - \theta y_{ii'}$$
Acotando este valor como **no-negativo** podemos obtener: 
	$$ \theta \leq \frac{x_i}{y_{ji`}}$$
Entonces, si nuestra restricción es que las variables sean mayores de 0, al intentar sacar una variable podemos ver si la que quitamos nos crea un valor negativo y denegarla.
La variable que tendremos que saar será con la que se obtenga: 
$$\boxed{min_{i\in B}\{\frac{x_i}{y_{ji'}}\}}$$
+ Mientras que sea **mayor o igual a 0**
+ Si nos encontrásemos con un caso en el que todos los valores son negativos significaría que la región no esta acotada, esto simplemente no pasa con un buen modelo. Te faltan restricciones.

En el ejempo que estamos haciendo ahora mismo obtenemos: 
$$min\{\frac{2}{-1}, \frac{4}{1},\frac{1}{1}\}$$

### Segunda iteración:
Para la segunda iteración hemos sacado de la base a $x_5$ e incluido la variable $x_1$. La base que utilizaremos será: 
	$$ B_1 = \{x_1, x_3, x_4\} = \begin{pmatrix}
-1 &&1 &&0 \\ 1 && 0&& 1 \\ 1&& 0&& 0
\end{pmatrix} $$
A partir de aquí repetimos los pasos. 




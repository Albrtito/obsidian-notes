---
aliases:
  - Expresiones condicionales en programación lineal
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-11-23
sr-interval: 1
sr-ease: 130
---
# Expresiones condicionales en programación lineal

> [!NOTE] Definition: 
> Cuando nos encontramos con expresiones del tipo: 
> 
> > **Si variable1 es mayor que 20 entonces pasa algo**
>
> tenemos ante nosotros una **expresión condicional.** 

> p.e: $$x_i < a \rightarrow b=1$$
> $$x_i \geq a \rightarrow b = 0$$
```python
if x <a:
	then b = 1
	else b = 0
```

![[1727968107 - Expresiones condicionales en programación linealj.png|center]]
+ Para modelizar este tipo de restricciones utilizaremos el **método BIG-M**

Con este método queremos crear una restricción para el caso 1 y otra para el caso 2 de forma que se cumpla: 

+ $x<a \rightarrow b = 1$
+  $x\geq a \rightarrow b = 0$

Las restricciones que podemos crear para cada caso varían. Pero cada restricción deberá de asegurar que **obliga a b a tomar un valor (0 o 1) y en el caso contrario la restricción se queda unbounded**

Hay dos formas de crear estas restricciones:
1. Primera forma:
   + Utilizar la desigualdad 1 para forzar b = 0 si x > a y  b = {0,1} si x < a
   + Utilizar la desigualdad 2 para forzar b = 1 si x < a y b ={0,1} si x > a
2. Segunda forma: 
   + Utilizar la desigualdad 1 para forzar: b = 1 si x < a y b = {0,1} si x>a
   + Utilziar la desigualdad 2 para forzar b = 0 si x >a y b = {0,1} si x < a


Manteniendo el caso de prueba podemos crear dos restricciones: 
+ **Para el caso 1:**
  $$
  x < a + M(1-b)
   $$
+ **Para el caso 2:**
  $$
  x \geq a - Mb
   $$
Podemos comprobar que: 
1. En la primera restricción: 
   + Si x < a => b = 0
   + Si x > a => b = 
2. En la segunda restricción: 
   + b = 0 => x ≥ a 
   + b = {0,1} => 

El único problema que nos quedaría por resolver es que necesitamos que todas las restricciones sean válidas para una [[1727270366 - Forma estandar|Forma estandar]] de un problema de programación lineal. → Solo restricciones de tipo ≥, ≤, =
Para resolverlo se añade/substrae un valor infinitesimalmente pequeño. Manteniendo el caso anterior debemos de cambiar la restricción para el caso 1 a: 
$$
x \leq a + M(1-b)-\epsilon
$$
***

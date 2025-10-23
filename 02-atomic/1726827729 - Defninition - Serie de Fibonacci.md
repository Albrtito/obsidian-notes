---
aliases:
  - Defninition - Serie de Fibonacci
  - Serie de Fibonacci
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-03
sr-interval: 48
sr-ease: 290
---
# Serie de Fibonacci

> [!NOTE] Definición 
>  La serie de fibonacci se define como la [[Recurrence relations|relación de recurrencia]]: 
>  $$
>  a_n = a_{n-1} + a_{n-2}
>  $$ 
>  + Donde: $a_0 = 0: a_1 = 1$

## Implementación de la serie:
A la hora de codificar la la serie para obtener el resultado de F(n) existen varios métodos: 
### Recursividad:
Usando la implementación básica: 
+ **Implementación básica:**
	```c
	long fibonacci_0 (int n)
	{
	if (n == 0) return 0;
	if (n == 1) return 1;
	return fibonacci_0(n-1) + fibonacci_0(n-2);
	}
	```
+ Evaluamos casos más de una vez, por ejemplo, para F(4) se evalúan F(4-1) y F(4-2) que a su vez vuelven a evaluar F(4-2). 
+ La cantidad de evaluaciones es **exponencial**. 

Podemos utilizar programación dinámica para resolver este problema, **almacenando valores intermedios**.
### Recursividad con memoria:
+ **Implementación almacenando valores:**
	```c
	list f;
	long fibonacci_aux (int n) {
	  if (f[n] == UNKNOWN)
	    f[n] = fibonacci aux(n - 1) + fibonacci aux(n - 2);
	  return f[n];
	}
	long fibonacci_1 (int n) {
	  int i;
	  f[0] = 0;
	  f[1] = 1;
	  for (i = 2; i≤n; f[i++] = UNKNOWN)
	    ;
	  return fibonacci aux(n);
	}
	```
+ Tenemos una tabla/lista de valores f en la que guardamos el valor de la serie fibonacci para cada n. 
+ Comprobamos si sabemos ya el valor para fibonacci(n) para no volver a calcularlo. 

Se puede optimizar aún más con programación dinámica, sin necesidad de usar siquiera una tabla o recursividad.
### Programación dinámica:
+ **Implementación usando programación dinámica:**
	```c
	long fibonacci_2 (int n)
	{
		int i,z;
		int x = 0;
		int y = 1;
		if (n<2)
			return n
		for (i =2; i<= n; i++)
		{
			z = x + y;
			x = y;
			y = z; 
		}
		return z;
	}
	```
+ En vez de calcular cada valor “hacia abajo” lo hacemos de abajo hacia arriba. Vamos calculando valores empezando desde los dos primeros (0 y 1) hasta que llegamos al valor deseado. 





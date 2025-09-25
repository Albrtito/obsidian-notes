---
aliases:
  - Algorithm - Profundizacion iterativa
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-26
sr-interval: 19
sr-ease: 228
---
# Algorithm - Profundizacion iterativa

> [!NOTE] Intro: 
> + Algoritmo basado en [[1732114607 - Algorithm - Primero en profundidad|Algorithm - Primero en profundidad]]
> Hacer exploraciones en profundidad a $d_{max}$ que se incrementea en $k$ entre iteraciones. 
> > Cuando no encuentro una solución, voy más abajo. Aumento mi profundidad máxima. 

## Pseudocódigo: 
1. Realizo un algoritmo de primero en profundidad con un valor para $d_{max}$ 
2. Compruebo si se ha encontrado solución: 
	+ Si se ha encontrado solución → **HALT**
	+ Si no se ha encontrado solución → **Incrementar $d_{max}$ en $k$ ** y volver al paso 1.
	

## Propiedades:
**Admisibilidad y completitud:**
+ Este algoritmo **es completo** pues siempre se encontrará una solución. 
+ El algoritmo es **admisible** si y solo si: 
	+ El valor para **k es igual a 1**
	+ El valor **inicial para $d_{max}$ debe de ser 1**
	+ Los costes son unitarios

## Eficiencia: 
La eficiencia va a ser la misma que en la búsqueda en primero en profundidad. 
+ b →  Factor de ramificación
### Tiempo: 
$$
O(b^d)
$$
### Memoria: 
$$
O(bd)
$$
En caso de usar **lazy evaluation**
$$
O(d)
$$


> [!check] Duda: Por que no nos quedamos con el arbol anterior
> Porque entonces tenemos que **guardar el arbol anterior** y por memoria esto no sera eficiente.  


***
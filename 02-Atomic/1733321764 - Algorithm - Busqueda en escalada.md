---
aliases:
  - Algorithm - Busqueda en escalada
  - Algoritmo Hill-Climbing
  - Algoritmo de busqueda H.S
  - H.S.
tags:
  - incomplete
  - heuri
References: 
cssclasses:
---
# Algorithm - Busqueda en escalada

> [!NOTE] Intro: 
>  Para introducir este algoritmo lo presentaremos con: 
>  + Un **factor de remificación regular**. 
>  + Los costes no serán unitarios. 
>  + Asumimos que todas las funciones heurísticas que usamos son consistentes
>  + Por defecto siempre minimizamos
>    > Elegimos el nodo más prometedor y descartamos el resto
>    > + Elegimos el nodo más prometedor y descartamos el resto

+ Se utilizan en casos de tener un **factor de ramificación muy alto** 
## Propiedades: 
+ **Completo:** → NO
   La heurística puede equivocarse y saltarse la solución
+ **Admisible:** → NO
  Si no es completo no es admisible
## Eficiencia: 
+ **Memoria** : Utilización de memoria constante pues solo guardamos el nodo actual en el que estamos. 
  Como también tenemos que guardar el camino que hemos encontrado guardaremos un número igual a la distancia del camino en un vector: 
  $$
  O(d)
  $$
+ 


***
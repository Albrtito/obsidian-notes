---
aliases:
  - Segunda práctica de heurística
tags:
  - heuri
References: 
cssclasses:
---
# Segunda práctica heuristica

## Evaluación:
+ **Satisfabilidad lógica: (CSP)**: 4p
+ **Búsqueda:** 6p 

## Forma de entrega:

> [!Attention] Como expresar restricciones: 
> Las restricciones y dominios se deben de seguir definiendo de forma algebráica y lo más generalizadas posible.  

## Búsqueda: 
### Búsqueda espacio de estados: 
+ Los diferentes estados se pueden crear usando objetos (creando clases)
	+ Los estados se **representan con contenido semántico**
+ Los operadores toman la forma de funciones/métodos. 
```c
if <condition>
	then <efectos>
```

+ **Creación de funciones de adyacentes:** Dado un estado la función devuelve sus estados sucesores(de un nodo loa adyacentes). `función descendants` 
	+ Esta función **expande un nodo**
	  

***
---
aliases:
  - Funciones hash
  - Funciones resumen
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# Funciones hash

> [!NOTE] Definición: 
> Haceptando un bloque de datos 

+ **Solo se cumple la propiedad de integridad**
+ **No se cumple** la propiedad de **confidencialidad**
+ Debe de poder resumirse **cualquier longitud de mensaje de entrada**
+ Los resúmenes son de **longitud fija**


> [!BUG] Problema: Colisiones 
> Al ser el espacio de mensajes mucho mayor al espacio  

## Pseudoaleatoriedad
Las funciones hash han de cumplir las siguientes propiedades de **pseudoaleatoriedad basadas en [[1726507033 - Entropía y aleatoriedad|Entropía y aleatoriedad en criptografía]]**

+ **Difusión:** Cambio de 1 bit cambia al menos el 50%
+ **Determinista:*
+ **Eficiencia:**

## Resistencia a preimagen:
**namely:** Propiedad de **una sola via**. 

Se debe de poder ir solo en una dirección de la función. No se debe de poder encontrar un mensaje a partir del resumen de dicho mensaje.

## Resistencia a segunda preimagen:
**namely:** Resistencia debil a colisiones

No debe de poder haber **dos mensajes con el mismo resumen**.


## Resistente a colisiones:
Es imposible encontrar **dos mensajes de nuestra elección** que tengan el mismo hash.

## Ataques de fuerza bruta:

> [!NOTE] Propiedad:
> Una función resumen **solo debe de permitir ataques por fuerza bruta**, no debe de permitir **que se realice análisis criptográfico.**
+ Si se permite ataques por otros medios distintos a la fuerza bruta el **algoritmos se considera debil/roto** y no será válido
+ Se atacará a las tres propiedades de resistencia de la función
### Probabilidades:
Las probabilidades de encontrar colisiones usando distintos ataques de fuerza bruta son:

1. **Preimagen:** $1\over 2^n$
2. **Segunda preimagen:** $1\over2^n$ 
3. **Ataque de colisión:** $1\over 2^{n/2}$ → Ataque del cumpleaños

Siendo n la longitud del hash.
 
**Remark:**
Como la manera más facil de atacar va a ser el ataque por colisión, esta propiedad es la que **marca como de seguro es el sistema**

## Estructura y funcionamiento de una función Hash:

La mayoría de funciones hash actuales utilizan la **estrucrtura MERKLE-DAMGÄRD**
![[1728307154 - Funciones hashj.png]]

## Ejemplos reales:
Tenemos dos familias principales de funciones hash, la familia de las funciones MD ([[1728308824 - Algorithm - MD5|MD5]])) y las funciones [[1728309243 - Algorithm - SHA|SHA]] 
+ A la familia de las MD **ya se les ha encontrado debilidades y todas están rotas**
+ En las sha **exiten 6 tipos** numerados del 0 al 3. **Se han encontrado debilidades en los tipos 0 y 1**. Los tipos más usados hoy en día son el 2 y el 3.


***

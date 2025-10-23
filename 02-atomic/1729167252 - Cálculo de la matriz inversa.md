---
aliases:
  - Inverse matrix
  - Calculo de la matriz inversa
tags:
  - heuri
  - algebra
References: 
cssclasses: 
sr-due: 2025-01-28
sr-interval: 70
sr-ease: 290
---
# Cálculo de la matriz inversa

> [!NOTE] Intro: 
> El cálculo de la matriz inversa es algo fundamental en gran casi todos los procesos complejos e programación. 
> Hacer este cálculo **rápido** es aún más complicado y uno de los problemas de optimización más importantes: 


> Si un informático quiere hacerse millonario solo tiene que aprener a calcular inversas muy rápido 
> - Carlos linares


Conocemos varios métodos para realizar este cálculo que se expondrán a continuación. 

## Necesidades: 
Para que una matriz A tenga inversa debe de:
+ **Tener determinante distinto de 0**
+ **Ser cuadrada (nxn)**
## Calculo por determinatnes y adjuntos: 

El método que se utiliza para hacer cálculos a mano desde el primer momento en el que te cuentan lo que es una inversa. 

$$
A^- = \frac{1}{|A|}(Adj(A))^T
$$
+ Donde $Adj(A)^T$ es la [[1729168096 - Matriz adjunta|Matriz adjunta]] de A transpuesta.
## Otras formas: 

Este método no es el que utilizamos computacionalmente para realizar calculos de forma eficiente, en esos casoa existen descomposiciones de la matriz A que permiten calcular la inversa más rápido.


***

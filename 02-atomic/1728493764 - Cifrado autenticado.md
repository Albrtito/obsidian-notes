---
aliases:
  - Cifrado autenticado
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# Cifrado autenticado
Utilizando tanto las funciones [[1728309909 - MAC|MAC]] como el cifrado del texto podemos generar lo que llamamos **cifrado autenticado**, este cifrado puede ser generado de distintas formas. 

+ **Encript-then-MAC**: Encriptamos y luego creamos la MAC **utilizando el texto cifrado**. 
  + Prefe del profe
+ **Encript and mac**: Se encripta y se crea la mac al mismo tiempo
+ **MAC-Then-Encrypt:** Calculamos la MAC, luego **ciframos el texto y la MAC juntos**
	+ Tenemos que descifrar antes de nada

## Modos de operación:
Para generar el MAC podemos utilizar los propios modos de opración del [[1726493246 - Algorithm - AES|AES]]. En concreto utilziaremos el **modo contador**. 

***

---
aliases:
  - Sustitución monoalfabeto monográfica
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2024-12-13
sr-interval: 52
sr-ease: 269
---
# Sustitución mono-alfabeta monográfica

> [!BUG] Problema: 
> Con este tipo de cifrados siempre vamos a obtener el mismo problema: Las probabilidades de cada uno de los caracteres cambiados encajarán con las del alfabeto conrrespondiente. 
> 


## SUMAS: Cifrador de ==desplazamiento== puro(ROT):

Es aquel cifrador que utiliza una función del tipo: 
$$
\boxed{C_i = (m_i \pm b) \mod n}
$$
Cada uno de los caracteres es desplazado dentro del propio alfabeto. 
+ b: Constante de desplazamiento. (Sería la clave del sistema)
**Remarks:**
+ ROT → Rotación

> p.e:
	**El cifrador Cesar:**
	Un ejemplo de este cifrado sería el **cifrado cesar**, que **desplaza** el grafo dentro del alfabeto una cantidad de posiciones. 
	En este tipo de cifrado cada grafo **siempre se sustituye** por el mismo grafo-cifrado. → Solo hay un alfabeto transformado (**Mono-alfabetismo**)



## MULTIPLCACIONES: Cifrador de ==decimación== pura:
Es aquel que utiliza una multiplicación para variar el alfabeto y transformarlo en un alfabeto cifrado. 
$$
\boxed{C_i = (a \times m_i) \mod n}
$$
+ a: Clave de cifrado. Constante de decimación

### SUMA + MULTIPLICACIÓN: Cifrador por sustitución afín
Se realizan ambas la suma y multiplicación. En este caso tanto b como a serán claves del cifrado.
$$
\boxed{C_i = (a \times m_i + b) \mod n}
$$

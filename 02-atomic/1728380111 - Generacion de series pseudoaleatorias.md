---
aliases:
  - Generacion de series pseudoaleatorias
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# Generacion de series pseudoaleatorias

> [!NOTE] Intro
> Crear series aleatorias require la medición de elementos naturales, esto es algo muy complicado y dificil de hacer así que the next best thing ha sido la generación de series que **simulan ser aleatorias**. 
> 
> Para generar estas series necesitamos:
> + Un generador de números aleatorios
> + Una **clave base**

## Propiedades
Al crear una serie de estas características definimos una serie de propiedades deseables que se han de cumplir.

+ En primer lugar los [[1728380472 - Postulados de Golomb|Postulados de Golomb]]
+ ==El periodo de la serie será **lo más grande posible**==
+ ==La serie estará distribuida uniformemente==
+ ==La serie sera **impredecible**: esto se mide usando la [[1728381283 - Complejidad lineal de una serie cifrante|Complejidad lineal de una serie cifrante]]==

## PRNGs:
![[1728381448 - PRNGs|PRNGs]]


***

---
aliases:
  - Postulados de Golomb
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2024-11-30
sr-interval: 28
sr-ease: 230
---
# Postulados de Golomb

> [!NOTE] Intro: 
> Golomb crea una serie de postulados que **definen cualidades deseables que han de tener las series pseudoaleatorias**
> 

Estos postulados dicen lo siguiente: 

Para que una serie(k) pseudoaleatoria sea buena…

1. Debe de existir el **mismo número de ceros que de 1s**. Se acepta una diferencia igual a la unidad

2. La mitad de las rachas ha de tener longitud 1, la cuarta parte longitud 2, la octava long 3, etc.
   + Llamamos **racha** a la sucesión de dígitos iguales

3. Para todo k, **la autocorrelación fuera de fase ha de ser** **constante**
   + LLamamos autocorrleación a la función que realiza un desplazamineto de la secuencia hacia la izquierda y **compara los aciertos/fallos entre la sequencia sin desplazar y la secuencia desplazada**.
     ==$$AC(k) = (A-F) / T$$==
     + A: Aciertos al mover la serie
     + k: Movimientos que realizamos(desplazar una vez,dos veces,etc.)
     + F: Fallos al mover la serie
     + T: Longitud total de la serie (o del perodo si la serie es infinita)



***

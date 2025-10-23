---
aliases:
  - AddRoundKey
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# AddRoundKey
Se sumarán $OR$  exclusivo el estado intermedio con la clave de cada ronda. En la ronda 0 será el $OR$ exclusivo entre el texto de entrada y la clave inicial; en las rondas siguientes (p.e. 1 a 9) será el $OR$ exclusivo de las subclaves de cada ronda con la salida de la función MixColumns y en la última ronda (10) el or exclusivo de la subclave de estado 10 y la salida de ShiftRows.
***
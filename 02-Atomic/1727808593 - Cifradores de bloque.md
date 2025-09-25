---
aliases:
  - Cifradores de bloque
tags:
  - cripto
  - incomplete
References: 
cssclasses:
---
# Cifradores de bloque

Descomponen $M$ en bloques de símbolos de igual longitud tal que:
$$M = M_1, M_2, ..., M_n$$
Cifran cada bloque con la misma clave -> mapeo reversible entre texto en claro y cifrado. Nótese que el tamaño de los bloques suele ser de 64, 128 o 256 bits.

+ Imagen no importada

## Cifrador de bloque ideal

Se puede definir en una tabla de mapeo del tamaño de $2^n$ bits de texto claro y cifrado. 

>[!DANGER]
>Existen $2^n!$ posibles asignaciones de texto en claro = texto cifrado, por lo que hay un total de $2^n!$ claves posibles. **Esto es una burrada.**

Para resolver este problema, se genera un algoritmo de cifrado usando redes de permutaciones, sustituciones y/o *estructuras de Feistel*.

>[!NOTE] Estructuras de Feistel
>Diseño básico usado en cifradores de clave simétrica. Se divide el mensaje a la mitad y en una mitad se opera y en la otra no, para luego cambiarse al final de la ronda. El mensaje se itera por varias rondas (DES, predecesor de AES, usa esto)






***
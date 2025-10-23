---
aliases:
  - Definition - Criptosistema
  - Criptosistema
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2024-12-30
sr-interval: 53
sr-ease: 230
---
# Definition - Criptosistema
![[Screenshot 2024-09-13 at 4.07.14 PM.png]]
> [!NOTE] Definición: 
> Un criptosistema se compone de dos [[1726498880 - Definition - Cifrador|cifradores]] que, junto a claves generadas por un sistema de generación de claves, cifran y descifran mensajes entre dos interlocutores.

## Características: 
Las características de estos sistemas son las del método de cifrado utilizado por los cifradores y el generador de claves. 

### Técnicas matemáticas de cifrado:
Para generar cifrados se utilizan dos técnicas básicas: 
1. **Sustitución:** Modificar un carácter por otro
   + Este método sirve para crear **confusión**. 
2. **Transposición o permutación:** Redistribuir los caracteres **sin modificarlos**. 
   + Esta técnica se utiliza para difundir las características del mensaje original.
Ambos métodos realizan la operación matemática **basándose en una función/reglas**.

+ Ambas técnicas ya fueron introducidas por Claude Shanon en “Communication theory of secrecy systems(1949)”
+ Con estas técnicas tenemos que asegurarnos de que el sistema **no ha perdido información.**

### ==Sistemas simétricos y asimétricos:==
Basándonos en el número de distintas claves en un sistema de cifrado dividimos entre:
+ Sistemas **simétricos:**
  Aquellos sistemas con **una sola clave, privada y compartida**. La clave ha de ser **compartida a través de un canal privado** para asegurar la confidencialidad del sistema. Hablamos entonces de **claves privadas**
+ Sistema **asimétrico:** 
  Aquellos sistemas con **dos claves, una privada y otra pública**. La clave pública se utiliza para cifrar el mensaje y la privada para descifrar. La clave pública **puede ser compartida en un canal público.**

### Procesamiento de texto en bloque y flujo:
El texto del mensaje a des/cifrar se puede procesar en:
+ **Bloques:** Grupos de carácter, de forma secuencial.
	+ [[1727808593 - Cifradores de bloque|Cifradores de bloque]]
+ **Flujo:** De caracter en caracter, de forma continua.

## Clásicos y modernos: 
Dividimos los criptosistemas en dos grandes grupos según si pertenecen a la [[1726498694 - Definition - Criptografía#Clásica y moderna|criptografía clásica o moderna]]. 
 + [[1726753991 - Criptosistemas clásicos|Criptosistemas clásicos]]
 + [[1726754186 - Criptosistemas modernos|Criptosistemas modernos]]

---
aliases:
  - Cifrador de flujo
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2024-12-01
sr-interval: 29
sr-ease: 230
---
# Cifrador de flujo

> [!NOTE] Definición: 
> Los cifradores de flujo cifran el **mensaje(M) byte|bit per byte|bit** **realizando una opración XOR con la serie cifrante**(K).Cada elemento de la serie cifra un byte|bit. 
> $$M = m_1, m_2, m_3,m_4...$$
> $$K = k_1, k_2, k_3,k_4..$$
> + $m_i$ se cifra con $k_i$
> + La serie cifrante (K) es **idealmente infinita y aleatoria**

**Remarks:**
+ Es imposible generar una serie infinitamente aleatoria con el uso de ordenadores → Se utilizan series **pseudoaleatorias** generadas por PRNGs 

> [!CHECK] Solution: 
>  El ejemplo del cifrador de flujo **ideal** es el de [[1726497421 - Sustitución polialfabética no-periódica|Método de Vernam]], no obstante, al no poder generar series completamente aleatorias sabemos que **este cirfrador no es práctico** y debemos de preocuparnos de la [[1728380111 - Generacion de series pseudoaleatorias|Generacion de series pseudoaleatorias]].


## ==Síncrono y Autosíncrono:== 
AL ser un método de criptación síncrono, los cifradores de emisor y receptor han de ser capaces de **intercambiar la clave** cifrante. 

Cuando este intercambio se realiza de forma **externa será un sistema síncrono**, mientras que si se realiza de forma **automática será un sistema autosíncrono** 

+ #duda: Diferencias en la generación de la serie cifrante para cada uno de los casos

## Pros&Cons:
**VENTAJAS:**
+ Cifrado muy **rápido**
+ Los **errores no se propagan** (Cifrado uno a uno)

**DESVENTAJAS:**
+ Poca difusión
+ No se puede generar aleatoriedad
+ ==Problemas al reutilizar la clave.== 

### Ataques:
Se pueden realizar ataques sabiendo solo parte del sistema:
	1. **Ataque con texto original conocido:** Obtener K teniendo M yC[^1]
	   $$M\oplus C = M \oplus M\oplus K = K$$ 
	2. **Ataque solo al criptograma:** Usando dos trozos diferentes del cifrado. 
	   $$C_i \oplus C_j = M_i \oplus K \oplus M_j \oplus K = M_i \oplus M_j$$
***

[^1]: **Recordar** que las operaciones XOR se realizan en **pares**
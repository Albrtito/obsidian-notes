---
aliases:
  - Definition - Cifrador
  - Cifrador
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2025-02-26
sr-interval: 116
sr-ease: 270
---
# Definition - Cifrador

> [!NOTE] Definición: 
> Aquella máquina que cifra un mensaje usando un **método/función** y **una clave**. 
> Al mensaje transformado se le llama **cifrado**

**Remarks:**
+ El cifrador **genera un cifrado**

![[Screenshot 2024-09-13 at 3.58.36 PM.png|center]]

+ **k:** Clave
+ **C:** Mensaje cifrado
## Propiedades del cifrado:
Definimos una serie de espacios y transformaciones de cada cifrado. 
+ **Espacio de mensajes:** Cantidad de posibles mensajes que se pueden cifrar.
$$
M = \{m_1,m_2,...\}
$$
+ **Espacio de cifrados:** Posibles cifrados que se pueden generar ,dado un mensaje que pertenezca al espacio de mensajes.
$$
C = \{c_1,c_2,...\}
$$
+ **Espacio de claves:** Posibles claves a utilizar en el cifrador. 
$$
K = \{k_1,k_2,...\}
$$
+ **Familia de transformaciones de cifrado:** posibles transformaciones a realizar, utilizando una clave, a un mensaje para cifrarlo. 
==$$
e_k : m \rightarrow c
$$==
+ **familia de transformaciones de descifrado:** posibles transformaciones a realizar, utilizando una clave, a un mensaje para **descifrarlo**
$$
D_k: C \rightarrow M
$$
	+ Del cifrado(C) se obtiene el mensaje (M)

Para considerar un sistema de cifrado como válido, Kerckhoff propuso los [[1726519620 - Principios de Kerckhoff|Principios de Kerckhoff]]. 

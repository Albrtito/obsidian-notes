---
aliases:
  - Orden gaussiano
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2024-12-16
sr-interval: 27
sr-ease: 190
---
# Orden gaussiano

> [!NOTE] Definition:
> Dados dos números coprimos ( a y n) existe al menos un m tal que el resto potencial de a elevado a m sea igual a 1.
$$a^m = 1 \mod n$$
**Entonces**: 
$$\boxed{a^{\phi(n)} = 1 \mod n \rightarrow m = \phi(n)}$$
> Llamamos al **menor** m el **orden gaussiano de a con módulo n**
> + **m será normalmente referenciado con la letra w**:
> $$ a^w = 1 \mod n$$
> **Donde:**
> $$\boxed{w = orden(a,n)}$$


**Remarks:**
+ Si existe más que un solo m, entoces m ha de ser divisor de $\phi(n)$ o el propio Phi

## Generadores:
Cuando el orden gaussiano es igual al indicador de euler diremos que ese orden es **una raiz primitiva o generador** debido a que es campaz de **generar TODO EL CONJUNTO DE RESTOS de n**. 

***

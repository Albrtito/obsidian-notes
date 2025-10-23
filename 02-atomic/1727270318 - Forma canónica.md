---
aliases:
  - Forma canónica
  - Forma simétrica
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-05
sr-interval: 50
sr-ease: 290
---
# Forma canónica

> [!NOTE] Forma canónica:
> Un problema de programación lineal esta en forma canónica si: 
>+ El objetivo/función busca **MAXIMIZAR**
>+ Igualdades: **≤**
>+ Variables: **≥ 0**
>EL modelo se puede expresar de la siguiente forma:
>$$
\begin{gather}
\text{Función:}\\
\max z = c^Tx\\\\
\text{Restricciones:}\\
Ax <= b\\\\
\text{Variables:}\\
x>= 0
\end{gather}
>$$
>+ c → Vector de costes/beneficios (A obtener/reducir)
>+ b → Vector de recursos (Que delimitan)

+ Se usan estas [[1726759457-programacionlineal#Transformaciones|Transformaciones]]
	+ Mayoritariamente usamos transformaciones de multiplicación por -1 para modificar el valor de la inecuación. 
	+ Por otro lado, existe una transformación que nos interesa más que el resto, esta transformación es la que usamos para **convertir una restricción de igualdad en restricciones de tipo mayor/menor igual a**. 



***
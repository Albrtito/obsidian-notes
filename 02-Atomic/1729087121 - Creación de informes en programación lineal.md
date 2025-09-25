---
aliases:
  - Creación de informes en programación lineal
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-12-21
sr-interval: 14
sr-ease: 211
---
# Creación de informes en programación lineal

A la hroa de crear un informe de un problema de programación lineal hemos de tener en cuenta distintos datos que afectan directamente al problema: 

1. **Factible:** Si/No
2. **solución óptima:** única/infinita.
   + Hay solución si todas las variables artificiales toman valor 0
3. **z acotadad?:** Si/No
   Si tenemos o no una región cerrada.
4. **Análisis de las variables:** Importa si hay variables de holgura, esto querría decir que se podrían utilizar más recursos pero no entran a la perfección. Si no hay variables de holgura no importa:
   + No suele importar en casos de problemas binarios
5. **Recursos:**
	  1. **Coste económico de los recursos:**  Informe de las variables de holgura, ver si las hay valor que (sobra o que falta)
	  2. Informe del resultado obtenido en el cálculo del problema [[1729084911 - Dualidad en programacion lineal|dual]], es decir, **como afecta la variación en las variables principales a la función objetivo.**

***

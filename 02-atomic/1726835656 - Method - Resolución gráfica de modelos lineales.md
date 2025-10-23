---
aliases:
  - Method - Resolución gráfica de modelos lineales
tags:
  - heuri
References: 
cssclasses: 
sr-due: 2024-11-25
sr-interval: 41
sr-ease: 250
---
# Method - Resolución gráfica de modelos lineales
Una vez obtenidas las variables, función y restricciones podemos aplicar la resolución lineal para obtener la solución que maximiza/minimiza la función objetivo:

1. **Identificación de la región factible** (S): Para esto usamos las restricciones establecidas para delimitar los posibles valores para nuestras variables, pintando el modelo gráficamente.
   
2. **Obtener los puntos extremos:** Estos puntos son **las esquinas de la región factible**
   
3. **Identificar la solución:** La solución será **uno de los puntos factibles**. Para identificar que punto factible es podemos utiliza dos métodos.
    
	1. **Búsqueda del máximo** entre todos los puntos: Calcular el valor de cada uno de los puntos. Aplicar este valor a la función del problema y comparar entre el valor de la función para cada punto para obtener el máximo. 
	   
	2. **Curvas/Rectas de Isobeneficio**: Obtener la función objetivo para un valor que cumpla con las restricciones. Hecho esto “alejar” esta función a través de rectas paralelas hasta identificar el punto factible con el que se obtiene el valor máximo de f.
	   
	   + Cualquiera de estas rectas creadas al asignar un valor a z se llama **curva de isobeneficio o isocoste**. Si se pide una reprsentación gráfica de ellas se pueden unicamente pintar y analizar si coinciden con todo un lado de la región factible. → soluciones infinitas

**Remarks:**
+ Para problemas con menos de 3 variables de decisión no es imprescindible representar el problema de [[1726759457-programacionlineal#Forma canónica|Forma canónica]], **para valores mayores de 3 es imprescindible.**


> [!BUG] Problema: 
> Este método solo es util para casos que podamos representar en 2 o 3 dimensiones. El método estandarizado para n variables es el [[1727270270 - Method - Algorithm - SIMPLEX|Method - SIMPLEX]] 

## Tips: 
+ Siempre que se vea un **max, min**, apuntarlo para que no se pase ninguno. Va a ser siempre o la función beneficio o alguna de las restricciones 
> p.e: Si la región no esta completamente acotada(en resolución gráfica) puede ser por esto. 
***
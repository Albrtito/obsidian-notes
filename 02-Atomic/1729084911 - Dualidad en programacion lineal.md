---
id: 1729084911 - Dualidad en programacion lineal
aliases:
  - Dualidad en programacion lineal
tags:
  - heuri
sr-due: "2024-12-25"
sr-ease: 174
sr-interval: 18
---
# Dualidad en programacion lineal
Existe algún problema en programación lineal relacionado directamente con el problema que se esta intentando resolver. 

Definimos la **forma simétrica de un problema de programación lineal** igual que la forma canónica: [[1727270318 - Forma canónica|Forma simétrica]] 
+ La simétrica y la canónica son la misma

Llamamos **forma primal** al problema original del que se obtendra finalmente la forma dual. 
Entonces podemos definir la **forma dual de un problema de programación lineal como:**


> [!ATTENTION] Examen: 
> + En los examenes se suele pedir esto como **la contribución por unidad de recurso de la función objetivo**
>   
> + Cuando en examen se pregunta por un análisis de estos problemas (y en general para dar un informe de un problema de este estilo) se han de dar indiscutiblemente las siguientes respuestas: [[1729087121 - Creación de informes en programación lineal|Creación de informes en programación lineal]]
>   

## Forma dual:
+ Las inequaciones cambian de lado (menor o igual a mayor o igual)
+ Se transpone la matriz de coeficientes
+ Se cambia el vector de coeficientes de la función objetivo por el vector de recursos

**Remarks:**
 + El valor de la inecuación diciendo que los valores de las variables no pueden ser negativos no cambiaría pues es el único que debe de seguir cumpliéndose siempre.

Matemáticamente lo podemos definir como:
$$
\begin{aligned}
\max z& =\mathbf{c}^T\mathbf{x} \\
\text{sujeto a }& \mathbf{A}\mathbf{x}\leq\mathbf{b} \\
\mathbf{x}&\geq\mathbf{0}\\\\

\min w& =\mathbf{b}^T\mathbf{x}^{\prime} \\
\text{sujeto a }& \mathbf{A}^T\mathbf{x}^{\prime}\geq\mathbf{c} \\
\mathbf{x}^{\prime}&\geq\mathbf{0}
\end{aligned}
$$
> p.e:
> El problema: 
> $$\begin{gathered}
\text { mín } z=2 x_1+x_2 \\
x_1+5 x_2 \leq 8 \\
2 x_1+3 x_2 \leq 6 \\
3 x_1+x_2 \leq 6 \\
-x_1 \leq 0 \\
-x_2 \leq 0 \\
x_1, x_2 \geq 0
\end{gathered}$$
> Lo pasamos a forma simétrica/canónica:
> $$\begin{gathered}
\text { max } z'=-2 x_1-x_2 \\
x_1+5 x_2 \leq 8 \\
2 x_1+3 x_2 \leq 6 \\
3 x_1+x_2 \leq 6 \\
-x_1 \leq 0 \\
-x_2 \leq 0 \\
x_1, x_2 \geq 0
\end{gathered}$$
> Transformamos la forma simétrica a su forma dual:
> $$\begin{gathered}
\text { max } z'=8x_1'+6x_2' + 6x_3' \\
x_1'+ 2x_2' + 3x_3' - x_4' \geq -2 \\
5 x_1'+3 x_2' + x_3 '- x_5' \geq -1 \\
 x_i\geq 0 : \forall i \in \{0,1,2,3,4,5\} \\
\end{gathered}$$



**Remarks:**
+ Si el primal tiene una solución correspondiente a la base B, entonces 
$$x’^{*^T} = C_B^t B^-$$
Esto quiere decir que no hace falta que recalculemos todo, al estar unidos podemos obtener directamente el problema. La solución del dual se calcula directamente desde la solución del primal.
  + C → El vector de coeficientes de la base
  + B → La base de la última iteración del simplex que resuelve el problema primal

+ La solución óptima de la variable global i’esima: $X_i’^*$ es **la contribución por cantidad de recurso al crecimiento de la función objetivo**. Es decir, nos da información de como crecerá la función objetivo cuando modifiquemos nuestras variables.

$$
\begin{gather}
\min z. = 3x_1 + -2x_2\\
+4x_1  -2x_2 \leq 3\\
+5x_1  +2x_2 \leq -2\\
x \geq 0
\end{gather}
$$
***

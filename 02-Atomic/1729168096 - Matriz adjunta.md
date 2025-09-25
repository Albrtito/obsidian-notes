---
aliases:
  - Matriz adjunta
tags:
  - algebra
References: 
cssclasses:
---
# Matriz adjunta

## Definición
La matriz adjunta (adj(A)) es la transpuesta de la matriz de cofactores de A.

## Procedimiento Paso a Paso

### 1. Calcular los cofactores
Para cada elemento $a_{ij}$ de la matriz A:
- Eliminar la fila i y columna j para obtener la submatriz $M_{ij}$
- Calcular el determinante de esta submatriz $M_{ij}$
- Multiplicar por $(-1)^{i+j}$ para obtener el cofactor $C_{ij}$

La fórmula del cofactor es:
$C_{ij} = (-1)^{i+j} \det(M_{ij})

### 2. Construir la matriz adjunta
La matriz de cofactores C tiene la siguiente forma:
```
C = [C₁₁  C₁₂  C₁₃  ...  C₁ₙ]
    [C₂₁  C₂₂  C₂₃  ...  C₂ₙ]
    [C₃₁  C₃₂  C₃₃  ...  C₃ₙ]
    [ ⋮    ⋮    ⋮    ⋱    ⋮ ]
    [Cₙ₁  Cₙ₂  Cₙ₃  ...  Cₙₙ]
```



## Ejemplo para una matriz 2x2
Para una matriz $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$

1. Calcular cofactores:
   - $C_{11} = (+1)\det(d) = d$
   - $C_{12} = (-1)\det(c) = -c$
   - $C_{21} = (-1)\det(b) = -b$
   - $C_{22} = (+1)\det(a) = a$

2. Matriz de cofactores:
   $C = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}$

3. Matriz adjunta (transpuesta de C):
   $adj(A) = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$


***

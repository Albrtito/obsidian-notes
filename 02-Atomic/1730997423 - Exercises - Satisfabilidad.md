---
aliases:
  - Exercises - Satisfabilidad
  - Ejercicios satisfabilidad
tags:
  - incomplete
  - heuri
References: 
cssclasses:
---
# Ejercicios de Satisfabilidad
## Ejemplos en clase:
### CSP(Alumnos):

> [!NOTE] Enunciado:
> Seis alumnos:
> $$ (Juan, Marıa, Alfredo, Yara, Rubén y Felisa)$$ 
> 
> Están en el mismo grupo de Ingeniería del Software. **Tienen que realizar un documento dividido en tres partes haciéndolas en orden y hay que decidir quien hace cada cosa**. 
> 
> + Juan no tiene los conocimientos para realizar la primera parte.
> + Marıa solo puede participar en la tercera. 
> + Alfredo y Ruben se llevan mal y no quieren trabajar juntos
> + Ruben y Felisa insisten en trabajar en la misma parte. 
> + Ademas Ruben le deja a Yara su portatil para que haga su parte cuando el acabe. 
> 
> ¿Que parte deberıa hacer cada alumno? Reduce por arco consistencia y camino consistencia los dominios de las variables del problema y encuentra una solucion factible.
>

+ **Para la solución modelada ASUMIMOS QUE TODOS QUIEREN TRABAJAR UNICAMENTE EN UNA PARTE**

**Definición de conjuntos:**
$$ Alumnos = \{J,M.A.Y.R.F\}$$
**Definición de variables:** Se define una variable por alumno.

$x_i:$ Parte que se asigna a a cada alumno $i \in Alumnos$ 

**Definición de dominios:** Debemos de definir los dominios de todas las variables:

> [!attention] Restricciones en los dominios:
> A la hora de definir los dominios de cada variable, se deben de implementar las restricciones que actuen directamente sobre los dominios para optimizar el problema. 

+ En este caso definimos diferentes los dominios de Juan y María **aplicando directamente en el dominio las primeras dos restricciones.**
$$
\begin{gather}
D_{x_i} = \{1,2,3\} \forall i \in Alumnos \backslash \{J,M\}\\\\
D_{x_J} = \{2,3\}\\
D_{x_M} = \{3\}
\end{gather}
$$
**Restricciones:**
1. A y R distinta parte: 
   $$ X_A \neq X_R$$
2. R y F misma parte:
   $$
   X_R = X_F
   $$
3. Y después de R
   $$
   X_R \leq X_y
   $$

> [!attention] Remark: 
> Debemos también de asegurarnos de aquellas **restricciones que el enunciado no dice explicitamente:** 
> + En este caso debemos de asegurarnos de que hay al menos un alumno realizando cada una de las partes.

4. Todas las partes asignadas:
   $$ Partes = \cup_{i \in Alumnos} x_i$$

### CSP (Reinas)

---
id: 1747756890-sistemas-fiables
aliases:
  - Sistemas fiables
  - Fiabilidad de un sistema
tags:
  - #Distri
---

# Sistemas fiables
Se dice que un sistema es fiable si **cumple con sus especificaciones**. 

## Medida de la fiabilidad:
Para medir el tiempo de vida de un sistema se utiliza una variable aleatoria X junto a la función R(t), que devuelve la probabilidad de que el tiempo de vida (X) sea mayor que el tiempo t elegido.
$$
\begin{align}
R(t) = P(X>t)\\
R(0) = 1 ; R(\infty) = 0\\
\end{align}
$$
**Remarks:** 
- El estudio de la gráfica/función R(t) nos da una medida de la fiabilidad. Pero esta función no se obtiene normalmente para todo el sistema sino para cada uno de lsos componentes. 
- La fiabilidad se da en el intervalo [0,t]


### Medida de la fiabilidad de un sistema dada la de sus componentes:
> [!NOTE] Sistemas en serie:
> Dada $R_i(t)$ como la fiabilidad de un componente, entonces la fiabilidad total será el producto de todas: 
> $$
> R(t) = \prod_{i=1}^N R_i(t)
> $$

**Remarks:** 
- Los fallos de cada componente han de ser independites
- La fiabilidad del sistema total es menor que cualquiera de los componentes

> [!NOTE] Sistemas en paralelo:
> Dada $R_i(t)$ como la fiabilidad de un componente, entonces la fiabilidad total se da por: 
> $$
> R(t) = 1-\prod_{i=1}^N Q_i(t)
> $$
> Donde $Q_i(t)  = 1- R_i(t)$


> [!NOTE] Sistemas k-out-of-n:
> Estos sistemas son aquellos en los que mientras k componenets de n funcionen, el sistema funciona.
> Dada $R_i(t)$ como la fiabilidad de un componente, entonces la fiabilidad total se da por: 
> $$
> R(k,n,t) = \sum_{r=k}^{r=n}\binom{n}{r} R^r_i (1-R_i)^{5-r}
> $$
> Donde $Q_i(t)  = 1- R_i(t)$


***
### Up
- [[1747756642-sistema-tolerante-a-fallos|Sistema tolerante a fallos]]
### Down
- [[1747757386-tipos-de-fallos-en-sistemas|Tipos de fallos en sistemas]]
- [[1747758799-disponibilidad-de-un-sistema|Disponibilidad de un sistema]]


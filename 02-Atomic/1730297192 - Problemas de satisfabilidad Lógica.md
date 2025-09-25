---
id: 1730297192 - Problemas de satisfabilidad Lógica
aliases:
  - Problemas de satisfabilidad logica
  - Problemas SAT
  - SAT
tags:
  - heuri
---
# Problemas de satisfabilidad Lógica

> [!NOTE] Intro: 
> Existe una gran cantidad de problemas que podemos modelar directamente como problemas de [[20240523 - 122919 - Propositional logic|Propositional logic]], este tipo de problemas son aquellos con **condiciones lógicas** → “Si pasa x entonces y | Si pasa x también pasa y”
> En esta nota tocaremos la creación de las fórmulas y obtención de modelos para este tipo de problemas. 


> [!example] Nomenglaturas: 
> - **Expresiones atómicas:** Variables binarias que toman valores 1/0. Las llamaremos también variables
>  - **CNF** : Forma Normal Conjuntiva
>  - $\neg$ :  Negación lógica, equivalente a $\hat{x}$.
>  - $\perp$:  FALSE: Valor negativo **asignado a una variable**, cuando una variable toma este valor significa que toma un valor negativo
>  - **T** :TRUE:  Valor positivo asignado a una variable 
>  - **Conjunción lógica:** AND 
>  - **Disjunción lógica:** OR
>  - **Literal puro:** Un literal es puro en una fórmula si y solo si su negación lógica no aparece en la fórmula. 
>    > por ejemplo: $(x\lor y) \land (\hat y \lor x)$ → x es puro pues $\hat x$ no aparece en la fórmula
>   - **Tautología**: fórmula proposicional que siempre  es cierta independientemente del valor que tomen las variables.
>    > por ejemplo:  $F = x_1 \lor \overline{x_1}$
>    - **Contradicción**: algo que no puede ser cierto lógicamente (1 y 0) 
>    > por ejemplo:  $F = x_1 \land \overline{x_1}$.  

##  Fórmula:
Un problema de satisfabilidad se define por una **fórmula lógica proposicional**: 
$$
F = p \lor q \land r \rightarrow w
$$
Como trabajar con fórmulas de cualquier tipo es dificil y requeriría diferentes approaches **siempre utilizaremos la FORMA NORMAL CONJUNTIVA (CNF)** de la fórmula. 

+ Una fórmula proposicional puede ser **o verdadera (T) o falsa $\perp$**
+ En lógica proposicional se  usa $p \rightarrow q = \hat p \lor q$, **disyunción de literales**.
+ **NOTA:** Si se tiene una fórmula verdadera y se quiere añadir un nuevo literal este literal debera tomar 1 o 0 para que la fórmula sea satisfacible y el contrario para que deje de serlo. 
+ **NOTA:** Al crear la formuila siempre preferimos tener **el menor número de variables posibles** para luego poder resolverlo más facilmente con alguno de los algoritmos propuestos a continuación.
### Forma Normal Conjuntiva (CNF):
En la forma normal conjuntiva todas las cláusulas han de contener únicamente operadores de tipo OR y han de estar unidas por operadores de tipo AND:
$$F=\Lambda_{i=1}^n C_i=\Lambda_{i=1}^n\left(V_{j=1}^n l_j\right)$$
> por ejemplo: $(\hat x \lor y)\land (y \lor z)$
+ LLamamos cláusulas a los conjuntos de disjunciones unidos por las conjunciones

> [!Attention] EXAM & PROBLEMS: 
> De cara al examen y problemas de examen siempre obtendremos **directamente esta forma**, no buscaremos obtener una fórmula de ningun otro tipo. 

## Modelo:
> [!NOTE] Modelo: 
> Un modelo de satisfabilidad lógica es la **definición de variables de una fórmula para que dicha fórmula se cumpla.** 
> $$
> M = \{x_i = T|\perp\}: \forall i \in X
> $$
> 
> Decimos entonces que: 
> **Una fórmula es satisfacible si y solo si existe un modelo para el cual la formula es verdadera**

Según la complejidad de la fórmula obtener el modelo será mas o menos dificil: 

+ **1-SAT**: problema que se resuelve en tiempo lineal $O(n)$. Este problema tiene la forma de:
$$x_1 \land \overline{x_2} \land \overline{x_1} \space ... \space \land x_n$$
	+  No contiene ANDS
+ **2-SAT**: problema que se resuelve en tiempo cuadrático $O(n²)$
$$(\overline{x_1} \lor x_2) \land (x_1 \lor \overline{x_3}) \space ...$$

Para obtener el modelo podemos aplicar los siguientes métodos: 
+ Para problemas del primer tipo:  [[1733916831 - Metodo de resolución SAT|Resolucion SAT]]
+ Para problemas del segundo tipo usaremos: [[1733917531 - Algorithm - Davis-Putnam|Algorithm - Davis-Putnam]] o [[1733918229 - Algorithm - Davis-Putnam-Logemann-Loveland|Algorithm - Davis-Putnam-Logemann-Loveland]]

***

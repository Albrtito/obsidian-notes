---
Date: 2024-03-18
tags:
  - discrete
"References:": 
sr-due: 2024-12-18
sr-interval: 239
sr-ease: 270
---

> [!NOTE]  Theorem:
> For a sequence like the [[1726827729 - Defninition - Serie de Fibonacci|Fibonacci sequence]]:
>$$
>a_n = Aa_{n-1} + Ba_{n-2}: n>= 3
>$$
> The solution for this type of recurrences is based on a transformation into a second degree equation.  For each term of a a power of x will be assigned. This way for the lowest term the power 0 is assigned. From there higher powers are assigned. 
> In this case $a_{n-2}$ is the lowest power and so $Ba_{n-2}$ is transformed into $Bx^0 = B$. 
> For the complete transformation we'll get: 
>$$
> x^2 = Ax + B
>$$
> After transforming solutions for the equation can be obtained. There are three possible cases. (for $\alpha , \beta$ as solutions for the equation)
> 1. Both solutions are real and different ($\alpha \not = \beta$)
> 	1. The solution for the recurrence would be: $K_1 \alpha^n+K_2 \beta^n$
> 2. Both solutions are real and the same ($\alpha = \beta$)
> 	1. Then the solution for the recurrence would be: $(K_1+n K_2) \alpha^n$
> 3. Solutions are complex (imaginary numbers) : Then we cannot do shit, either the solution is "I cannot compute the solution" or u have forgotten how to multiply and computed wrong the second degree solution. 
> 
> **Conditions:**
> + Recurrence relation of order 2 
> + Homogeneous (no independent term)
> + Constant coefficients
> + Known initial conditions
> 
> **Solutions:**
>$$
> a_n= \begin{cases}K_1 \alpha^n+K_2 \beta^n & \text { if } \alpha \neq \beta \\ \left(K_1+n K_2\right) \alpha^n & \text { if } \alpha=\beta\end{cases}
>$$

**Remark:**
+ In order to get the value of K1 and K2 we'll use a system with the initial conditions by substitution of the n value in the obtained relation. 
f.e: If int he previous example we've had been given the initial conditions $a_1 $ $a_2$ and after computing the relation we've had obtained two real roots then the system would be such: 
$$
\begin{align}
a_1 = K_1\alpha^1 + K_2\beta^1\\
a_2 = K_1\alpha^2 + K_2\beta^2 
\end{align}
$$
As a1, a2 $\alpha, \beta$ are known we can obtain K1 and K2,


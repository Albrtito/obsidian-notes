---
aliases:
  - Methods for solving limits
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-07-01
sr-interval: 17
sr-ease: 248
---
# Methods for solving limits:

## 1. **Look for common factors**
**f.e:** See here that after removing (x-3) we can compute the limit
$$
\begin{aligned}\lim_{x\to3}\frac{x^2-9}{x^2-5x+6}=\lim_{x\to3}\frac{x+3}{x-2}=6.\end{aligned}
$$

## 2. **Divide by the greatest term**
**f.e:** See here that after dividing by x we get a limit that can be computed. However note that this computation can be also computed based on what is explained in [[#Polynomial quotients]]  
$$
\lim_{x\to\infty}\frac{x+3}{x-4}=\lim_{x\to\infty}\frac{1+3/x}{1-4/x}=1.
$$

## 3. **Use the conjugate**
**f.e:** When having roots, it is reliable to say that in most cases the solution goes towards conjugates. 
$$
\lim\limits_{x\to\infty}\left(\sqrt{x+1}-\sqrt{x}\right)=\lim\limits_{x\to\infty}\frac{1}{\sqrt{x+1}+\sqrt{x}}=0.
$$
## 4. Change of variable: 
When there are several roots (dividing) of different exponent there may be a chance to perform a change of variable such as the roots disappear: 
**f.e:**
	$$
	\lim_{x\to64}\frac{\sqrt{x}-8}{\sqrt[3]{x}-4}
	$$
	Because there is an square root and a cubic root. Use: $t^6 = x$ . Then $\sqrt[6]x = t$ and if x = 64   t = 2 ($2 = \sqrt[6]{64}$) and we have the following transformation to the limit: 
	$$
	\lim_{t\rightarrow 2} \frac{x^3 - 8}{x^2 - 4}
	$$
	This can be factored into: 
	$$
	\lim_{t\rightarrow 2} \frac{(x-2)(x^2+2x+4)}{(x-2)(x+2)}
	$$
	Turning into: 
	$$
	\frac{4 + 4 + 4}{4} = 3
	$$
## 5. [[20240620 - 154721 - Taylor Polynomial|Taylor Polynomial]]
We can use the taylor polynomial in order to approximate functions that appear in limits.

f.e: 
	$$
	\begin{gather}
	\operatorname*{lim}_{x\to0}\frac{\operatorname{cos}x-\operatorname{e}^{x}+x}{x^{2}} \\\\
	=\lim_{x\to0}\frac{1-x^2/2+o(x^2)-(1+x+x^2/2+o(x^2))+x}{x^2} \\\\
	=\lim_{x\to0}\frac{-x^2+o(x^2)}{x^2}=-1.
	\end{gather}
	$$

## Theorems: 
List of useful theorems for limit solving: 
$$
lim_{x\rightarrow x_0} f(x)
$$
### 1. Sandwich lemma
**If you can find a function g(x) and h(x):** g(x) ≤ f(x) ≤ h(x) then:
   
→ [[20240605 - 171939 - Theorem - Sandwich lemma|Sandwich lemma]]
  
### 2. Exponential limits
For limits such as:
$$\lim_{x\rightarrow \alpha} 1^{\infty /-\infty}$$
→ [[20240605 - 175232 - Theorem - Exponential limits|Exponential limits]] 

### 3. Exponential form: 
The following limit is well known and can be obtained directly:

$$
\lim_{x\rightarrow 0} (1+x)^{1/x} = \lim_{x\rightarrow 0} [\frac{1} {(1+x)}]^x = e
$$

→ [[20240606 - 220121 - Exponential limit forms|Exponential limit form]]

### 4. L’Hôpital rule: 

$$
 \lim_{x\rightarrow a} \frac {f(x)}{g(x)} = \lim_{x\rightarrow a} \frac {f'(x)}{g'(x)}
 $$

→ [[20240616 - 155016 - Theorem - L'Hôpital-Bernoully rule|L'Hôpital rule]]


## For limits at infty:

For solving limits at infty we can use several methods and strategies. Of course, because Calculus is just a bunch of happy ideas very smart people had to ruin the life of the student these are just some suggestions that could work. Who knows what ur dealing with!

### Polynomial quotients:
For limits such as: 
$$
\begin{gather}
\lim_{x\rightarrow x_0} f(x): \\ f(x) = \frac{P_1(x)}{P_2(x)} =\frac{a_0+xa_1+x^2a_2...+ x^na_n}{a_0+xa_1+x^2a_2...+ x^na_n}
\end{gather}
$$

There are three posible casos based on the **maximum degree of x in P1 and P2**: 

1. If the max degree of x in P1 is greater than the one in P2 then **the limit goes to infinity**
   $$
   Max(P_1) > Max(P_2) \Rightarrow \infty
   $$
   
   The idea is that the part above grows larger than the one below. Then it goes to infty before being able to be divided by anything. 
   
   f.e: 
	   $$
	   \lim_{x\rightarrow x_0} \frac{x^2+2}{x} = \infty
	   $$

2. If the degree of x in P2 is greater than the one in P1 then **the limit goes to 0**
   
   Same idea, but if the part below goes to infinity first, then it is division by infinity → 0 
   $$
   Max(P_2) > Max(P_1) \Rightarrow 0
   $$
   f.e: 
   $$
	   \lim_{x\rightarrow x_0} \frac{x}{x^2 + 2} = 0
	$$

3. If the degree of x in P2 is equal to the one in P1 then:
   **The limit is equal to the division of both coefficients of**: $x^{\text{maxDegree}}$
   
   f.e: 
	   $$
	   \lim_{x\rightarrow x_0} \frac{4x^2}{x^2 + 2} = \frac{4}{1} = 4
	   $$
**Remark:**
+ For **roots** it is nothing more than changing the exponent of the x inside the root. 
  f.e: An $1/x^1$ goes into an square root as $1/x^2$ and so on. 
  So we can directly say that for limits such as: 
  $$
  lim_\infty \frac{x-2}{\sqrt{4x^2 + 1}}
  $$
  The solution would be 1/2 as the $x^2$ inside the root is equal to x outside. And the 4 goes to 2 because of the root. 

### Bounded functions: 
There exists a family of functions that can be defined as **bounded** this means that **their values always oscillate in an interval**. 
Some of this functions are trigo functions:
$$
\sin x, \cos x ...
$$
What does this imply for limits at infty. Well, we can define two cases. 

1. Bounded functions that oscillate between all **positive values** or all **negative values**
	
	In this cases we can just treat the function as a constant, negative or positive. As when reaching infty this oscillation doesn’t really matter. 


2. Bounded functions that oscillate between **positive and negative values**
   
   This functions are the **danger zone** ones, in some cases we **won’f find a solution to the limit**as the oscillation between positive and negative in, for example, a multiplication, makes it impossible to obtain only one value for the limit.
   Other times when we have sum’s and similar operations with them we’ll easier find limits as it does not matter if we sum or subtract any value to infty (or minus infty).
## For limits at 0: 

### 1. Trigo: Power reducing formula: 
+ [[20240611 - 135712 - Trigonometric power reducing formula|Trigonometric power reducing formula]]
### 2. Different power roots: 
For different power roots the best path is to perform a **change of variable** that takes out the roots or transforms them into squares roots. 

### 3. Binomial limits: 
Binomial limits can be expressed using the [[20240515 - 013001 - Theorem - Newton's binomial theorem|Newton's binomial theorem]]. After changing the expression the limit is usually easier.

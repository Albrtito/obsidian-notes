---
Date: 2024-03-12
tags:
  - diffcalc
"References:":
  - "[Initial value problem](Initial%20value%20problem)"
  - "[ODEs](ODEs.md)"
sr-due: 2024-08-19
sr-interval: 99
sr-ease: 258
---
# Solving ODEs with the laplace transform 
 + This technique can be also applied for non-homog. terms with discontinuities(g(t))
+ Useful for ODEs of order higher than 2
+ Transform an initial value problem ode to an algebraic equation 

We'll use ODEs that are **linear, with constant coefficients**, for different g(t) and different order(n = 2 or higher).
+ Using the Laplace transform is really useful for solving **initial value problems**

## Practice cases:
### Example 1:
**Initial ODE:**
+ **HOMOGENEOUS**
$y'' -y' -2y = 0, y(0) = 1, y'(0) = 0$

**Using the Laplace transform:**
+ Suppose that the sol. y = y(t) exist (as in the previous theo.)
$$
\zeta\{y''-y'-2y\} = \zeta\{0\}
$$
Use 1st property of the [The Laplace transform](The%20Laplace%20transform.md): **Linearity of the transform**
$$
\zeta\{y''\} - \zeta\{y'\} - 2\zeta\{y\} = 0
$$
Using the 2nd property: **Transforms of derivatives**
$$
s^2 \zeta \{y\}- sy(0) - y'(0) -[s\zeta\{y\}-y(0)]-2\zeta\{y\} =0
$$
Renaming $\zeta \{y\} = Y(s)$ we get:
+ **Remember**: y'(0) = 0
$$
s^2 \zeta \{y\}- sy(0) - y'(0) -[s\zeta\{y\}-y(0)]-2\zeta\{y\} =0
$$
Now we are using the ODE and the initial conditions together, this is why we can use y'(0) = 0. After simplification of the equation above.
$$
[s^2-s-2] Y(s) + 1- s = 0
$$
Isolating Y(s)
$$
Y(s) = {s-1 \over s^2 - s -2}
$$
 **Remarks:**
 + The bottom part is the characteristic equation
 + We **obtained the Laplace transform of the solution of the ODE.** Final step is to obtain the actual ODE solution. 

Find y(t) wh0se Laplace transform is Y(s). In order to do so we'll use the [[20240620 - 170611 - Method - Partial Fractions|Partial Fractions]] 
$$
Y(s) = {1\over 3}{1\over s-2} + {2 \over 3}{1\over s+1}(k_1, k_2 \in R): k_1 = 1/3, k_2 = 2/3
$$
Then we know: (Use the PDF in aulaglobal)
**FINAL SOLUTION:**
$$
Y(s) = {1\over 3}e^{2t} + {2 \over 3}e^{-t}
$$

### Example 2:
**Initial ODE**: Initial value problem
+ **NON- HOMOGENEOUS**
$$
y'' -2y' + 5y = t: y(0) = 1, y'(0) = 2
$$
Transformation, turning each y to it's Laplace transform (using linearity property)
$$
\zeta\{y''\} - 2\zeta\{y'\} + 5\zeta\{y\} = \zeta\{t\}
$$
After solving this (apply the derivatives property) we get the following value for Y(s). 
**Note:** $Y(s) = \zeta\{y\}$  so now that we want to compute y(t). In order to obtain that function we'll compute the **inverse of  the Laplace transform**
$$
\begin{align}
Y(s) = \zeta\{y(t)\} \\ y(t) = \zeta^{-1}\{Y(s)\}
\end{align}
$$
$$
Y(s) = {s^3 + 1\over s^2(s^2-2s+5)} 
$$
Using the [[20240620 - 170611 - Method - Partial Fractions|Partial Fractions]] we obtain: 
$$
Y(s) = \frac{A}{s} + \frac{B}{s^2}+ \frac {Cs + D}{s^2 - 2s + 5}
$$
+ The first two fractions are created  due to the $s^2$ there is in the initial quotient
+ A, B, C,D (all real) are values to be found
After finding A,B, C, D we get: 
$$
A = 2/25, B = 1/5, C = 23/25. D = -1/25
$$
Then we get the following expression: 
$$
Y(s) = \frac{2/25}{s} + \frac{1/5}{s^2}+ \frac {1}{25}\frac {23s -1}{s^2 - 2s + 5}
$$
**Note:** We use the following trick to manipulate all so that we can get an expression that appears in the table given in [DiffCalc_Resources_Laplace_Transforms](../00.References/DiffCalc_Resources_Laplace_Transforms.pdf)
$$
\frac {23s -1} {(s-1)^2 + 4} = \frac {23(s -1) + 22} {(s-1)^2 + 4} = 23\frac {(s -1)} {(s-1)^2 + 4} + 11\frac{2}{(s-1)^2+4}
$$
**Solution after applying the table inverse transformations:**
$$
y(t) = \zeta^-\{Y(s)\} = \frac{2}{25} *1 + \frac{1}{5}t + \frac{23}{25}e^t cos(2t) + \frac{1}{25} e^t sin(2t)
$$
## How to use it: 
After these two examples we can say the following steps are used to compute IVP with the Laplace transform: 
1. Transform the ODE such as $Y(s) = \zeta\{y(t)\}$
2. Use linearity property of Laplace transform to separe all transformations
3. Use derivative property of Laplace transform to get all wrt y and y'. 
4. Apply the initial conditions 
5. Now u have obtained Y(s) = (some expression) here comes the difficult part
6. Compute the **inverse Laplace transform** of Y(s) obtaining y(t). 
	1. For this step use [[20240620 - 170611 - Method - Partial Fractions|Partial Fractions]] and the [DiffCalc_Resources_Laplace_Transforms](../00.References/DiffCalc_Resources_Laplace_Transforms.pdf) . We could also use the [Convolution product](Convolution%20product.md) of the function if we knew had the initial conditions in order to apply the convolution on Y(t)
	3. This table contains most of the inverse transformations we'll use. However some tricks could be needed in order to obtain expressions that can be used with the table. 

### Remarks: What if we don't know the values at 0 but at another point $t0$ ?
The use of the Laplace transform requires to know the value of the sol y and its derivative at t= 0. What if we don't have those?
For this cases we should apply **change of variable** in the following way: 
$$
\tau = t - t_0
$$
Where tau is the newly created variable
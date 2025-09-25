---
id: 20240528 - 121302 - First order linear  ODE
aliases: []
tags: []
---
# First order linear ODE 

> [!NOTE] Quick method: 
> **Conditions:**
> + Order 1
> + linear
>
>**Estandar form:**
>$$
> \frac{dy}{dx} + P(x) y = f(x)
>$$ 
>**Method:**
> 1. Obtain integration factor: $$u = e^{\int P(x)}$$
> 2. Solution given by: $$\frac{d[u*y]}{dx} = f(x)*u$$
> 3. Integration at both sides: $$ \int\frac{d[u*y]}{dx} dx = \int f(x)*u \space dx$$ 
> 4. Solve right side integral: (Left side goes away by FTC): $$ u*y = \int f(x)*u \space dx$$


## General form and solution:

This DE are of the form: 
$$
a_1(x)u' + a_0(x)u = F(x)
$$
+ Solution is the function u(x) or u.
**Where:**
+ $a_1(x)$ is a function of x multiplying the first derivative of u
+ $a_0(x)$ is a function of x multiplying the function u
+ F(x) is a function of x

**Remarks:**
+ When F(x) = 0 the DE is **homogeneous**

### General solution: 
The method is based on finding the solution for the homogeneous and then for the particular equation
1. First, solve the homogeneous equation (without F(x)). This solution is: 
$$
\begin{gather}
a_1\frac{du}{dx} + a_0 u = 0\\
\frac{du}{dx} = -\frac{a_0u}{a_1}\\
\frac{du}{u} = -\frac{a_0dx}{a1}\\
\int \frac{1}{u} du = \int -\frac{a_0}{a1} dx\\
\ln|u| = \int -\frac{a_o}{a_1}dx\\
\boxed{u_h = C_1 e^{\int-\frac{a_o}{a_1}dx}}
\end{gather}
$$


We simplify calling g(x) to:

$$
g(x) = \int^{}_{x}\frac{a_0(t)}{a_1(t)}dt
$$
Then the general solution for the homogeneous part, using the new definition of g(x) would be: 
$$
\boxed{u_h = C_1e^{-g(x)}}
$$
 2. We can create a relation between this new solution we have found for the homogeneous and F(x) in order to find a **solution to the particular form** #duda WHAT?
$$
\left[e^{g(x)} u\right]^{\prime}=\frac{F(x) e^{g(x)}}{a_1(x)}
$$
This expression can be simplified by direct integration: 
**Note:** $[e^{g(x)}u]'$ is **all** derived. Then an integer just removes the derivative leaving $e^{g(x)}u$
$$
e^{g(x)} u_p=\int^x \frac{F(x) e^{g(x)}}{a_1(x)}
$$
Simplified: 
$$
 u_p=e^{-g(x)}\int^x e^{g(x)}\frac{F(x) }{a_1(x)}
$$
Because we know the value of $e^{g(x)}$ already we have obtained the particular form.

 3. The final **general solution is given based on the principle of superposition** (sum of both homogeneous and particular parts)
**Note:**
 + The homogeneous equation is multiplied by a constant (A) that will appear from integration of g(x). (it’ll be some e to some constant) 
$$
u(x) = u_h + u_p
$$
$$
u(x) = Ae^{g(x)} + e^{-g(x)}\int^x e^{g(x)}\frac{F(x) }{a_1(x)}
$$

**Remark:**
+ For the non-homogeneous part, the integral will need to be usually done applying [[20240529 - 132751 - Method -Integration by parts|Integration by parts]]
+ The value: $e^{g(x)}\over a_1(x)$ is called **integrating factor** because it reduces the non-homogeneous part in order to solve by direct integration.
+ #duda : Same as last one in this same document. 
+ This solution is also true for an ODE of n-th order 

## Solved examples: 
$$
u' + xu = xe^{x^2}
$$
+ With u(0) = 1 as Initial condition
Then: 

**USING THE METHOD EXPLAINED BEFORE:**

**Homogeneous part:**
$$
\begin{gather}
u' + xu = 0\\
{\frac{du}{dx}\over u} = -x\\
\frac{1}{u}du = -xdx\\
\int \frac{1}{u}du = \int -xdx\\
\ln u = \frac{-x^2}{2}\\
u_h = C_1e^{\frac{-x^2}{2}}
\end{gather}

$$
Here the **integrating factor is:** $e^{\frac{x^2}{2}}\over 1$ and g(x) = $\int \frac{x^2}{2}$

**Particular part:**
$$
u_p = e^{-g(x)} \int F(x) e^{\frac{-x^2}{2}}
$$
$$
u_p = e^{-x^2\over 2}\int xe^{x^2}e^{-x^2\over 2}
$$
$$
u_p = -e^{x^2\over 2}\int x e^{3x^2\over 2}
$$
Applying integration by parts and u-substitution.
$$
\begin{gather}
u_p = e^{-x^2\over 2} \frac{1}{3} e^\frac{3x^2}{2} + C_2 = \\
e^{-x^2\over 2}\frac{1}{3} e^\frac{x^2}{2} \cdot e^{x^2} + C_2=\\
\boxed{\frac{1}{3}e^{x^2} + C_2 = u_p}
\end{gather}
$$

We obtain a final solution: 
$$
\begin{gather}
C_1e^{\frac{-x^2}{2}} + \frac{1}{3}e^{x^2} + C_2 = u_p= u\\
C_3 e^{\frac{-x^2}{2}} + \frac{1}{3}e^{x^2} = u \\
\end{gather}
$$
+ C3 appears from the union of the other two constants.

**Initial value problem:** 
Use the initial value of u: u(0) = 1. To obtain C3

$$
\begin{gather}
u(0) = C_3 + 1/3 = 1\\
C_3 = 1 - 1/3 = 2/3
\end{gather}
$$
Then we get the final solution for the DE with the given initial conditions: 

$$
\begin{gather}
\frac{2}{3}  e^{\frac{-x^2}{2}} + \frac{1}{3}e^{x^2} = u \\
\boxed{\frac{1}{3}[2e^{\frac{-x^2}{2}} + e^{x^2}] = u} \\
\end{gather}
$$

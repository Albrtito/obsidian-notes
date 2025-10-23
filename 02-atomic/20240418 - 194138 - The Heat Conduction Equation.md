---
id: 20240418 - 194138 - The Heat Conduction Equation
aliases: []
tags: []
---
# The heat conduction equation
## Description of the model used in DiffCalc UC3M course:
We’ll take as a model a cylindrical solid bar of some homogeneous material. This bar is insulated such as the only possibility for the bar to exchange heat is at the ends. 
 
Let’s first make some **assumptions** to simplify the problem: 
+ Dimensions of each cross-section (cut with the plane z-y) of the bar are smaller compared with L. This means
	+ Temperature will be constant on such sections
	+ The bar is considered one-dimensional. → The only space variable being x
+ Bar surface is insulated; heat is exchanged only through the ends
+ **We’ll study the behaviour of the bar temperature, u(x,t) in space x and time t.**

### First model: 

$$
\begin{cases} 
{\partial u\over \partial t} = \alpha^2 {\partial^2 u\over \partial x^2}, &\text{For: } 0<x<L& t>0 &\rightarrow PDE \\\\

u(0,t) = 0; u(L,t) = 0,& \text{For: }t >0 & \rightarrow \text{Boundary Conditions} \\\\

u(x,0) = f(x), & \text{For: } 0\leq x \leq L & \rightarrow \text{Initial Condition}
\end{cases}
$$

+ Given data: L, $\alpha$ 
+ Boundary conditions ensure that at the end and at the beginning of the tube the temperature is always 0
+ Initial conditions ensure that at time equals 0, the temperature equals to the function f(x) that determines the initial temperature in the bar.
**Remarks:**
+ Alpha squared representes the thermal diffusivity (depends on the material)
+ We’ve Dirichlet Homogeneous BCs (named after the guy who discovered this type of Boundary conditions)
+ f is the initial temp. distribution in the bar. 

#### Solving: 
In order to solve the model we’ll use the [Method of separation of variables](20240418%20-%20193802%20-%20Method%20-%20Separation%20of%20variables.md)…

1. Substituting into the PDE…
^SeparationOfvariables
$$
\begin{gather}
{\partial u\over \partial t} = {\partial \over \partial t}(X(t)T(t)) = X(x){d\over dt} T(t) = X(x)T'(t)\\\\
{\partial^2 u\over \partial x^2} = {\partial^2 \over \partial x^2}(X(t)T(t)) = {d^2\over dx^2}X(x) T(t) = X''(x)T(t)\\\\
\Rightarrow_{\text{PDE}}\\\\
XT' = \alpha ^2 X''T \Rightarrow\\\\
\boxed{\frac{1}{\alpha^2}\frac{T'}{T} = \frac{X''}{X} : (T(t) \not = 0, X(x)\not = 0)}
\end{gather}
$$
+ Since if one of the variables changes while the other one is maintained fix, the other one would still change, violating the identity.The only possibility for this identity to comply is by including a separation constant lambda.
$$
\lambda = \text{Separation constant}
$$
$$
\begin{gather}

	\begin{cases}
		\frac{1}{\alpha ^2}\frac{T'}{T} = -\lambda \\\\
		\frac{X''}{X} = -\lambda
	\end{cases}

\\\\
\Rightarrow
\boxed{
\begin{cases}
		T' + \alpha^2\lambda T = 0  \\\\ 
		X'' + \lambda X = 0
	\end{cases}
	
}
\end{gather}
$$
**These two equations are ODEs !!**

2. Let’s consider the BCs (Boundary conditions) ^8f043a

$$
\boxed{x = 0}: u(0,t) = 0 \Rightarrow X(t)T(t) = 0 \Rightarrow \boxed{X(0) = 0}
$$
+ T(t) $\not =$ 0. As we are looking for non-zero solutions

$$
\boxed{x = L}: u(L,t) = 0 \Rightarrow X(L)T(t) = 0 \Rightarrow \boxed{X(L) = 0}
$$
3. Applying the boundary conditions to the ODEs found in step 1.

For the second function: 
$$
\begin{cases}
X'' + \lambda X = 0\\\\
X(0) = 0; X(L) = 0
\end{cases}
$$
+ **THIS IS THE BOUNDARY VALUE PROBLEM**
This means finding the eigenvalues and eigenfunctions. 
$$
\begin{cases}
\lambda _n = \frac{n^2\pi}{L^2} & n = 1,2,... \rightarrow \text{Eigenvalues}\\
X_n(x) = sin(\frac{n\pi}{L}x)& n = 1,2,... \rightarrow \text{Eigenfunctions}
\end{cases}
$$
Applying it to the first one: 
$$
T' + \alpha ^2\lambda T = 0 \rightarrow \boxed{T' +\frac{\alpha^2n^2\pi^2}{L^2}T = 0}
$$
Because $\frac{\alpha^2n^2\pi^2}{L^2}$ is constant, this ODE is **order 1, linear** and can be solved **using the integrating factor.**

4. The **solution** will be proportional to: 
$$
T_n(t) = e^{-(\frac{n^2\pi^2\alpha^2}{L^2})t} ; \text{   } n = 1,2,...
$$
##### Solution of the model: 
Finally, we get…
$$
\begin{gather}
u_n(x,t) = T_n(t)X_n(x) = \boxed{\boxed{e^{-(\frac{n^2\pi^2\alpha^2}{L^2})t} sin(\frac{n\pi}{L}x)}}; & n = 1,2,---
\end{gather}
$$
+ This is **the fundamental solution of the heat equation**
+ This solution is linearly independent for all t grater than 0
+ $u_n(x,t)$ satisfies the PDE + BCs

Using the [Principle of Superposition](Principle%20of%20Superposition) we make a “combination" of all these solutions, we get: 
$$
u(x,t) = \sum^\infty_{n = 1} c_nu_n(x,t)
$$
The **formal solution of the heat equation** (<font color="#ff0000">MAY BE AN EXAM QUESTION)</font>

#### Formal solution of the model: 
$$
u(x,t) = \sum^\infty_{n = 1} c_n e^{-(\frac{n^2\pi^2\alpha^2}{L^2})t} sin(\frac{n\pi}{L}x)
$$
The coefficients $c_n$ can be found using the [[20240418 - 190338 - Fourier series|Fourier series]] along with the initial conditions provided u(x,0) = f(x). Once applied (see below for an example of this application) we get: 
$$u(x, t)=\sum_{n=1}^{\infty}\left(\frac{2}{l} \int_0^l u_0(s) \sin \frac{n \pi s}{l} d s\right) e^{-n^2 \pi^2 k t / l^2} \sin \frac{n \pi x}{l} .$$

##### Obtaining u(x,t) knowing that f(x) = u(x,0)
If we know that f(x) = u(x,0) then, because u(x,0) = $\sum^\infty_{n=1}c_ne^{-(\frac{n^2\pi^2\alpha^2}{L^2})t}sin(\frac{n\pi}{L}x)$ if t = 0, then 
$$
\sum^\infty_{n=1}c_ne^0sin(\frac{n\pi}{L}x) = \sum^\infty_{n=1}c_nsin(\frac{n\pi}{L}x)
$$
 
This means that:

$$
f(x) = \sum^\infty_{n=1} c_nsin(\frac{n\pi}{L}x)
$$
Based on this, if we know the expression for some function f(x), we can obtain the expression for u(x,t). 

**f.e:** For f(x) = 1
$$
f(x) = \sum^\infty_{n=1}c_nsin(\frac{n\pi}{L}x) = 1
$$
For this type of function we know that, based on what is said in [Fourier series](20240418%20-%20190338%20-%20Fourier%20series.md) : 
$$
\begin{gather}
\int^{L}_{-L}sin(\frac{n\pi}{L}x)sin(\frac{m\pi}{L}x)dx = \\\\
\frac{L}{2}\cdot 
\begin{cases}
0 : \text{IF: } n\not = m\\
1: \text{IF: } n = m
\end{cases}
\end{gather}
$$
We can use this property, multiply both sides by $sin\frac{m\pi}{L}x$ to obtain: 
$$
\sum^\infty_{n=1}c_nsin(\frac{n\pi}{L}x) sin(\frac{m\pi}{L}x) = sin(\frac{m\pi}{L}x)
$$
We know that only if n = m the integral defined above is different from 0. Then we integrate the expression: 
$$
\int_{0}^{L} \sum^\infty_{n=1}c_nsin(\frac{n\pi}{L}x) sin(\frac{m\pi}{L}x) dx = \int^{L}_0
 sin(\frac{n\pi}{L}x)dx
$$

On the left hand side of the equality, after simplifying (we can take the sum out with the constants), we know that this side can only be different from 0 if n = m, and if its different it’s value will always be $L\over 2$
$$
\sum^\infty_{n=1}c_n\int_{0}^{L} sin(\frac{n\pi}{L}x) sin(\frac{m\pi}{L}x) dx = \int^{L}_0
 sin(\frac{n\pi}{L}x)dx
$$

Then for some term m (the one we inserted with the m variable) we have. 
+ $c_m$ : The coefficient for n = m
+ We take n = m because this term is the only one in the sum that’s different form 0. 
 
 $$
c_m \frac{L}2= \int^{L}_0
 sin(\frac{n\pi}{L}x)dx 
$$
 Moving it to the other side we finally get the expression for $c_m$. **This is the solution to compute the coefficients of u(x,t)**
 $$
c_m = \frac{2}{L}\int^{L}_0
 sin(\frac{n\pi}{L}x)dx 
$$
**REMARKS:**
 + There is **not only one solution** but at least n solutions(infinite solutions). As for each n. There is a coefficient such as n = m that is defined with the obtained expression. 

Following the example, let’s **find the generalised form of $c_m$:** (for f(x) = 1) 

Solving the integral, we multiply by whatever it is inside the sin in order to compute the integral 

$$
c_m = \frac{2}{L}\frac{L}{m\pi}\int^{L}_{0} \frac{mn}{L}sin(\frac{m\pi}{L})dx
$$
Canceling the L’s outside the integral and solving: 
$$
\begin{gather}
c_m = \frac{2}{m\pi} [-cos(\frac{m\pi}{L}x)]^{x = L}_{x = 0}\\
c_m = \frac{2}{m\pi}(-cos(m\pi)+1)\\
c_m = \frac{2}{m\pi}(1-cos(m\pi)) = \frac{2}{m\pi} *\begin{cases} 2 & \text{m is odd}\\ 0& \text{m is even}\end{cases}

\end{gather}
$$
The odd and even case is there to explain the following: 
+ When m is odd, then we have $(1-cos(m\pi))$ = 2 as $cos(m\pi) = -1$. Then, we multiply by 2
+ If m is even. Then $(1-cos(m\pi))$ = 0 as $cos(m\pi) = 1$. Then, we multiply by 0. (zero solution, not interested)

Once we have an expression for all the coefficients we can write the function u(x,t)
$$
\begin{gather}
u(x,t) = \sum^{\infty}_{n = 1} c_ne^{-(\frac{n^2\pi^2\alpha^2}{L^2})t} sin(\frac{n\pi}{L}x) \\
u(x,t) = \sum^{\infty}_{n_{n = odd} = 1} \frac{4}{n\pi}e^{-(\frac{n^2\pi^2\alpha^2}{L^2})t} sin(\frac{n\pi}{L}x)
\end{gather}
$$
In order to generalise the solution. (because we only care about the odd values and we cannot express it with n). Change the variable to k with the following definition for even and odd numbers. 
$$
\text{even numbers: } 2n, n = 0,1,2,3..
$$
$$
\text{odd numbers: } 2n+1, n = 0,1,2,3..
$$
Then using k = n define the **solution for u(x,t)**: 
$$
\boxed{u(x,t) \sum^{\infty}_{k = 0}\frac{4}{(2k+ 1)\pi} e^{-(\frac{n^2\pi^2\alpha^2}{L^2})t} sin(\frac{(2k +1)\pi}{L}x)}
$$


### Second model, defined length: 

$$
\begin{cases} 
{\partial u\over \partial t} =  {\partial^2 u\over \partial x^2}, &\text{For: } x\in(0\frac{\pi}{3}) \\\\

u(0,t) = 0; u(\frac{\pi}{3},t) = 0,& \text{For: }t >0 & \rightarrow \text{Boundary Conditions} \\\\

u(x,0) = f(x), & \text{For: } x\in[0,\frac{\pi}{3}] & \rightarrow \text{Initial Condition}
\end{cases}
    

$$

**Differences with the first model**
+ alpha is equal to 1 => No alpha
+ New intervals for which x is defined: The intervals are given based on a defined length equal to $\pi\over 3$
#### Solving:

1. Again, the [Method of separation of variables](20240418%20-%20193802%20-%20Method%20-%20Separation%20of%20variables.md) is used.
	Rolling back to the first model… we can see this solved in step 1. However in this case as alpha is 1. The resulting solution would be: 
$$
\begin{gather}
\text{Spatial part of the problem}\\\\
	\begin{cases}
		X''(x) + \lambda^2X(x) = 0\\
		X(0) = 0 = X(\frac{\pi}{3})
	\end{cases}
\\\\
\text{Temporal part of the problem:}\\\\

T'(t) + \lambda^2T(t) = 0
	
\end{gather}
$$
2. Solving the spatial problem, imposing the boundary conditions. 
**Spatial problem:**
$$
x = Acos(\lambda x) + Bsin(\lambda x)
$$
**Using boundary conditions**
$$
0 = X(0) = A \rightarrow A = 0 \rightarrow x = Bsin(\lambda x)
$$
**Solution of the spatial problem:**
$$
\boxed{X_n(x) = sin(3nx)}
$$



3. Solving the temporal problem: 
+ We’ll find one solution of the temporal problem for each solution of the spatial problem. 
$$
T_n'(f) `+ \lambda_n^2T_n(t) = 0
$$
Using the expression obtained from lambda in the last step
$$
T_n = e^{-\lambda^2_nt} = e^{-(3n)^2t}
$$
4. Once obtained this two solutions we can get the generalised solution for this heat model: 
**fundamental solution:**
$$
u_n(x,t) = e^{-9n^2t} sin(3nx)
$$
**General solution:**
$$
u(x,t) = \sum^\infty_{n=1}c_n e^{-9n^2t}sin(3nx)
$$


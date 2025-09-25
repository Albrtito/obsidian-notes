---
aliases: 
tags:
  - diffcalc
"References:": 
DateCreated: 2024-04-05
sr-due: 2024-04-24
sr-interval: 1
sr-ease: 130
---
# Systems of first order ODEs
## Intro: 
As we’ve already seen, a differential equation is defined as the relation between a function y(x), it’s derivative y’(x) and the independent variable x. 
The usual goal in those cases is to find the function y(x) such as the whole relationship is valid. 

What if the relation does not only refer to one function of x, but several of them? In that case we would have: 
$$
y'(x) = y(x) + y_2(x) + y_3(x) + x
$$

This relationship is imposible to solve by itself, we can however find a solution if we define other relationships regarding the functions $y(x), y_2(x), y_3(x)$, such as: 
$$
\begin{gather}
y'(x) = y(x) + y_2(x) + y_3(x) + x\\\\
y_2'(x) = 2(y(x)) + y_2(x)/2 + 4y_3(x) + 3x\\\\
y_3'(x) = y(x) + 4y_2(x) + y_3(x)/3 + x/2
\end{gather}

$$
Done this way there are now 3 differential equations for 3 functions of x we need to find. We can define a system of differential equations (Yay!). But first lets work a little bit further with this example: We’ll call each of the right hand sides of the equality above a function of the three functions of x (the three ys) and x.
$$
\begin{gather}
y'(x) = f_1 (y_1(x),y_2(x),y_3(x),x)(\\\\
y_2'(x) = f_2 (y_1(x),y_2(x),y_3(x),x)\\\\
y_3'(x) = f_3 (y_1(x),y_2(x),y_3(x),x) \\\\\\
\text{with: } \\\\
f_1 (y_1(x),y_2(x),y_3(x),x) = y(x) + y_2(x) + y_3(x) + x\\\\
f_2 (y_1(x),y_2(x),y_3(x),x) = 2(y(x)) + y_2(x)/2 + 4y_3(x) + 3\\\\
f_3 (y_1(x),y_2(x),y_3(x),x) =y(x) + 4y_2(x) + y_3(x)/3 + x/2


\end{gather}

$$

we can now generalise this case to **define any system of first order ODEs** 

**Remember:** It’s first order cause the biggest order of any of the derivatives we have is 1. 
f
It is linear cause all the functions of x (all the y’s) are never to the power of nothing bigger than 1. 

### General form of a system of first order ODEs
I’ll make some naming changes from the naming I’ve used for the example: 
+ t will be the independent variable (instead of x)
+ functions of t will be represented by $u_n$

$$
\begin{gather}
\frac{du_1}{dt} = f_1(u_1,....,u_n,t)\\
\frac{du_2}{dt} = f_2(u_1,....,u_n,t)\\
...\\\\
\frac{du_n}{dt} = f_1(u_1,....,u_n,t)\\
\end{gather}

$$
**Remarks:**
(adding here future remarks about lineal systems: Existence and uniqueness of a solution, autonomous and non-autonomous systems. Transformations between autonomous and non-autonomous systems.)

## Properties: 
### Autonomous systems: 
A system is said to be autonomous when all the functions $f_i$ that define it are **independent of the variable t.** Else the system is said to be non-autonomous. 

+ **Autonomous: Variable t is never alone, all $f_i$ do not contain i**
	f.e: $f_1(u_1,…,u_n), f_2(u_1,…,u_n),…,f_n(u_1,…,u_n)$
+ **Non-autonomous:** $f_i$ do contain i. 
	f.e: $f_1(u_1,…,u_n,t), f_2(u_1,…,u_n,t),…,f_n(u_1,…,u_n,t)$

**Remark:** 
Any system non-autonomous of order n is equivalent to an autonomous system of order (n+1). 
**Creation of the new funciton $u_{n+1}$**
+ Substitute all t for $u_{n+1}$ : Then $u_{n+1} = t$
+ Add a new equation of the form: 
$$
	\frac{du_{n+1}}{dt} = 1
$$


## Linear System:

**Remember:** Linearity of an ODE is based on wheter the exponent of y(t) is smaller or equal to 1.  

Then, linear ODEs systems can be described in terms of a linear algebra equation system. This way we’ll use a matrix A to represent the coefficients of each function for each equation (these coefficients are functions of t), the functions (u’s) will be represented as a vector. And the part there is left (the t in the functions for the general form) will be represented as a vector containing all funcitons of t. (I think I really did not explain myself in this paragraph, I will try to compensate in the following generalisation.)
### General form of a system of first order LINEAL ODEs
#duda Why are can we transform the system into this vectorial form if it’s lineal 

$$
\frac{du}{dt} = A(t)u + F(t)
$$
Where: 
+ u is a vector containing all the functions of the form $u_i(t)$ 
+ A is a matrix with all the coefficients for the previously defined functions on all the equations (these coefficients are function of t)
+ F(t) is a vector with all the “indpeendent terms" (I don’t know if I should call them that way but I understand it so fuck it)

When we expand this formula we get:
$$
\begin{gather}
\frac{d}{dt}
\begin{pmatrix}
u_1\\...\\u_n
\end{pmatrix}
=
\begin{pmatrix}
a_{11}(t) & ... & a_{1n}(t)\\
...\\
a_{n1}(t) & ... & a_{nn}(t)
\end{pmatrix}
\begin{pmatrix}
u_1\\...\\u_n
\end{pmatrix}
+ 
\begin{pmatrix}
F_1(t)\\...\\F_n(t)
\end{pmatrix}
\end{gather}
$$

### Homogeneous linear system: 

For an homogeneous system we’ll allways have: $F(t) = 0$

Using Abel’s theorem … (the whole explanation about how the eigenvalues are really important and where we really get those form goes here(or maybe the explanation is different, anyways it would go here and it’s not important for the solving of systems))

### A. Autonomous lineal systems: 

This systems are of the form: 
$$
\begin{gather}
\frac{du_1}{dt} = a_{11}u_1 + ...+ a_{1n}u_n\\
...\\
\frac{du_n}{dt} = a_{m1}u_1 + ...+ a_{nn}u_n\\
\end{gather}
$$
+ **The coefficients are constant**
**Remark:** This case can also be called, homogeneous-lineal with constant coefficients.

We can then write this as the following vectorial ODE:
$$
\frac{du}{dt} = Au
$$
Whith: 
$$
u =
\begin{pmatrix}
u_1\\...\\u_n 
\end{pmatrix},
A =
\begin{pmatrix}
a_{11}&...&a_{1n}\\
&...&\\
a_{n1}&...&a_{nn}
\end{pmatrix}
$$

**Note:** all the terms of the matrix A are constant (do not depend on t)
### General solution:
We’ll look for a solution of type:  $\underline u(t) = \underline Ue^{\lambda t}$ , when we insert this expresion into the equation we get: 
$$
\underline U\lambda e^{\lambda t} = \underline{\underline A}\underline Ue^{\lambda t}
$$
By extracting the common term $e^{\lambda t}$ we get: 
$$
\underline U\lambda = \underline{\underline A}\underline U
$$
The problem now is to find some values for lambda and for U such as the relation holds,this problem is the [Eigenvalue problem](Eigenvalue%20problem) seen in linear algebra. 

(If u don’t get eigenvalues or have forgotten them take a quick break to revisit. Go back to see how nice algebra and all first course courses where.)

Based on the solution of the eigenvalue problem we know that: 

**IF** matrix $\underline{\underline{A}}$ has n different eigenvalues with n (linearly independent) eigenvectors. 
+ We’ll note eigenvalues as: $\lambda _j$ 
+ We’ll note eigenvectors as: $\Phi _j$ 

**THEN:** The [Principle of Superposition](Principle%20of%20Superposition) states that the general solution of the equation is the following linear combination: 
$$
\underline u (t) = \sum ^n _{j=1}c_je^{\lambda _j t}\underline\Phi _j
$$
where: 
+ $c_j \in \mathbb{R}$ : are arbitrary constants defined by the **initial conditions**. Shoutout to the initial value problem (I.V.P)

+ we'll use the **principle of superposition.** As we have already done during the course. A linear combination of the solutions obtained is also a solution for the ODE.

## Cases: 
### Case with constant coefficients. 
+ With A being a real matrix (n x n)
$$
X'(t) = Ax(t)
$$
**note:** x = 0 (zero vector) is always a solution. 
Let's look for a sol. in this exponential form: $X(t) = ue^{rt}$ , with vector $u \in R^n$ , $r\in R$ to be found (note that u, r **can be complex**). (with **u not 0**)


Substitution into the system gives: 
$$
r u e^{rt} = Aue^{rt}
$$
$$
Au = ru
$$
**This is an EIGEN VALUE PROBLEM**
+ This is a solution as long as r and u are the eigenvalue and eigenvector.
**CONCLUSION:**
The proposed exponential solution is a solution of the system if v and u are an eigenvalue and the associated eigenvector of A. 

+ We need to calculate the eigenvalues $v_1,...,v_n$ of A

#### Computation of eigenvalues of A: 
There are three cases we need to distinguish: 
1. All eigenvalues are real and different
	1. Able to find n linearly independent eigenvectors (**we want this**)
	2. This happens if **A is symmetric** 
		1. Then all eigenvalues are real
		2. Even with repeated eigenvalues there **will be n linearly independent eigenvalues**
2. There are pairs of complex conjugate eigenvalues 
3. Some eigenvalues are repeated

**Summarising:** We want A to be symmetric
#### Case 1: 
For all eigenvectors real and different (linearly independent)
In this case we've n linearly indept.. eigenvectors $u^1,...,u^n$
$$
\Rightarrow \text{we've n sol, of (*): } X^1(t) = u^1e^{r_1t},...,X^n(t) = U^ne{r_nt}
$$
Are these solutions linearly independent? Check with the wronskian: 
$$
\begin{gather}
W[x^1,...,X^n] = det
\begin{bmatrix} 
u^1_1e^{r_1t} & ... &  u^n_1e^{r_nt}\\ 
 & ... & ... \\ 
u^1_ne^{r_1t} & ... & u^n_ne^{r_nt} 
\end{bmatrix}\\\\\\
= e^{r_1t}e^{r_2t}...e^{r_nt} det
\begin{bmatrix} 
u^1_1 & ... &  u^n_1\\ 
 & ... & ... \\ 
u^1_n & ... & u^n_n 
\end{bmatrix} \not = 0
\end{gather}
$$
+ $\forall t \in I$

**WE OBTAIN A GENERAL SOLUTION**
#### Computation of the general solution for case 1
$$
X(t) = C_1X^1(t) + ...+ C_nX^n(t), \text{with } C_1...C_n \in R
$$

+ **Remember** : A symmetric complies with all the requisites so it is also a general solution

#### Example: 
$$
X'(t) = \begin{bmatrix} -3 & \sqrt{2}\\ \sqrt{2} & -2 \end{bmatrix}
$$
1. Look for the sol. in the form $X(t) = ue^{rt}$ , with u ,r to be found. 
2. We get: $(A- rI) u = 0$
3. Find the eigenvalues imposing the $det(A-rI)=0$

$$
\begin{gather}
\begin{bmatrix}
-3-4 & \sqrt{2} \\ \sqrt{2} & -2-r
\end{bmatrix}
\begin{bmatrix}
u_1\\ u_2
\end{bmatrix}
= 
\begin{bmatrix}
0\\0
\end{bmatrix}

\\\\
\Rightarrow 
\\\\

det(A-rI) = 0\\\\

(-3-r)(-2-r)-2 =0\\
6 + 2r + 3t + r^2 -2 = 0\\
r^2 + 5r + 4 = 0\\
r_1 = -1\\
r_2 = -4
\end{gather}
$$

4. Both solutions must be linearly independent, then we can just use compute one of the linearly dependent solutions for each of them. First:
5. Obtain the relation between $u_1$ and $u_2$ with r = r1
$$
\begin{gather}
\begin{bmatrix}
-2 & \sqrt{2} \\ \sqrt{2} & -1
\end{bmatrix}
\begin{bmatrix}
u_1\\u_2
\end{bmatrix}
= 
\begin{bmatrix}
0\\0
\end{bmatrix}
\end{gather}
$$
Then: 
$$
-2u_1 + \sqrt{2} = 0 \rightarrow \sqrt{2}u_2= 2u_1 \rightarrow u_2 = \sqrt{2}u_1
$$

We can now substitute u2 for it's computed relation and compute the vlaue for the fist eigenvalue. 
$$
u^1 = u_1\binom{1}{\sqrt{2}}
$$
We can choose any value for u_1 as it will be linearly dependent to the actual eigenvalue (any of those are valid)
6. Compute the solution for the second eigenvalue, using the other root. r2
$$
 u^2 = \binom{-\sqrt{2}}{1}
$$
7. Computation of the general solution: $X^1(t) + X^2(t)$
$$
X(t) = C_1\binom{1}{\sqrt{2}}e^{-t}+ c_2\binom{-\sqrt{2}}{1}e^{-4t}: (c_1, c_2 \in \mathbb{R})
$$


#### Phase portrait of a system: 

With 2 x 2 systems we can visualise the system in the plane. 
$$
X^1(t) = (x_1,x_2) = (e^{-t}, \sqrt{2}e^-t) \rightarrow x_2 = \sqrt{2}x_1
$$


If we plot $X^2(t)$ we'll get: 
$$
x_2 = \frac{-1}{\sqrt{2}}x_1
$$
Plotting: 

```desmos-graph
x_2 = \frac{-1}{\sqrt{2}}x_1

```

**Both together:**

```desmos-graph
x_2 = \frac{-1}{\sqrt{2}}x_1
x_3 = \sqrt{2}x_4
```

x 
---

#### Case 2: 
#### Example: 

---
aliases:
  - Theorem - Solution of a non-homogeneous recurrence relation
tags:
  - discrete
"References:": 
cssclasses:
---
# Solution of a non-homogeneous recurrence relation: 

A linear non-homogeneous recurrence relation is such as there are **no powers of any term greater than 1** and **the independent term is different from 0**. For this theorem we'll call the independent term $t_n$
Of course for this course (#Discrete ) we'll always work with **constant coefficients**

A linear non-homogeneous recurrence relation is such as there are **no powers of any term greater than 1** and **the independent term is different from 0**. For this theorem we'll call the independent term $t_n$
Of course for this course (#Discrete ) we'll always work with **constant coefficients**

 
> [!NOTE] Theorem:
> Contents
>  For a sequence $(a_n): n\in N$: Non homogeneous with constant coefficients: 
>$$
\begin{gather}
a_n = c_1 a_{n-1} + c_2 a_{n-2}+...c_k a_{n-k} + t_n:\\ n>= k +1
\end{gather}
>$$
>**Conditions:**
>+ k initial conditions are known
>+ $t_n$ is a function  or n taking natural numbers and outputting real numbers
>
>**General Solution:**
>The solution for this recurrence will be the sum of the solution for the homogeneous part of the recurrence. (see [[Theorem 110 Solution of a homogeneous Fibonacci-type recurrence relation]] plus the solution for any particular solution of the full recurrence. **The key (the only harder part) is finding the particular solution**
>$$
a_n =a_n^h + a_n^p 
>$$
>+ $a_n$ is the solution for the relation 
>+ $a_n^h$ is the solution for the homogeneous 
>+ $a_n^p$ is the solution for the particular


## Solution for the particular part
>+ **Remark:** During the (#Discrete)  course we'll only see t as a polynomial function, a power function or a polynomial times a power  of n, non other type of functions. 
>  
>  + Then if $t(n)$ is a polynomial, it has to be of the form: 
> $$
>  t_n = b_0 + b_1n + ...+ b_tn^t
>$$
>+ If $t(n)$ is a power function then: 
>$$
> t_n = s^n
>$$
>+ If $t(n)$ is a polynomial times a power function
>$$
>t_n = s^n[b_0 + b_1n + ...+ b_tn^t]
>$$
>
>For each of this types of functions we'll make a guess of how the particular part should  look like. Generalising all three cases into a single guess we obtain: 
>$$
>a^p_n = s^n [p_0 + p_1n + ... + p_tn^t]
>$$
>+ If t is a polynomial then the $s^n$ disappears 
>+ If t is a power function then all what's inside the [] disappears
>+ If t is a power function times a polynomial then this is the proper guess
>
>When we make a guess of how the particular form should look we have the values for s (in the power function). N is our unknown and all the p's are constants we have to obtain. **Once we obtain these constants we'll have solved the particular part** 
>**Remarks:**
>+ All p's must have a concrete value. No free parameters
>+ Usually when solving we call the p's A, B,C..
>+ **When a root of the characteristic equation (the homogeneous part) solves the guess you've made. Then it's needed to multiply that guess times n. If again, a root solves it, multiply again**
>$$
>a^p_n = n^m s^n [p_0 + p_1n + ... + p_tn^t]
>$$
>Where m is the number of times that roots are repeated
>
### Finding the p's
>In order to find the value of all the p's (constants introduced via the guess made) the value for all elements in the recurrence relation is substituted by the particular solution (substituting n with the proper term). The after solving the relation we obtain the values for the p's

f.e: For a relation$a_n = a_{n-1} + a{n-2} + s^n[b_0 + b1_n + b2_n^2]$  the particular guess would be of the previously specified form: $a^p_n = s^n[p_0 + p_1n + p_2n^2]$. Then after substitution in the initial relation we get: 
>$$
\begin{gather}
s^n[p_0 + p_1n + p_2n^2] = \\
s^{n-1}[p_0 + p_1{n-1} + p_2{n-1}^2] \\
+ s^{n-2}[p_0 + p_1{n-2} + p_2{n-2}^2]\\
  + s^n[b_0 + b1_n + b2_n^2]
\end{gather}
>$$
+ We obtain the values for all p based on this relation

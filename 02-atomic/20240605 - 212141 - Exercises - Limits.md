---
aliases:
  - Exercises - Limits
tags:
  - calc
"References:":
  - "[[Calc_Exercises_LimitsContinuicity.pdf]]"
  - "[[Definition - Limits|Limit]]"
cssclasses:
  - page-manila
sr-due: 2024-06-29
sr-interval: 9
sr-ease: 210
---
# Exercises - Limits

## 2. Common factor: 
### 2.1: Use [[20240606 - 181806 - Notable Identities#($a n - b n)| Notable identity]]

### 2.3: Apply a change of variable:With different exponent roots this is a good method. 

Can it be done simply by multiplying by the conjugate? → With different value roots, go with a change of variable. 

### 2.5: Use [[20240515 - 013001 - Theorem - Newton's binomial theorem|Newton's binomial theorem]] 


### 2.6: Apply the conjugate (With three terms, just swap the sign of the root)


## 3. Using: $\lim_{x\rightarrow 0}\frac{\sin x}{x} = 1$ and $\lim_{x\rightarrow 0}\frac{e^x -1}{x} = 1$

### 3.1: Use a change of variable in order to separe the function: $t = 2x^3$

### 3.2: Conjugate to have something else than x squared down. Then use the trigonometric relation $sin^2 + cos^2 = 1$ up with the 1. 

### 3.3: This relation (the one defined above: [[#3. Using $ lim_{x rightarrow 0} frac{sin x}{x} = 1$ and $ lim_{x rightarrow 0} frac{e x -1}{x} = 1$|This one]]) is true for x. As long as x is equal everywhere the rest does not matter, so if: 


$$
lim_{x\rightarrow 0} \frac{sin (x^2)}{x^2} = 1
$$
+ With a change of variable we can directly see. Because it tends to 0. Does not matter there the change of variable and we can directly do t = $x^2$ 
### 3.5: Perform a **change of variable** : 
$$y = log(1 +x)$$
Take into account that then: 
$$
e^y = e^{ln(1 +x )} \Rightarrow e^y = 1 + x \Rightarrow x = e^y -1
$$

### 3.6: This is a direct limit of to e when x tends to 0, see:[[20240606 - 220121 - Exponential limit forms|Exponential limit forms]]

### 3.7: Apply Taylor

### 3.9: We are looking for the structure defined for this exercise. In order to get it we first obtain a common factor of $e^{sin x}$ and then apply a change of variable (that is not really necessary but in order to see the resemblance with the relation stated is needed)

### 3.12: Solved using [[20240611 - 135712 - Trigonometric power reducing formula|Trigonometric power reducing formula]]

## 4. Limits to infty: 

+ Polynomial formulas (whether one degree is greater than the other) are the a quick way of performing division by the largest factor. 
  For ROOTS with SUMS this division is better done directly. Taking into account that anything divided by x. If x goes to infty, goes to 0. 
+ For trigonometric functions. If divided by x they still go to 0. 
+ For the polynomial limits at infty is equivalent for terms for which we can perform a change of variable for a polynomial term. 
  f.e: 
  $$
  \lim_\infty \frac{e^x}{e^x - 1}
  $$
  
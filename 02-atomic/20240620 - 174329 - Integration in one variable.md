---
aliases:
  - Integration in one variable
  - Integral
tags:
  - calc
  - diffcalc
"References:": 
cssclasses: 
sr-due: 2024-06-26
sr-interval: 2
sr-ease: 248
---
# Integration in one variable: 
Collection of notes and concepts about the computation of integrals in one variable calculus. 

The first thing to see is how to compute the value of the primitive integrals and all the methods that we can use to do so. These methods are collected in the following note:
+ [[20240620 - 174413 - Calculus of primitive integrals|Calculus of primitive integrals]]


The computation of integrals can be done without any knowledge of what actually is an integral. In order to understand that concept we need to explain what the **fundamental theorem of calculus** is: 

## Fundamental theorem of calculus:
Before advancing into the theorem some definitions must be given. These definitions will conclude in the explanation about what is an integral. 

### The area below a function:
Given some function f(x), **the area below it** can be approximated with some number of rectangles. Even if the function is curved we can try and fit rectangles inside of it. 
Computing the area of those rectangles is easy (height times base) and therefore if we could somehow have **infinitely many rectangles** that approximated to the function really tightly it would give us a really good approximation of the area below that function. 

This idea is exactly what the definite integrals are all about. 
#### Definite integrals:
+ [[20240620 - 192729 - Definition - Definite Integrals|Definition - Definite Integrals]]

### Definition: 

Given all of these we can properly introduce the fundamental theorem of calculus: 
+ [[20240620 - 191531 - Theorem -Fundamental theorem of calculus|Fundamental theorem of calculus]]

## Improper integrals: 
When f is defined on an infinite interval we have [[20240620 - 201418 - Improper Integrals|Improper Integrals]]. These integrals are computed through limits. 

## Areas, Volumes and lengths: 
Because the integrals are performing an infinite sum to compute areas below the graph of a function, we can easily use them to compute areas in general and even expand this idea to volumes and lengths: 

### Areas in the plane: 

1. **Area delimited by the graph of a function f and the lines x = a and x = b:** 
$$
A = \int_a^b |f(x)| dx
$$
2. **Area delimited by the graph of TWO functions g and f and two horizontal lines x = a and x = b**
$$
A = \int^b_a |f(x) - g(x)| dx
$$
### Volumes: 

1. **Knowing the area of each cross section of three dimensional volume as A(x).**
$$
V = \int_a^b A(x) dx
$$
2. **Rotation of the graph of f around the X axis**
$$
V = \pi \int_a^b (f(x))^2 dx
$$
3. **Rotation of the graph of f around the Y axis:**
$$
V = 2\pi \int^b _a xf(x) dx 
$$
### Lengths of curves: 

1. **Length of the graph of a function f(x) bounded in an interval:**
$$
L = \int^b_a \sqrt{1 + (f'(x))^2}dx
$$

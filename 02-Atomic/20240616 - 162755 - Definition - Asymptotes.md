---
aliases:
  - Definition - Asymptotes
  - Asymptotes
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-06-25
sr-interval: 5
sr-ease: 244
---
# Asymptotes: 

> [!NOTE] Definition: 
> An asymptote of a function f as $x\rightarrow \infty / -\infty$ is another function g such as: 
> $$
> \lim_{x\rightarrow \infty / -\infty}(f(x) - g(x)) = 0
> $$ 

During the #calc we’ll only study asymptotes that are **straight lines**. 
These straight lines can be in three orientations: Vertical, Horizontal or oblique. 

1. **Vertical asymptotes:** Are those found when **any of the side** limits of the function at $x_0$ is infinite. 
$$
\lim_{x\rightarrow x_0^{+/-}} f(x) = \pm \infty
$$

2. **Horizontal asymptotes:** Are those found when **the limit when the function tends to infty/- infty is a finite real number**
$$
\lim_{x\rightarrow \pm \infty} f(x) = a
$$

3. **Oblique asymptote or Slant asymptote**: Are those found when **the limit when f tends to infty/-infty is a line: $y = mx +b$**. In order to find if there are any oblique asymptotes we must perform two checks: 

The limit of f divided by x must be finite and the solution will be the slope of the asymptote.
$$
m = \lim_{x\rightarrow \infty}
\frac{f(x)}{x}
$$

In order to obtain the “ordenada en el origen (b)” we must find a finite limit such as: 
$$
b = \lim_{x\rightarrow \infty} (f(x) - mx)
$$
+ Same thing happens if x → $-\infty$ 

**Remarks:**
+ Vertical asymptotes wont be at points where f is continuous. Could be at the end of f. 

+ A graph can **cut an horizontal or sland asymptote** but never a vertical one. → Goes agains the definition of function. 

+ The **polynomials that are not a straight line** NEVER HAVE STRAIGHT ASYMPTOTES
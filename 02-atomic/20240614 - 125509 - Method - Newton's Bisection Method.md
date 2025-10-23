---
aliases:
  - Method - Newton's Bisection Method
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-07-09
sr-interval: 19
sr-ease: 270
---
# Newton’s Bisection Method: 

This method is used to **find a root of a continuous function f on a closed interval \[a,b\]** using [[20240614 - 123841 - Theorem - Bolzano|Theorem - Bolzano]]. 

The idea is to reduce the interval by half. If once reduced we obtain that the value at the half is 0 then nice, we have found a root. If it is not 0, then it’s either a value bigger or smaller than 0 and we can apply the method again on a smaller interval. 

1. Compute $f(\frac{a+b}{2})$ 
	1. If $f(\frac{a+b}{2})$ = 0 => Finished
2. Else, use the smaller interval as a new starting point. 
3. Repeat until arrived to the desired accuracy




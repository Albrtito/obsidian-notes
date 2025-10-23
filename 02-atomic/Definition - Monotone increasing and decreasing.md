---
Date: 2024-03-19
tags:
  - calc
"References:": 
sr-due: 2024-08-14
sr-interval: 106
sr-ease: 292
---

> [!NOTE] Definition:  
> A sequence is can increase or decrease. We are interested on those sequences such as the increase or decrease is constant. Namely, they keep increasing or decreasing all the time. 
> ![Pasted image 20240319135228](../99%20-%20Meta/0.%20Attachments/Pasted%20image%2020240319135228.png)
> + We like A: It increases monotone (increases all the time)
> + Don't like B: Does not increase monotone (changes between increasing and decreasing)
> 
> **Formally defined:**
> A sequence is **monotone increasing** if $\forall n \in N$ we have: 
> $$
> a_{n+1} >= a_n
> $$
> + If $a_{n+1} > a_n$ we say **strictly increasing**
> 
> A sequence is **monotone decreasing** if $\forall n \in N$ we have:
> $$
> a_{n+1} <= a_n
> $$
> + If $a_{n+1} < a_n$ we say **strictly increasing**


**Remark:**
+ If a **whole sequence** is **positive** then: **CONDITION:** Whole sequence needs to be positive
	1.  We can say that the sequence is **monotone increasing when:**
		$$
			a_{n+1}/a_n >= 1:\forall n\in N
		$$
	2. We can say that the sequences is **monotone decreasing when:**
		$$
		a_{n+1}/a_n <= 1:\forall n\in N
		$$
This works because if every term is smaller than the next one, the division must be bigger than one. But if it's grater, then it must be decimal.
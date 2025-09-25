---
aliases:
  - Not a perfect square
tags:
  - calc
"References:": 
cssclasses: 
sr-due: 2024-06-22
sr-interval: 8
sr-ease: 250
---
**# Proof - Not a perfect square: 

> [!NOTE] Proof
> 
Given $n \in N$ **not a perfect square**, prove that: 
>$$
\sqrt{n} \not \in \mathbb{Q}
>$$
>**Hint:**  Write n as $n = z^2r$ where: 
>+ r is a number with no squares

This poof is based on the **reductio ad absurdum**, we’ll start assuming something and we’ll try to obtain an impossible or absurd result that cannot happen at the same time that our initial assumption.
Our initial assumption will be that n is rational. Then n can be expressed as a fraction ($p^2/q^2$). (Squared because n is inside an square root). We also assume that those numbers p and q have no common divisor other than 1. Because it cannot be a perfect square. 

1. Take p and q both integer numbers such as: 
$$
\gcd (p,q) = 1
$$
and: 
$$
{p^2\over q^2} = n
$$
2. Taken this definition we now have that: 
$$
p^2 = n \cdot q^2 = z^2q^2r
$$
Then: 

**NOTE:** Here we don’t really care what k is. It can be obtained, but by properties we know that if $p^2$ depends on something times r, then also p will. 

$$
p = r \cdot k 
$$
3. Redefine p: 
$$
r^2k^2 = z^2q^2r
$$
We can simplify to obtain: 
$$
q^2 = {k^2 \over z^2} r
$$
This means that: 
$$
q = r \cdot m
$$
4. We have obtained a contradiction because of the multiplicity of r in both p and q. This means that our initial assumption is not correct. 
The contradiction: 
$$
gcd(p,q) \geq r
$$

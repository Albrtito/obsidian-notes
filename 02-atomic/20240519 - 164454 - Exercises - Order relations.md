---
aliases:
  - Exercises - Order relations
tags:
  - discrete
"References:":
  - "[[Discreta_Exercises_All_Solved.pdf]]"
  - "[[20240519 - 165004 - Order Relation|Order relations]]"
cssclasses:
  - page-manila
sr-due: 2024-05-23
sr-interval: 4
sr-ease: 248
---
# Exercises - Order relations

## 13.1: 
+ **Obtain the Dom and Image:** Because it is reflexive the image and domain are equal to A.
+ **Obtain the Hasse diagram:** Apply the algorithm
+ **Obtain a total order compatible with R**: We can directly obtain $1\preceq 2 \preceq 3 \preceq 4 \preceq 5$
## 13.2: 
Let A the set A = {0, 1, 2} × {2, 5, 8}, and let us define the order relation R on A such that (a, b)R(c, d) ⇔ (a + b) | (c + d). Find the maximal, minimal, maximum, and minimum elements of the poset (A, R)

First we transform the relation into a more comprehensible form by obtaining the value of the sum of the coordinates at each point.
After doing so we can create the Hasse graph with those values and see that: 
+ There is no maximum or minimum
+ The maximals and minimals are directly obtained following the rules:
**Remember:**
**Maximals**: Those nodes that have no edges from them to another node. (No outgoing edges). (remember than with Hasse graphs, even if the arrows are not drawn the edges are directed)

**Minimals:** Those nodes with **no incoming edges** 

**Maximum:** A node such as it **is a maximal** and no other node is also a maximal
**Minimum:** A node such as it **is a minimal** and no other node is a minimal.

## 13.3: 
Let us consider the relation R on R2 given by $$(a, b)R(c, d) ⇔ a ≤ c \text{ and } b ≤ d $$ Find the maximal and minimal elements of the set $$C ⊆ R_2: C = {(x, y) ∈ R_2 : x^2 + y^2 = 1} $$Find sup(C) and inf(C) by considering C as a subset of R2.

Set C is defining all the points that exist in the **unit sphere of radius 1**. 
For all of those values, we obtain that all the maximals (those for which no value relates with **them**) are the points where x and y are both positive. 
All the minimals (points that relate with no one) are the ones when x and y are both negative. 

**maximals:** $\{(x,y) \in C / x, y \geq 0\}$
**minimals:**$\{(x,y) \in C / x, y \leq 0\}$

The supremum and minimum is found by deducing that for any point of A to be greater than any point of C, then this point has (x,y) both greater or equal to 1. Then the minimum of these points is (1,1)

The infimum is obtained in a similar way, however this time the point must have (x,y) smaller or equal to -1. Then the **infimum is (-1,-1)**

## 13.4: 
Let A be the set A = {n ∈ Z : 2 ≤ n ≤ 12}, and let us define on A the order relation R given by: n R m ⇔ n | m, or n is prime and n ≤ m . 

Tell the maximal, minimal, maximum, and minimum elements of the poset (A, R)

**Just painting the Hasse graph, solution with exercises**

## 13.5: 
Consider the two binary relations on set N:
$$
\begin{aligned}
& a \mathcal{R}_1 b \Leftrightarrow \exists n \in \mathbb{N} \text { such that } a=b^n, \\
& a \mathcal{R}_2 b \Leftrightarrow \exists n \in \mathbb{N} \cup\{0\} \quad \text { such that } a=b^n .
\end{aligned}
$$
1. Show that $\mathcal{R}_1$ is an order relation. Is $\mathcal{R}_2$ also an order relation? Is $\mathcal{R}_1$ a total order?

In order to show that it is an order relation we need to show that the three properties of order relations comply: 
+ **Transitivity:** 
+ **Anti-symmetry**
+ **Reflexivity:**

We conclude.
+ The R1 relation is an order relation.
+ The R2 relation is also an order relation as the 0 does not affect the three properties. 
+ R1 is not an total order: Total orders need for all the elements to be related to another one(besides itself). Based on the definition, prime numbers won’t be able to relate to any other number. 

2. Find the Hasse diagram of both relations on the set
$$
A=\{n \in \mathbb{N}: 1 \leq n \leq 9\}
$$
3. Find for $\mathcal{R}_1$ and $\mathcal{R}_2$ the maximal, minimal, maximum, and minimum elements on $A$. Find also the supremum and infimum of $A$ as a subset of $\mathbb{N}$

Minimal and maximal elements are directly obtained from the Hasse diagram. Only for the R2 relation is there anything else but maximals and minimals. The R2 relation has a minimum at 1 and an infimum at 1. Any other maximums, minimums, infimums or supremums do not exist. 

See that 1 is an infimum even while it is inside the set A. Also observe that for any value of N to be an infimum or a supremum it should be below(infimums) every other node in the Hasse graph, **and connected to them** or above (supremums)

## 13.6: 
Let us consider the cycle $C_4=\left(V_4, E_4\right)$ with labelled vertices $V_4=\{a, b, c, d\}$.
1. If $A$ is the set of the spanning subgraphs of $C_4$ :
$$
A=\left\{G=\left(V_4, E\right) \mid E \subseteq E_4\right\},
$$
compute the cardinal of $A$.

All spanning subgraphs of A is given by all the possible edges of a cycle graph that E could contain for those four vertices. There are 16 of these possible combinations. 
$$
 |A| = 16
$$
1. We define on $A$ the following equivalence relation $\mathcal{R}$ : if $G_1, G_2 \in A$,
$$
G_1 \mathcal{R} G_2 \quad \Leftrightarrow \quad G_1 \text { is isomorphic to } G_2 \text {. }
$$

Find the equivalence classes $[G]_{\mathcal{R}}$, and the quotient set $C=A / \mathcal{R}$.

The equivalence classes are given by the form of the spanning graphs. First divide them by the number of edges. This automatically creates 5 classes, for those 5 classes all minus the one with 2 edges are already an equivalent class. 
The class of spanning graphs with 2 edges can be divided between those that represent the perfect matching of the cycle graphs (parallel edges) and those that have an L form. 
In total 6 equiv classes. 

3. We now define the order relation $\preceq$ on the quotient set $C$ as follows: $[A]_{\mathcal{R}} \preceq[B]_{\mathcal{R}}$ if and only if there exist graphs $G_1=\left(V_4, E_1\right) \in[A]_{\mathcal{R}}$ and $G_2=\left(V_4, E_2\right) \in[B]_{\mathcal{R}}$ such that $E_1 \subseteq E_2$. Find the Hasse diagram associated to the set $(C, \preceq)$. Is $(C, \preceq)$ a totally ordered set?

The Hasse diagram is obtained with all classes in line but the c2 class (the graphs with 2 edges) that are in the same level. This means that it is **not a complete order**

4. Let $Z \subset C$ be the subset of $C$ containing the classes of equivalence that contain at least one representative with two edges. Compute $\sup (Z)$ and $\inf (Z)$.

The supremum will be C3 while the infimum C1

## 13.7: 
Prove that for all n in N the following equation holds: 
$$
	3 | (4^n - 1)
$$
Use induction to prove in all N: 
1. **Base case:** Prove for n = 1
2. **Assumption:** Assume that it works for some n = k
3. **Prove for n = k+1**: Use the following: 
$$
3 | (4^{k+1} -1 ) \rightarrow 3 | (4^k(3 +1)-1) \rightarrow 3|(4^k\cdot 3 + 4^k-1)
$$
This proves for n = k+1 as 3 divides anything multiplied by 3 and also divides $4^k -1$ as proven in step 2. Then the sum can also be divided by 3. 

## 13.8: 
A polygon P is convex if, for any two points a, b ∈ P , the segment ab joining both points is totally contained inside the polygon. Prove that the sum of the interior angles of a convex polygon of n ≥ 3 sides is (n − 2)π.

This could be proven directly by explaining the following? 
For any polygon with n vertices, we can divide the polygon into n-2 triangles by taking one of the vertices and tracing a line from that vertex to every other vertex besides the two contiguous to it. This creates n-3 lines that divide the polygon into n-2 triangles. 
All triangles have as vertices vertices of the polygon. This means that summing the angles of all the triangles will conclude in the sum of the angles of the polygon, with each triangle having a total angle sum of pi. The final sum is: 
$$
(n-2)\pi
$$

However this problem can also be solved by using induction. 
## 13.9:
Prove that 1 + $2^n$ $< 3^n$ for each n $\geq 2$

Using induction: 
1. **Base case:** n = 2
$$
1 + 2^2 < 3^2; 5 < 9
$$
2. **Assume for n = k** 
$$
1 + 2^k < 3^k
$$
3. **Prove for n = k +1**
$$
1 + 2^{k +1} < 3^{k+1} \Rightarrow 1 + 2^{k} \cdot 2 < 3^{k} \cdot 3 \Rightarrow (1/2 + 2^{k}) < {3^{k} \cdot 3 \over 2}
$$
$$
(1/2 + 2^{k}) < 1 + 2^k <3^k < {3^{k} \cdot 3 \over 2}
$$

## 13.10: (not-done) 
Prove using induction that the number of odd–degree vertices in any graph G is an even number.

## 13.11: (not-done)
Prove by induction that the Fibonacci numbers Fn and Fn+1 are relatively prime for all integer 
$$
n ≥ 0: Fn = Fn−1 + Fn−2 , n ≥ 2 , F0 = 0 , F1 = 1 . 
$$
Hint: You do not need to solve the recurrence equation to perform the proof.
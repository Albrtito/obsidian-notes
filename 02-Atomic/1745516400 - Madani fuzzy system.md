---
aliases:
  - Madani fuzzy system
tags:
  - ai
References: 
cssclasses:
---
# Mamdani fuzzy system
1. Fuzzification
2. Rule evaluation
3. Composition 
4. Defuzzification

## 1. Fuzzification:
It turns the data either into a: 
+ **fuzzy singleton:** Data do not have noise, nice and single value
+ **fuzzy set:** Data has noise, more values

## 2. Evaluation:
1. **Match the fuzzified inputs with antecedents** #duda Why the antecedentse? What is the antecedents?
	+ This can be done by matching the disjunction(OR) of the rule antecedents of matching the conjunction (AND) of the rule antecenteds
2. **Compute the consequent** by applying either clipping or scaling of the antecent. 

	+ **Clipping:** Most common method, faster and less complex, easy to defuzzify
		$$
		Q(x) = min(S, \mu_c (x))
		$$
		>f.e ![[1745516400 - Madani fuzzy systemj.png|center|300]]
	+ **Scaling:** Try to preserve more the original shape, loses less info
		$$
		Q(x) = S \cdot \mu_c (x)
		$$
		>f.e ![[1745516400 - Madani fuzzy systemj-1.png|center|300]]

## 3. Aggregation: 
Unification of the outputs of all rules. In order to do so we can use different **aggregation rules:**
+ max
+ sum
+ min
+ etc..

> f.e Given two outputs of two rules we can apply the union (max value between both) to obtain a result
> ![[1745516400 - Madani fuzzy systemj-2.png]]


## 4. Defuzzification
IN order to turn the fuzzy output into a **single crisp number** there are different defuzzifying methods:

+ Centroid of Area
+ Bisector of Area
+ Mean of maximum
+ Smallest of maximum 
+ Largest of maximum

**Remarks:**
+ The moment of defuzzification can produce undesired results, it usually requires fine tunning
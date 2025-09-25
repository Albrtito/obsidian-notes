---
sr-due: 2024-03-14
sr-interval: 1
sr-ease: 210
---
---
Date: 2024-03-12
Class: #logic  
Chapter: 4 
References: 

---
1. We all are students
2. Juan is a student
3. Juan is everybody's friend
4. Some people are Juan's friends
5. We all are friends
6. Everything is blue
7. Maria si blonde
8. Every person from madrid is spanish
9. Everybody who has a car license is over 18 
10. Some students at this University are from Madrid
11. Some Republicans are rich 
12. All Republicans are rich 
13. There is no one who is Republican and not rich
14. In every couple of neighbors there is someone who is envious 
15. All who are neighbors hate each other 
16. All computer science students are friends of all fans of logic 
17. Some students of computer science have friends that are fans of logic
18. Some computer science students are friends only of fans of logic 
19. All partners of Juan are fans of Betis 
20. There are Betis players whose family members are all Portuguese 
21. Some French are friends of any Spaniard 
22. Only football players admire football players
23. Only fools are fooled by sellers 
24. Antonio is fooled by Juan
25. All who help Juan work at Manolo’s home 
26. Some plants do not have flowers 
27. Every building is stable 
28. Some people are unbearable 
29. There are people who do not eat meat 
30. All cats are mammals 
31. All mammals have hair 
32. Juan shaves those who do not shave themselves 
33. All the nights of the round table are loyal to Arthur
34. Some roadrunners are smart
35. All coyotes chase a roadrunner (the roadrunner doesn’t have to be the same one)
36. Arturo is married to Geneva
37. Marco is friend of those who help him
38. Nobody is interested in Opera and Heavy Metal at the same time
39. Everything is spatial or not material
40. There is nothing spatial and material at the same time
41. Some things are not material
42. Nothing is extense
43. If everything is material, then there are things that are extense
44. If everything is easy and enjoyable, then Isabel will not study
45. There are no things that are not nice
46. If everything is simple or easy, then Fernando will do the job
47. It is not true that there are things that are not simple and there are things that are not easy
48. If storks are birds of prey, then they fly
49. Stephen admires someone
50. Everyone admires philosopher Plato
51. Daniel learns from a teacher
52. They all either love or hate Bono
53. If Burgos is located at the North of Madrid, something is located at the North of Madrid
54. Something is linked to everything (directional link)
55. Everything is linked to something (directional link)
56. Some dogs bark at every child
57. A person x is a grandparent of another one, z, if and only if x is a parent of a third one, y, who is a parent of z.
58. John does not have any brother, but he has a cousin.
59. If two people are brothers then, if they have children, the newborns are cousins
60. Nobody is a brother of his parent
61. Not everyone is a parent of someone
62. No one is the son of everybody
63. If Albert and John are cousins, John's father's is the uncle of Albert




1. Some computer science students are friends only of fans of logic

$$ \exists x \forall y (C(x) \land L(y) \rightarrow F(x,y)) $$

2. All partners of Juan are fans of Betis

$$ \forall x (P(j,x) \rightarrow B(x)) $$

If x is a partner of Juan (j) then x is a fan of Betis.

3. There are Betis players whose family members are all Portuguese

$$  \exists x \forall y (C(x) \land L(y) \rightarrow F(x,y)) l \exists x \forall y (C(x) \land L(y) \rightarrow F(x,y))  x (B(x) \land P(x)) $$

In this case P means: “The familiy of x is portuguese”

However in order to say the same thing we could create y to be a family member and then set it to portuguese.

$$ \exists x\forall y (B(x) \land F(x,y) \rightarrow P(y)) $$

In this case if x is a betis player and y is a family member of x then y is portuguese. This is valid for some x and all y.

1. Some French are friends of any Spaniard

$$ \exists x \forall y (F(x,y)) $$

1. Only football players admire football players

$$ \forall x (A(x) \rightarrow F(x)) $$

If you admire football players then it’s suficient condition to say you are a football player. If we can negate both an change the dir of the arrow so it still makes change then it’s right

1. Only fools are fooled by sellers

$$ \forall x \forall y (F(x) \land S(y) \rightarrow $$

1. Antonio is fooled by Juan
2. All who help Juan work at Manolo’s home

$$ \forall x(H(x,j) \rightarrow M(x)) $$

1. Some plants do not have flowers

$$ \exists x (\lnot F(x)) $$

1. Every building is stable

$$ \forall x(S(x)) $$

1. Some people are unbearable

$$ \exists x ((U(x)) $$

1. There are people who do not eat meat

$$ \exists x \lnot E(x) $$

1. All cats are mammals

$$ \forall x (C(x) \rightarrow M(x)) $$

1. All mammals have hair

$$ \forall x(M(x) \rightarrow H(x)) $$

1. Juan shaves those who do not shave themselves

$$

$$



$$ F(a,j) $$


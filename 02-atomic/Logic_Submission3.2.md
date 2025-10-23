---
tags:
  - logic
---
2. **Formalize the following deduction and verify whether it's correct, using proof with assumptions (\*).** 
	+ You must be a good programmer either to pass or work for a company. 
	+ You will neither pass nor program well unless you are patient. 
	+ It is clear that I ‘ll pass or I’ll have a fight with my parents. • If I fight with my parents, I program well. 
	+  I can conclude that I have patience.
	a: pass 
	e: work in a company
	b: program well
	p: have patience
	r: fight with my parents
	$a \lor e \rightarrow b,  \lnot(\lnot a \land \lnot b) \rightarrow p, a\lor r, r \rightarrow b \Rightarrow p$ 
	1. Premise 1: $a \lor e \rightarrow b$
	2. Premise 2: $\lnot(\lnot a \land \lnot b) \rightarrow p$
	3. Premise 3: $a\lor r$
	4. Premise 4: $r \rightarrow b$
	5. Morgan laws 2: $\lnot \lnot a \lor \lnot\lnot b \rightarrow p$
	6. Double negation elimination 5: $a\lor b \rightarrow p$ 
	7. Assumption CT (I): r
		1. MP 4,7: b
		2. Addition Rule 8: $a\lor b$
		3. MP 6,9: p
	8. Assumption CT (II): a
		1. Addition Rule 11: $a\lor b$
		2. MP: 6,12 : p
	9. Close Assumption CT: p 
5. **Formalize the following deduction and verify whether it is correct, using proof with assumptions (\*):**
	+ f you're talking you are human.
	+ If you have nothing to say, do not talk.
	+ Only if you have something to say, you're an intelligent life form.
	+  If you're human, and you have something to say, you are a good conversationalist.
	+ You're not intelligent or you are a human. 
	+ Therefore, if you speak or you are intelligent, you're a good conversationalist.
	h: talk 
	s: be human
	t: have something to say
	i: intelligent
	c: good conversationalist
	$$
		h\rightarrow s, \lnot t \rightarrow \lnot h, i\rightarrow t, s\land t\rightarrow c, \lnot i \lor s \Rightarrow h \lor i \rightarrow c
	$$
	1. DT: $h\rightarrow s, \lnot t \rightarrow \lnot h, i\rightarrow t, s\land t\rightarrow c, \lnot i \lor s, h \lor i \Rightarrow c$
	2. Premises numbered from 1 to 6
	3. Assumption CT (I): h
		1. MP : s
		2. Contraposition 3: $h\rightarrow t$ 
		3. MP : t
		4. Product Rule: $s\land t$ 
		5. MP: c
	4. Assumption CT (II): i 
		1. MP: t
		2. Disjunctive Syllogism: $\lnot i \lor s \rightarrow (\lnot \lnot i \rightarrow s)$
		3. MP: $\lnot \lnot i \rightarrow s$
		4. Double negation elimination: i 
		5. MP: s
		6. Product rule: $s\land t$
		7. MP: c
	5. Close assumption: c
6. $p\land q \rightarrow (r\rightarrow s), r\land \lnot s\Rightarrow t \rightarrow \lnot(p\land q)$
	1. Deduction theorem: $p\land q \rightarrow (r\rightarrow s), r\land \lnot s,t\Rightarrow  \lnot(p\land q)$
	2. Assumption RA: $p\land q$
		1. MP: $r\rightarrow s$
		2. SR 3: r
		3. SR 3: $\lnot s$
		4. MP: s
	3. Close assumption RA: $\lnot(p\land q)$
9. $\lnot(p\lor q), \lnot p \rightarrow (r\land t) \Rightarrow r$
	1. Assumption RA: $\lnot r$
		1. Assumption RA: $\lnot p$
			1. MP: $r\land t$
			2. SR 5: r
		2. Close Assumption RA: $\lnot \lnot p$
		3. Double negation elimination: p 
		4. Addition rule 8: $p\lor q$
	2. Close assumption RA: $\lnot \lnot r$
	3. Double negation elimination: r
13. $\lnot(p\land q),\lnot p \rightarrow r, \lnot q \rightarrow s \Rightarrow r\lor s$
	1. Morgan Law 1: $\lnot p \lor \lnot q$
	2. Assumption CT (I): $\lnot  p$ 
		1. MP: r
		2. Addition Rule: $r\lor s$
	3. Assumption CT (II): $\lnot q$
		1. MP: s
		2. Addition Rule: $r\lor s$
	4. Close Assumption CT: $r\lor s$
15. $a\rightarrow b, b\rightarrow c, \lnot c, d\rightarrow c \Rightarrow d\rightarrow \lnot(a\lor b)$
	1. DT: $a\rightarrow b, b\rightarrow c, \lnot c, d\rightarrow c, d\Rightarrow \lnot(a\lor b)$
	2. Assumption RA: $a\lor b$
		1. Assumption CT(I): a
			1. MP: b 
			2. MP: c
		2. Assumption CT(II): b
			1. MP: c
		3. Close Assumption CT: c
	3. Close Assumption RA: $\lnot (a\lor b)$

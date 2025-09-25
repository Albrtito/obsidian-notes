Date: 2024-02-19
Class: #logic 
Chapter: 
References: 

---

Llegar a la formula desde los axiomas: 
1. $p\rightarrow (\lnot\lnot p \rightarrow p)$
	1. A1: $A\rightarrow(A\rightarrow A)$
	2. A8: $A\rightarrow(\lnot \lnot A \rightarrow A)$
2. $(p\land q\rightarrow p)\lor p$
	1. A4: $p\land q\rightarrow p$
	2. A5: $p\land q\rightarrow p \rightarrow (p\land q\rightarrow p) \lor p$
	3. MP: $(p\land q\rightarrow p)\lor p$
3. Proof of no contradiction: $\lnot (A\land \lnot A)$
	1. A4: $A\land \lnot A \rightarrow A$
	2. A4: $A\land \lnot A \rightarrow \lnot A$
	3. A7: $(A\land \lnot A \rightarrow A) \rightarrow ((A\land \lnot A \rightarrow \lnot A)\rightarrow \lnot (A\land \lnot A))$
	4. MP (twice): $\lnot (A\land \lnot A)$
4. $A\land C\rightarrow A\lor B$
	1. A2: $(A\land C \rightarrow A )\rightarrow (((A\land C)\rightarrow (A\rightarrow A\lor A ))\rightarrow (A\land C\rightarrow A\lor B))$
	2. A4: $A\land C \rightarrow A$
	3. A5: $A \rightarrow A\lor B$
	4. A1: $(A \rightarrow A\lor B)\rightarrow ((A\land C) \rightarrow (A \rightarrow A\lor B))$
	5. MP: $A\land C\rightarrow A\lor B$
5. ...
6. ** Usando el Axioma A6 comprueba que la deducción siguiente es correcta. 
$$
	p \lor q, p\rightarrow r, q\rightarrow r\Rightarrow r
$$
A6: $(p\rightarrow r)  \rightarrow ((q\rightarrow r)\rightarrow (p\lor q \rightarrow r))$
MP: r
7. ...
8. ** Usando axiomas A2 y A3 comprueba que la deducción siguiente es correcta. 
$$
p\rightarrow q, p\rightarrow(q\rightarrow r), p \Rightarrow p\land r
$$
Need to get r: A2: A = $p\rightarrow q$ B = $p\rightarrow(q\rightarrow r)$  C = r
A3: $p \rightarrow (r\rightarrow p\land r)$
MP

9. ** Usando los axiomas A7 y A8 comprueba que la deducción siguiente es correcta: 
$$
	\lnot p \rightarrow q, \lnot p\rightarrow \lnot q \Rightarrow p
$$
A7: $(\lnot p \rightarrow q)\rightarrow ((\lnot p \rightarrow \lnot q)\rightarrow \lnot \lnot p)$
MP: $\lnot \lnot p$
A8: p 

10. ** Usando los axiomas A3, A4, A5 comprueba que la deducción siguiente es correcta. 
$$
	p \land q, s \Rightarrow (q\lor r)\land (p\land s)
$$
**Objective:** Use A3 to get the AND
	A3: $(p\lor r) \rightarrow ((p\land s) \rightarrow(p\lor r)\land (p\land s ))$
	
Get p and q from the expression using A4. 
A4: $p\land q \rightarrow p , p \land q \rightarrow q$
Build the or using A5. 
A5: $q \rightarrow q\lor r$
Build the and using A3: 
A3: $p \rightarrow (s\rightarrow p\land s)$
Use Modus Ponen's to obtain the separated formulas. 
MP: $(p\land r) , (p\land s )$
Apply the objective in A3 with MP to obtain the result: 
MP: $(p\lor r)\land (p\land s )$

11. ...
## Teorema de la deducción: 

12. Indicar en la columna en blanco las fórmulas válidas y las deducciones correctas que podemos obtener aplicando el TD a la expresión dad de todas las fórmulas posibles. Poner todos los paréntesis necesarios. 
	

| **Fórmula válida** | **Dedución Correcta** |
| ---- | ---- |
| $(\lnot q \rightarrow r)\rightarrow ((\lnot q \rightarrow \lnot r)\rightarrow(\lnot \lnot q))$ | $\lnot q \rightarrow r, \lnot q \rightarrow \lnot r \Rightarrow \lnot \lnot q$ |
| $(\lnot p\lor q \rightarrow s) \rightarrow (r\rightarrow (q \rightarrow s))$ | $(\lnot p\lor q \rightarrow s) ,r ,q \Rightarrow s$ |
| $s \rightarrow (p \rightarrow  \lnot t) \rightarrow (s\land (t\rightarrow \lnot p))$ | $s, (p\rightarrow \lnot t)\Rightarrow s\land (t\rightarrow \lnot p)$ |
| $r \rightarrow (s\rightarrow (\lnot p\rightarrow r\land s))$ | $r, s,\lnot p \Rightarrow r\land s$ |
| $\lnot (r\rightarrow (s\rightarrow (\lnot r\lor \lnot s)))$ | Cannot apply |
| $(s\land \lnot \lnot p) \rightarrow (\lnot p\lor q) \rightarrow(q \rightarrow r\rightarrow r)$ | $s\land \lnot \lnot p, \lnot p\lor q, q \rightarrow r\Rightarrow r$ |

13. Comprobar si la deducción es correcta: 
$$
    q \rightarrow p \land r, p \rightarrow s, p \land s\rightarrow t\Rightarrow q\rightarrow t
$$
	1. **Premise:** $q\rightarrow p\land r$ 
	2. **Premise:** $p\rightarrow s$ 
	3. **Premise:** $p\land s \rightarrow t$ 
	4. **Deduction theorem:** q
	5. **MP** $p\land r$
	6. **A4**: p
	7. **A4**: r
	8. **MP:** s
	9. **A3:** $p\land s$ i
	10. **MP**: t
14. Demostrar el teorema de contraposición: 
$$
(A\rightarrow B)\rightarrow (\lnot B\rightarrow \lnot A)
$$
	1. **Premise:** $A\rightarrow B$
	2. **Premise:** $\lnot B$ 
	3. **A7:** $(A\rightarrow B)\rightarrow ((A\rightarrow \lnot B)\rightarrow \lnot A)$
	4. **MP:** $(A\rightarrow \lnot B)\rightarrow \lnot A$
	5. **A1:** (To obtain A then not B) $\lnot B \rightarrow (A\rightarrow \lnot B)$ 
	6. **MP:** $(A\rightarrow \lnot B)$ 
	7. **MP:** $\lnot A$
	8. **A1 + MP**:$(\lnot B\rightarrow \lnot A)$ 
15. ...
16. ...
17. Comprobar validez de la siguiente fórmula: 
$$
\lnot(r\lor t) \rightarrow (\lnot p \lor q \rightarrow (( q \rightarrow r) \rightarrow (\lnot p \land \lnot t)))
$$
	1. **Deduction theorem:**$\lnot(r\lor t),\lnot p \lor q,  q \rightarrow r \Rightarrow  \lnot p \land \lnot t$
	2. **Premise:** $\lnot (r\lor t)$ 
	3. **Premise:** $\lnot p \lor q$
	4.**Premise:** $q \rightarrow r$
	5. **Morgan law 1:** $\lnot r \land \lnot t$
	6. **MP:** $\lnot r$ , $\lnot t$
	7. **Contraposition:** $\lnot r\rightarrow \lnot q$
	8. **MP:** $\lnot q$
	9. **Interdefinitions 4.1:** $p \rightarrow q$
	10. **Morgan law 1:** $\lnot q \rightarrow \lnot p$
	11. **MP:** $\lnot p$
	12. **A3 + MP:** $\lnot p \land \lnot t$

18. ...
19. Comprobar la validez de la siguiente fórmula: 
$$
(\lnot r\rightarrow p)\rightarrow (p\lor s \rightarrow (( \lnot (q\rightarrow s)\lor r)\rightarrow ((p\rightarrow \lnot q)\rightarrow q \lor r)))
$$
**Deduction theorem:**
$$
\lnot r\rightarrow p, p\lor s, \lnot (q\rightarrow s)\lor r, p\rightarrow \lnot q \Rightarrow q \lor r
$$
1. **Premise:** $\lnot r\rightarrow p$
2. **Premise:** $p\lor s$ 
3. **Premise:** $\lnot(q\rightarrow s)\lor r$
4. **Premise:** $p\rightarrow \lnot q$ 
5. 
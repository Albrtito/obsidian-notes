---
aliases:
  - Telephone number problem
tags:
  - discrete
"References:":
  - https://en.wikipedia.org/wiki/Telephone_number_(mathematics)
cssclasses:
---
The telephone number problem solves the **ways that persons can be connected through person to person phone calls in a net of n persons**. This is the same as solving the number of matchings on the complete graph of degree n. 

+ To see the number of [Perfect matchings on complete graphs](20240501%20-%20140204%20-%20Perfect%20matchings%20on%20complete%20graphs.md).
## Recurrence: 
The telephone number problem satisfies: 
$$
T(0) = 1, 
$$
$$
T(n) = T(n-1) + (n-1)T(n-2): n\geq 1
$$
+ **Fist term:** If the first person of the recurrence is disconnected then the solution is given by the previous solution(the one from T(n-1) persons).
+ **Second term:** If the first person is not disconnected then there are (n-1) possible connections of that person with the other ones in the network, for the (n-2) persons still in the network there are T(n-2) possibilities of connections. 




---
aliases:
  - CIDR Notation
  - CIDR
  - Classless Interdomain Routing
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-02-01
sr-interval: 56
sr-ease: 290
---
# CIDR Notation:
> CIDR: Classles Interdomain Routing

## Intro:
When working with IP addresses we use CIDR notation to **reference groups of IP Adresses.**

If we want to reference large groups of IPs we could just say: 
> “from the 192.34.23.0 to the 192.34.23.255

Which would theoretically include all the ones with any value in the fourth and the same values for the first three ones.

However, because we study computer science and life could not make things easier for us we opt for using another notation (sure it makes some things easier), this notation is based on **the number of bits that define the group of IP addresses we are refering to.** 

> In the previous example we could say that the first 24 bits are the ones that define the group as they never change. Then we write:
> $$ 192.34.23.0/24$$

**REMARK :** This idea of “groups of addresses” is known as [[1730827988 - Subnets|Subnets]]

Finally we can give a formal definition to this notation:

> [!NOTE] Definition:
> CIDR generalizes the notion of subnet addressing. The 32 IP address is divided into two parts in the form:
> $$a.b.c.d/x$$
> 
> + Where x indicates the number of bits in the first part of the address.
> + THe first part $a.b.c$ constitute the **network portion** and is known as **netork prefix** of the address

**Remarks:**
+ Usually organizations will have some base prefix and then create subnets from that.
+ Routers use this notion of prefixes to optimize routing algorithms and write in this form into the routing tables.

#duda: Según CIDR, las redes 192.168.45.3/24 y 192.168.45.0/24 son las mismas?
***
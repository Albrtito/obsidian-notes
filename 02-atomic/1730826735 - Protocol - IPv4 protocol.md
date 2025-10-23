---
aliases:
  - IPv4 protocol
  - IPv4
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-11-28
sr-interval: 6
sr-ease: 250
---
# IPv4 protocol
The IPv4 protocol is the first network addressing protocol created. It’s purpose is to d**efine the format that a datagram** (packet in the network layer) should have and **give an unique identifier to each host in the network**
## Datagram format: 

+ The packet will have a total of 20 bytes of header assuming no options.
+ Options are rarely used (deleted in the IPv6 for a reason)
+ **Because the existance of options wont allow for a direct knowledge of where the data begins the header lenght field is added**
![[Screenshot 2024-11-03 at 5.40.15 PM.png|center|400]]
### Fields:
Collection of the most important fields, or those that are not self explanatory.
+ **Version number:** Differntiate between IPv4 and IPv6 datagrams in order to know how to read it.
+ **Header lenght:** This field is used to know whether the datagram contains options or not. This allows to **know where the actual data begins**.
+ **Time to live:** Nº of max hops allowed inside the network before being dropped.
+ **Protocol:** Transport protocol being used

## IPv4 Addressing:
Each IP address is 32 bits long (4 bytes). 

$$
11000001\space 00100000 \space11011000 \space00001001
$$

+ A **total of $2^32$ ( $\equiv$ 4 billion)** possible IP addresses. 
+ Usually written in **dotted-decimal notation**. The example above would be:
  $$ 193.32.216.$$
  

+ **All interfaces must have an UNIQUE address** (See [[1731411013 - Network Address Translation (NAT)|NAT]]s for exceptions)
+ IP Networks where each host has its own IP address are called [[1730827988 - Subnets|Subnets]].
+ Addresses are written in their generalised [[1730832772 - CIDR Notation|CIDR]] notation.
+ A **broadcast address** is stablished as the $255.255.255.255$ .If a host uses this address to send information, all host connected to the network (and set to accept it) will get the info.
	+ **NOTE:** The broadcast address of each subnet can vary based on the range that that subnet takes. The broadcast address is **stablished as the last possible connection of the subnet**
	  > If a net goes from the 111.192.10.2 to - 111.192.10.24 the broadcast address will be 111.192.10.24

## Distributing addresses:

> [!BUG] Problem 
> But how do companies and hosts get their addresses? If addresses must be unique there must be some way of making sure that it stays that way.
> 

> [!check] Solution: 
> IP addresses for  organisations are given by the  ISPs. Each ISP is given some big address block that it then divides into smaller blocks for whoever is asking.
> 
> In the same way, ISPs will get their addresses by the ICANN(Internet Corporation for Assigned Names and Numbers), who also manages DNS.

+ In order to obtain this addresses from higher entities the [[1731409972 - Protocol - DHCP|DHCP]] protocol is used. 


## SOHO Subnets: 
**S**mall **O**ffice, **H**ome **O**ffice networks are everywhere. Everyone has a home network with one or two computers, an internet TV and a wireless point to connect smartphones. Same thing happens in small offices.  

> [!bug] Problem: 
>  Giving public addresses to each one of this networks is not practical due to the quantity of IP addresses but also because if the network gets bigger, similar IP addresse  would most possibly not be available


> [!check] Solution: 
> The solution is to introduce the [[1731411013 - Network Address Translation (NAT)|NAT]] (Network Address Translation) routers. This routers translate from public to local addresses. 

There are som **set addresses saved allways for SOHO subnets**, these address groupps are: 
+ `192.168.0.0/16`
+ `172.16.0.0/16`
+ `10.0.0.0/8` 



***

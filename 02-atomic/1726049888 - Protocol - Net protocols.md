---
aliases:
  - Net protocols
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-21
sr-interval: 60
sr-ease: 250
---
# Net protocols
When sending packages though the internet computers need to understand one another. This means **encoding the packages in the same way** as the one receiving them.
+ The [IETF](https://www.ietf.org/) defines public standard protocols.
**Remarks:**
+ Most protocols are public (TCP,IP) although anyone can develop a private protocol.

> [!NOTE] Definition(Kurose): 
> A protocol defines the ==format and the order== of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.
## Types by layer:
The internet is constructed as a layered architecture. For each of it’s layers there are several different protocols. 
### Application protocols: 
Main application layer protocol is DNS, a distributed database:
+ [[1728037357-dns|DNS]]

### Transport protocols:
Two main protocols are used in this layer, TCP and UDP. 
+ [[1727428429 - Definition - UDP|UDP]]
+ [[1727428451 - Definition - TCP|TCP]]
We must also mention the [[1727429612 - Definition - TLS|TLS]] tools. Used to add a layer of security to the transport layer protocols. 

### Network protocols:
The network protocols work with datagrams that encapsulate the transport layer data.
+ [[1731411683 - Procotol - IPv6|IPv6]]
+ [[1730826735 - Protocol - IPv4 protocol|IPv4 protocol]]

### Link protocols: 
The link layer has several protocols. One packet can be managed by several protocols in order to travel from one node to another.
This note collects the **important and widely used link protocols**, see the [[1732018095 - The network link layer|Link Layer]] note for other protocols such as the multiple acces protocols. 
+ [[1732018610 - Protocol - WIFI|WIFI]]
+ [[1732023041 - Protocol - Ethernet|Ethernet]]
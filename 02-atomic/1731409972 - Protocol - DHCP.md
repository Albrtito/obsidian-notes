---
aliases:
  - Protocol - DHCP
  - DHCP
  - Dinamic Host Configuration Protocol
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-01-11
sr-interval: 35
sr-ease: 270
---
# Protocol - DHCP

> [!NOTE] Intro: 
> DHCP (Dinamic Host Configuration Protocol) assignes IP addresses to hosts automatically. 
> 
> 

+ It works as a **client-server** protocol. Each subnet usually has a DHCP server. If else, the router redirects to the closest server.
+ It’s a **plug-and-play** or **zeroconf** protocol as nothing but running it needs to be done in the host. 

## Ineraction protocol:
This protocol is composed of four steps: 

1. **DHCP Client Discover:** 
   The new client sends an UDP packet to port 67 to IP Broadcast channel 255.255.255.255 and the client’s IP as 0.0.0.0. 
   
2. **DHCP Server offer(s):** 
   A DHCP or (several DHCP) servers recieve the discover message and respond with an offer message. 
   This offer is again done through broadcast channel and contains the IP being offered for the client. 
   **One client could have several IP offers**

3. **DHCP Client Request:** 
   The client chooses one or more IP addresses from the ofered ones and send a DHCP request message with the configuration it choose. 

4. **DHCP Server ACK:** The server acknowledges the request.

***
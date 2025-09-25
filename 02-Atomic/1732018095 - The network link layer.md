---
aliases:
  - The network link layer
  - Link Layer
  - The link layer
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-19
sr-interval: 8
sr-ease: 210
---
# The link layer

> [!attention] Biblio reference: 
> The wifi is really compact in the UC3M course and given with LANs. We wont be seeing the whole WIFI chapter. 
> 

> [!NOTE] Definition (MAIN IDEA):  
> The link layer has the **responsability of transferring a datagram from one node to a physically adjacent node over a link**. 
> + Connect a ONE LINK HOP via some medium
>   
> Each link is different and therefore needs a different protocol. 
> 
> The **implementation of this layer happens in each hosts**. 
>==+ A chip (link-card), specific to each protocol, is needed.== 

> [!example] Notation: 
>+ **host and routers = nodes:** From the link layer point of view all devices at the edges of the link are nodes and there are no differences between them. 
>+ **links:** The communication channels that connet adjacent nodes. There are several types. 
>+ **packet → FRAME:** The packet of the link layer is a frame, it **encapsulates the network layer packet (datagram)**
>==+ **MAC Addresses: Physical addresses: Link layer addresses:** The addresses used in the Link layer to identify hosts== 
>+ **bitTime:** The time to transmit one bit

> [!bug] Problems: 
> The main problems of the link layer are: 
> 1. There are several link mediums through wich a packet can travel. Several protocols need to be used easily. The problem is changing between protocols **fast.**

## Link layer services: 
The link layer may provide some of the following services based on the different protocols and mediums used.
### Framing:

> [!NOTE] Def: 
>  The act of creating the link frame, is directly related to the protocol used.


> [!check] Duda: Pq el channel acces protocol es algo dentro del servicio de framing?
> Porque el frame variará según el protocolo que utilice ese link.  Todo el framing coge el datagram pero no de la misma forma. 


Este servicio engloba: 
+ Creation of a **header and trailer**.
+ Use of a [[1732031831 - Link channel multiple access protocols|Channel access protocol]]. 
+ Creation of a **MAC ADDRESS** 

 **Remarks:**
+ A trailer is something added **behind the data** instead of before it.
      
### Adjacent reliable delivery:

> Already know how to do this based on the [[1727176650 - Principles of reliable data transfer|Principles of reliable data transfer]]


This service comes with a question on why it is necessary.

> [!bug] Problem, question: 
> If TCP is reliable, why is important to have a reliable link layer protocol. 
> If the link is reliable, why use TCP or any other reliable transport layer protocol ?

> [!check] Solution:
> + The retransmission of TCP packets can be avoided with a reliable link layer. Instead of retransmitting through the whole network we just need to do it over one link. 
> + Maybe if we are sure that the link will allways be reliable, it makes no sense to implement TCP. The reality is that we wont be able to really know that for sure. So better implement TCP

### Half-Full Duplex channels:

> [!NOTE] Def: 
> Based on the type of physical link being used a half or full duplex channel can be offered. 
> 
+ **Half duplex:** Only one side of the link can send at a time
+ **Full duplex:** Both sides of the link can send at the same time. 
**Remark:**
+ Altough one may think that nowadays allmost everything is full duplex, the reality is that most of the legacy internet connections are half duplex. 
> f.e: El cable coaxial
### Other services:
1. **Flow control** 
2. **Error detection**
3. **Error correctoin**

***
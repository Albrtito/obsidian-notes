---
aliases:
  - Packet switching
tags:
  - net
References: 
cssclasses: 
sr-due: 2025-01-26
sr-interval: 48
sr-ease: 208
---
# Packet switching

> [!NOTE] Definition: 
> Information on the internet is sent by hoping from one host to another until the target host is reached. Messages are not sent whole but broken down into smaller pieces, this process is called **packet switching**.  

+ An explanatory header is added to each of this packets by each of the network layers
+ Packets from **several hosts** can arrive to the same router. 
+ Pacages of one message musn’t allways travel together

This makes the network much quicker as **the links are being used constantly**. 

## Store and forward:
The transmission of packets between the routers is performed following an store and forward technique: ==**Entire packets must arrive in order for the packet to be sended to the next link**.== 
+ Router must **wait** for all bits. 
This creates [[1727255580 - Loss and delay in Networks#Transmission delay|transmission delay]]. 

## Queues: 
Each router has a queue that fills out with packets that need retransmission. This means two things:
+ The queue introduces [[1727255580 - Loss and delay in Networks#Queueing delay|queueing delay]].
+ If a packet arrives to a full queue is **lost**



***
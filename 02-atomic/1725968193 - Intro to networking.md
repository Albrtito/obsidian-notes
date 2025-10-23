---
aliases:
  - Intro to networking
tags:
  - net
References: "[[Net_Biblio_Kurose.pdf#page=28]]"
cssclasses: 
sr-due: 2025-02-16
sr-interval: 87
sr-ease: 230
---
# Intro to networking
When we talk about the internet we are just describing a **net of connected devices**, nothing more. To have a connection we only need two **devices**, a data **transmission method** and a **medium** to do it in. 

>**The telephone net:** A basic example is the telephone network where there each phone(device) is connected through a copper wire (medium) and sends electric signals to other phones (transmission method)

## Definition: Two different points of view
+ We can see the internet from a **nuts and bolts** view, focusing on the hardware, protocols, standarts,etc…
+ The internet can also be described from a service view. An **infrastructure that provides interfaces to apps**. These apps can be:
	+ **Distributed apps:** Those that need the internet to work 
	+ **Local apps:** Those that can run without the web
	 > f.e: The calculator
	 
## Fisionomía of the internet 

> [!NOTE] Host 
>We call **host or end system** to any device that is hooked to a net.  

+ Nowadays most of these end systems are portable devices while the initial host of the internet where traditional desktop workstations. 

In order to **connect all the host** to the network we use: 
+ [[1726049178 - Definition - Communication links|Communication links]] (the medium through which the signals flow) 
+ [[1726049339 - Definition - Packet switches|Packet switches]] (The middlepoints between links)

Computers communicate between them using [[1726049888 - Protocol - Net protocols|Net protocols]]. These protocols give an **standard way of establishing a communication between two nodes**. 
Anyone can create a protocol, though most protocols used are public.

### How’s all connected?
Nodes need to be connected between them, **connecting everything to everything is not viable**. So we need to hop from one node to another to reach destination. 
These hops go through a **hierarchy** structure where there are **bigger and smaller tier nodes**. 

+ ==**ISPs:** Internet Service Provider : Connects big networks between them==
	+ ==There will be some bigger national ISPs, smaller regional ISPs and even smaller acces ISPs==
+ ==**IXP:** Internet Exchange Point: Connects **ISPs** between them==
## Moving messages:
Messages are too big to be moved whole through the network. This would mean huge delays and inefficiency. In order to solve this we need to **divide the resources somehow**, this division is called **switching**, there are two types. [^1]

+ [[1727429966 - Packet switching|Packet switching]]
+ [[1727430724 - Circuit switcing|Circuit switcing]]

So **which one is better?** Depends on what ur using them for, **the internet moves packets using packet switching,** it focuses on the network as a “public” resourece. However other networks **such as the telephone network** use **circuit switching as it is the only possibility**

***
[^1]: Organisation of all of this package traffic and connections is complex, the easiest thing to do is divide it into smaller more maleable parts, this parts are called **layers,** more about them in [[1726572508 - The network stack|The network stack]].
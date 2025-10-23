---
aliases:
  - Loss and delay in Networks
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-19
sr-interval: 30
sr-ease: 205
---
# Loss and delay in Networks
When packets are transmitted through the internet they go through different links, routers or switches. **This routers save the packages arriving in a queue and transmitt the first package of the queue to the next link.** 

In order to analise the delays and losses that can appear in this network we’ll look at four stages of the packet journey in the router:
## Nodal processing:
> [!NOTE] Delay sources: 
> + **Processiong**: Checking errors and recieving package
> + **Queueing delay:** The time it stays at the queue. 
> + **Transmission:** The time it takes to send the actual package to the next link
> + **Propagation:** The time it takes to arrive to the next link. 

This way, **for each connection point** we’ll need to take into account the delay of this four sources.
This whole sum is called **nodal processing**. 

### Nodal delay/Total delay:
The delay obtained for each link after the sum of all delays.
$$
d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}
$$
#### Queueing delay: 
$$ \text{traffic intensity } = {La\over R}$$
+ ==R : Link bandwitdth (bps)==: How much can the link transmit
+ L: Packet length (bits)
+ a : average packet arrival rate (pck/s)

> **namely:** Los que entran por los que salen.Relación entre rates de salida y entrada.

Traffic intensity gives the measure of **how intense the trafic is.** 
  + La → bits comming in
  + R → bits going out
##### ==Analisis of the traffic intensity:==
  Traffic intensity can be either: 
  + Near to zero: If there is a ton of bandwith and little packages
  + Near to 1: Same bandwith and packets sent. (lots of delay)
  + Greater than one: Infinite delay. We cannot do anything with this.

#### Transmission delay:
Is defined as: 
$$
d_{trans} = L/R
$$
+ L: Packet lengh
+ R: link trasmission rate

#### ==Propagation delay:==
$$
d_{prop} = d/s
$$
+ d: ==Lenght of the physical link==
+ s: Propagation speed.

  
## Packet loss:
If the buffer of the router is full, the packet will be dropped. 
+ Can be fixed by retrasmission from last link, or methods applied in the sender/reciever

## Throughput and bottlenecks:

**Rate** at which bits are transfered. 
+ Instantaneous: A one specific momento
+ Average: Self explanatory.

This rate is given by the conneections between the different points of the network. 
+ The connections act as bottlenecks. The **smaller rate** will determine what the bottleneck is.
	+ Whatever is the smallest will always be the average throughput.
	+ Take into account that, if a shared pipe, when divided by the number of connections, is smaller than other pipes. Then this will act as the bottleneck

**Remark:**
+ **BOTTLENECKS DO NOT HAPPEN IF THERE IS ONLY 1 PACKAGE**
***
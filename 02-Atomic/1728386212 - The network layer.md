---
aliases:
  - The network layer
  - Network layer
tags:
  - net
  - incomplete
References: 
cssclasses:
---
# The network layer

> [!NOTE] Intro: 
> The transport layer is handling the proces to process, however this communication between processes depends on **host to host communication,** this is work of the network layer. 

> The comparrison used is that while the transport layer is the system used to send letters over a mailing system, the mailmain and the mail company who decide how to send them (by plane, car, train) and which routes to take would be the network layer. 


> [!Example] First, an example: 
> Before going into each part of the layer, lets thing about what happens when some host H1 wants to send to the host H2 some packages that are **created by the transport layer, remember that the network layer goes after the transport one while sending and befor it when recieving.**
>
> 1. H1 encapsulates each transport segment into a datagram and sends it into the nearest router
> 2. Magic and wonders happen inside the network layer (this is what we’ll talk about)
> 3. H2 nearest router send the datagram to H2 network layer
> 4. H2 network layer decodes and send the transport segment into the transport layer. 

From this example we can conclude that the **role of the network layer is to MOVE PACKAGES FROM ONE HOST TO ANOTHER**. 


## Names and dictionary: 

> [!example] Dictionary: 
> 
>
>+ **datagram** → A network layer packet 
>+ **data plane** → The part of the network layer that covers *per-router* functions. 
>	+ **forwarding functions** → The different functions inside the data plane
>	+ **forwarding tables** → Tables created by the control plane that tell each router were to send each package. 
>+ **control plane** → The part of the network layer that covers *network-wide* logic. Routing of datagrams
>	+ **routing protocols** → Protocols of the control pane
>	+ **routing** → The act of creating routes to move a datagram through the network. 
>	+ **SDN(Software Defined Networking)** → Implementation of the network layer that separates control and data planes.
>+ **ip forwarding** → The act of sending a datagrap to the next ip based on some algorithm. Algorithms are divided between traditional and generalised.
>+ [[1730624725 - Router|Router]] → The network layer device 
>+ **interface** → An interface is charged with connecting a host with the actual internet link. Is the **boundy between the host and the link**

> [!ATTENTION] Routers vs link-switches 
> A distinction between the routers and the link-layer switches is really important because **routers make decisions based on the network layer while switches make them based on the link layer**
> + Not to confuse link-switches with packet-switches (these are both routers and link-layer switches) 
## Two different planes: 
When moving packages between hosts we identify two main network layer functions, each of them done by one of the two planes of the network layer:


1. [[1730567078 - The network layer data plane|Data plane]]: 
	**Implements [[1730567584 - Forwarding function of the network layer|Forwarding]]:** When a datagram arrives at a router it must be *forwarded*, this means sending it to the next apropiate router in the path to its destination, blocking it or managing it.
	
   + The systems that implement this functions are the [[1730624725 - Router|routers]]. We can see more about their structure and where it’s implemented at its page. 
   
2. [[1730567097 - The network layer control plane|Control plane]]:
	**Implements [[1730567598 - Routing function of the network layer|Routing]]** Routing is identifying the paths to take over the network. This is done by **routing algorithms**
	
	+ Based on the approach to the control plane, its functions will be implemented by the [[1730624725 - Router|Routers]], specifically in their processors, or by external software systems (SDN).

### Middleboxes:
Aside the basic networking planes,needed for all of this systems to work, there are others, extra system **performing functions apart from normal,standar function of an IP router.** 

We identify three main systems of this nature:
1. [[1731411013 - Network Address Translation (NAT)|NAT]] translation
2. **Security services**
3. **Performance enhancement services.**

## Network service model:
The netwok service model could provide tons of different services, security, in-order delivery, guaranteed delivery, congestion or flow control… However **only one service is provided**, the [[1728387775 - Best effort services|best-effort service]]. 

## Network layer protocols: 
There are several network layer protocols, here is a list of them: 
+ [[1730651695 - The Internet Protocol (IP)|The Internet Protocol (IP)]] defines the format that the datagrams inside the network layer must have. 


***


---
aliases:
  - Application layer
tags:
  - net
References: "[[Net_References_s2_1.pdf]]"
cssclasses: 
sr-due: 2025-03-04
sr-interval: 85
sr-ease: 230
---
# Application layer

> [!Quote] Remember: 
> In any network, the aplicatinos that send messages through the network are called **distributed**. 

## Types of applications:
The **architecture of the application can be one of two types:**

### Server-Client:
1. **Server:** Where some common info is. It has a permanent place (permanent IP) and sends info to all the clients. 
2. **Clients:** The clients communicate with the server and not with each other. Do not need to be connected all the time

### Peer-Peer:
The peer to peer architecture uses a direct connection between hosts instead of a server-host connection. 
+ There is **no server**
+ There is a service for service mindset. (Bit-Torrent)
+ Peers are **intermittently connected**

## Communication of processes: 
Each application can be composed of one or more processes, **this processes can communciate (send messages) with other processes through the network** (also locally but we dont really care about that in networks). 
To stablish a connection the process needs to know where to loook at, here is where **sockets come in**. 


> [!Attention] Remark: 
> The application layer only knows **where to send** it, **where each process is recieving**  and with **which protocol.** 
> How to do the sending and recieving is part of **the other layers**

The messages sent are encoded with some application protocol, some protocols are HTTP(web), SMTP(mail). 
These protocols can be **public or propietary**

### Sockets: 

> [!NOTE] Definition: 
> Sockets define where each processs sends/recieves messages. Each process will have a socket that recieves data and another one that sends it (they are usually the same one)
> 

In order to **identify the socket** we use: 
+ **IP addresses**
+ **Port numbers**
> telnet: Check that we can use the telnet command to connect given an IP address and a port: 

```bash
 telnet <IPAddress> <port>
 ```

## Services: 
Applications may need different things, based on this we choose the proper [[1726049888 - Protocol - Net protocols#Transport protocols|Transport protocol]], some of the needs they may have are: 

+ Data **integrity:** Everything needs to reach ok, no corruption
+ **Throughput:** A need for a lot of packages in short times. (f.e: Video, multimedia)
+ **Timing:** A need for speed, no delay. Low latency
+ **Security:** Encryption and that type of thing

We’ll mainly focus on the **integrity and timing** of the data to decide between the two main transport protocols (TCP and UDP).




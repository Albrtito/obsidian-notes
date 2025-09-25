---
aliases:
  - TCP
  - Definition - TCP
tags:
  - net
References: 
cssclasses: 
sr-due: 2024-12-02
sr-interval: 30
sr-ease: 210
---
# TCP

> [!NOTE]  Definition:
>  TCP is a connection oriented **internet transport protocol** that offers **reliable transmission** [\^2\] of data between sender and reciever.

+ Works with **one-to-one**: One sender to one reciever
+ Data arrives **ordered and whole**
+ Offers **congestion control**[^1]
+ Offers **flow control** [^3]
+ Requires to **set up the connection** → [[1728042156 - The three way handshake|The three way handshake]] 
+ Requires a **closing connection** → [[1728044996 - Closing a TCP connection|Closing TCP]]

![[1727428451 - Definition - TCPj.png]]

## Cummulative ACKs:
It's important to mention that the ACKs in TCP are cummulative, this means that when we send an ACK for packet 3, what we are telling the sender is that **every packet until 3 has been recieved and THE LAST RECIEVED BYTE WAS 3. 

## Sequence numbering:
TCP has a **wierd way of numbering packets**.Lets first get the number of sequence numbers needed for some window of size n.
Based on the [[1727187791 - Method - RDT Sliding window|Method - RDT Sliding window]] we can say that for any sliding window with value n we’ll **need at least 2n sequence numbers to prevent any type of erros.**

TCP does not use this 2n sequence numbers but instead uses the **number of the first byte of the package** to number the whole packet. This has one really important consequence when we take into account the cummulative ACKs we see the following interactions (example):


> f.e: An interaction between sender-reciever with this sequence numbering would be:
> 
> 1. A package is sent with: 
> **Lenght: 20 bytes**
> **Seq:100**
> 
> 2. The reciever gets the package and… 
> **Sends an ACK numbered 120**. This means that all bytes until 120 have been properly recieved. Las recieved bythe number was 120
>



#duda: Are we, at any point, reusing the byte numbers? If a message has to many bytes arent we just incrementing the header on and on and on? Are there any “infinite messages”?

## Bi-Directional communication:
Al contrario que en los protocolos básicos de comunicación reliabely, TCP admits a bi-directional communication. This means that both the sender and reciever can interchange places and become the reciever and sender. 

This feature is really nice, but we **only care** about the **piggybacking** that can be done in a message. This piggybacking means that **both the acknowledgment and the message are going to travel together**. 

+ This will create **TWO SEQUENCE NUMBER SPACES**, one for each host. 
+ If we look closely at the TCP segment we can see the flags for the ACK

+ We see in the segment that both the **sequence number of the packet and the ACK** are saved.

**An example for better understanding:**
	![[1727428451 - Definition - TCPj-1.png]]

### Echoes: 
The data being send from the reciever each time it gets a package is goint to be **the last package with the same data and the corresponding ack flag**. To assure that the data has been recieved. This is called an **echo**
#duda: Reexplain this
+ It can also send its own data. Only this echo will allways be done

***

[^1]: [[1728027800 - Network congestion|Congestion control]]
[^2]: When explaining the workings of TCP we begin by assuming that the [[1727176650 - Principles of reliable data transfer|Principles of reliable data transfer]] are known, and the methods used for it are to.
[^3]: [[1728044151 - Network flow control#TCP Flow control|TCP flow control]]
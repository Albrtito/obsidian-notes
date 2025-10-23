---
aliases:
  - Practica - Routers - 2
tags:
  - net
References: 
cssclasses:
---
# Practica - Routers - 2
For this practice we’ll use a **modified version** of the [[1730716899 - Practica - IP addressing|IP Address Assignment]], with small changes to the number of hosts required for each of the networks. 


> [!check] MILESTONE:
> Compruebe que se tiene conectividad IP desde cualquier router o PC con el resto de los equipos del escenario y que la ruta seguida por los paquetes es la óptima, haciendo ping y traceroute. 
> 
> Realice un traceroute desde el hstOf1 a R100 y verifique si sigue la ruta a través de R1-R2 o de R1-R3. 
> 
> Ejecute un ping entre hstOf1 y R100 y no lo detenga. Con el ping en ejecución, desconecte las interfaces de los routers del triángulo seguidos por el ping anterior (R1-R2 o R1-R3).
> 
> Compruebe que se mantiene la conectividad global a pesar de una caída de comunicaciones en el triángulo R1-R2-R3 y verifique con un traceroute que se toma la ruta alternativa. Una vez se haya conseguido, contacte con el profesorado en clase para validar el hito 

## Requirements: 
1. **Office 1:** 100 hosts
2. **Office 3:** 25 hosts 
3. **Servers:** 10 hosts 
4. Ip addresses must be assigned optimizing the number of direcctions for each network 
### RIP Requirements:
1. RIP should not be used when no adjacent routers use RIP
2. Identify the initial router information
3. The router R100 should be accessible from office networks. 

## Address-interface assignment: 

**Remarks:** 
+ Hosts can be set up in between the router and the broadcast addresses
+ The “zero address”, broadcast and default gateway are taken into account when computing number of hosts. 

#duda: Why create an independent network for each of the server point-to-point connections. Why not create one network for all servers. 

1. **Office 1:** (Needs 100 hosts, 127 addresses are given using a /25 mask)
	+ Network: 10.0.75.0/25
	+ **Router (R1):** 10.0.75.1 (*eth0.1*)
	+ **Host (Ofi1):** 10.0.75.2 (*eth1*)
	+ Broadcast: 10.0.75.127
	  
2. **Office 2:** (Needs 25 hosts, 32 addresses are given using a /27 mask)
	+ Network: 10.0.75.128/27
	+ **Router (R2):** 10.0.75.129 (*eth0.1*)
	+ **Host (Ofi2):** 10.0.75.130 (*eth1*)
	+ Broadcast: 10.0.75.159
	  
3. **Servers:** (Needs 10 hosts, 16 addresses are given using a /28 mask ) 
	+ Network: 10.0.75.160/28 
	+ **Router (R3):** 10.0.75.161 (*eth0.1*)
	+ Broadcast: 10.0.75.175
	  
4. **R1 - R2**: (Needs 2 hosts and 1 broadcast address. Use a /30 mask)
	+ Network: 10.0.75.176/30 
	+ **Router(R1):** 10.0.75.177 (*eth0.3*)
	+ **Router(R2):** 10.0.75.178 (*eth0.2*)
	+ Broadcast: 10.0.75.179
	  
5. **R2 - R3**: (Needs 2 hosts and 1 broadcast address. Use a /30 mask)
	+ Network: 10.0.75.180/30
	+ **Router(R2):** 10.0.75.181 (*eth0.3*)
	+ **Router(R3):** 10.0.75.182  (*eth0.4*)
	+ Broadcast: 10.0.75.183
	  
6. **R1 - R3**: (Needs 2 hosts and 1 broadcast address. Use a /30 mask)
	+ Network: 10.0.75.184/30
	+ **Router (R1):** 10.0.75.185 (*eth0.2*)
	+ **Router(R3):** 10.0.75.186 (*eth0.3*)
	+ Broadcast: 10.0.75.187
	  
7. **R3-R4**:(Needs 2 hosts and 1 broadcast address. Use a /30 mask)
	+ Network: 10.0.75.188/30
	+ **Router(R3):** 10.0.75.189 (*eth0.2*)
	+ **Router(R4):** 10.0.75.190 (*eth0.2*)
	+ Broadcast: 10.0.75.191
	  
8. **R4-R100:** (10.0.0.0/24)
	+ **Router(R4):** 10.0.0.75 (*eth0.1*)
	+ **Router(R100):** 10.0.0.100 (*eth0.1*) → Assuming as nothing is sid in the picture
## Routing tables: 
**bold** → Backup connections

### R100: 

| Destination Network | Next Hop  | Interface |
| ------------------- | --------- | --------- |
| 10.0.75.0/24        | 10.0.0.75 | eth0.1    |
| 10.0.100.0/24       |           | eth0.2    |
### Backbone Router (R4)

| Destination Network | Next Hop    | Interface |
| ------------------- | ----------- | --------- |
| 10.0.100.0/24       | 10.0.0.100  | eth0.1    |
| 10.0.75.0/24        | 10.0.75.189 | eth0.2    |

### Server Router (R3)
+ This router is the **servers default gateway**

| Destination Network | Next Hop        | Interface  |
| ------------------- | --------------- | ---------- |
| 10.0.75.160/28      |                 | eth0.1     |
| 10.0.100.0/24       | 10.0.75.190     | eth0.2     |
| 10.0.75.0/25        | 10.0.75.185     | eth0.3     |
| 10.0.75.128/27      | 10.0.75.181<br> | eth0.4     |
| **10.0.75.0/25**    | **10.0.75.181** | **eth0.4** |
| **10.0.75.128/27**  | **10.0.75.185** | **eth0.3** |

### Office 1 Router (R1)
+ This router is the **Ofi1 default gateway**

| Destination Network | Next Hop        | Interface  |
| ------------------- | --------------- | ---------- |
| 10.0.75.0/25        |                 | eth0.1     |
| 10.0.75.160/28      | 10.0.75.186     | eth0.2     |
| 10.0.75.128/27      | 10.0.75.178     | eth0.3     |
| 10.0.100.0/24       | 10.0.75.186     | eth0.2     |
| **10.0.75.128/27**  | **10.0.75.186** | **eth0.2** |
| **10.0.75.160/28**  | **10.0.75.178** | **eth0.3** |
| **10.0.100.0/24**   | **10.0.75.178** | **eth0.3** |


### Office 2 Router (R2)
+ This router is the **Ofi2 default gateway**

| Destination Network | Next Hop            | Interface  |
| ------------------- | ------------------- | ---------- |
| 10.0.75.128/27      |                     | eth0.1     |
| 10.0.75.0/25        | 10.0.75.177         | eth0.2     |
| 10.0.75.160/28      | 10.0.75.182         | eth0.3     |
| 10.0.100.0/24       | 10.0.75.182         | eth0.3     |
| **10.0.100.0/24**   | **10.0.75.177**     | **eth0.2** |
| **10.0.75.160/28**  | **10.0.75.177**     | **eth0.2** |
| **10.0.75.0/25**    | **10.0.75.182**<br> | **eth0.3** |

***
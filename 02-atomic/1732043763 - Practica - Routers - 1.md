---
aliases:
  - Practica - Routers - 1
tags:
  - net
References: 
cssclasses:
---
# Practica - Routers - 1
> RSC/S16_escenario_1

> [!check] MILESTONE 
>  Compruebe la conectividad entres las redes A y B del escenario, **haciendo un ping entre PCA y PCB**. Verifique con el comando traceroute las interfaces atravesadas por los paquetes que van de PCA a PCB.

### Assigned IP addresses and interfaces:
> Subnet mask NET A: `172.16.75.0/25` 
> Subnet mask NET B: `172.16.76.0/25` 
> Subnet mask NET C (ROUTERS): `172.16.0.0/30` 


**RA:**
+ (NET A): eth0.0 → `172.16.75.1/25` 
+ (NET C): eth0.1 → `172.16.0.1/30` 

**RB:**
+ (NET B): eth0.0 → `172.16.76.1/25`
+ (NET C): eth0.1 → `172.16.0.2/30` 

**PCA:** 
+ (NET A): eth1 → `172.16.75.2/25` 

**PCB:**
+ (NET B): eth1 → `172.16.76.2/25`

## Routing tables: 

#### RA:

| TO             | NEXT_HOP | INTERFACE |
| -------------- | -------- | --------- |
| 172.16.75.2/25 | PCA      | eth0.0    |
| 172.16.76.0/25 | RB       | eth0.1    |
| 172.16.0.2/30  | RB       | eth0.1    |
#### RB:


| TO             | NEXT_HOP | INTERFACE |
| -------------- | -------- | --------- |
| 172.16.76.2/25 | PCB      | eth0.0    |
| 172.16.75.0/25 | RA       | eth0.1    |
| 172.16.0.1/30  | RA       | eth0.1    |
#### PCA:


| TO            | NEXT_HOP | INTERFACE |
| ------------- | -------- | --------- |
| 172.16.0.0/16 | RA       | eth1      |

#### PCB:


| TO            | NEXT_HOP | INTERFACE |
| ------------- | -------- | --------- |
| 172.16.0.0/16 | RB       | eth1      |



## INPUTTED CODE: 
1. **Removing IPv4 addresses from routes:**
```sh
# Los comandos de este lab son (para cada router): 
config terminal
interface eth0.0
no ip address 192.168.0.1/24
exit
interface eth0.1
no ip address 192.168.1.1/24
exit
interface eth0.2
no ip address 192.168.2.1/24
exit 
interface eth0.3 
no ip address 192.168.3.1/24

exit
interface eth0.4
no ip address 192.168.4.1/24
exit
interface wlan0
no ip address 192.168.5.1/24
exit 
exit
```

2. **Removing IP addresses from PCs**
```sh
# Ejecutar por lineas según que PC
 
	#PCA
	#Eliminamos el address de la interfaz eth1 para PCA
	sudo ip addr del 192.100.100.101/24 dev eth1
	# Este comando deja en blanco la interfaz. 
	sudo ip addr flush dev eth1

	
	#PCB
	#Eliminamos el address de la interfaz eth1 para PCB
	sudo ip addr del 192.100.100.102/24 dev eth1
	# Este comando deja en blanco la interfaz. 
	sudo ip addr flush dev eth1

```

3. **Adding new  IP addresses to PCs and default gateways**
```sh
# Los comandos de este lab son: (Ejecutar según que linea en cada PC)

	#PCA
	#Añadimos la dirección adecuada en el PCA
	sudo ip  addr add  172.16.75.2/25 dev eth1
	# Configuramos el default gateway por el router RA
	sudo ip route add default via 172.16.75.1 dev eth1


	#PCB
	#Añadimos la dirección adecuada en el PCB
	sudo ip addr add  172.16.76.2/25 dev eth1
	# Configuramos el default gateway por el router RB
	sudo ip route add default via 172.16.76.1 dev eth1
	

```

**Assigning IP addresses to the routers:**
```sh
# Los comandos de esta parte son: (Ejecutar según que linea para cada router)
	#RA: 
	# NET A
	config terminal
	interface eth0.0
	ip address 172.16.75.1/25
	exit
	
	# NET C
	interface eth0.1
	ip address 172.16.0.1/30
	exit 
	exit

	# RB:
	# NET B
	config terminal 
	interface eth0.0
	ip address 172.16.76.1/25
	exit
	
	# NET C
	interface eth0.1
	ip address 172.16.0.2/30
	exit
	exit
```

**Create the routes between the networks:**

```sh
# From RA send to NET B
	config term
	ip route 172.16.76.0/25 172.16.0.2
	exit
	
# From RB send to NET A
	config term 
	ip route 172.16.75.0/25 172.16.0.1
	exit
```

***
***
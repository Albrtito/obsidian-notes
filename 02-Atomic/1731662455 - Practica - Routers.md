---
aliases:
  - Practica - Routers
tags:
  - net
References: 
cssclasses:
---
# Practica - Routers


> [!attention] CAREFUL: 
> Collection of things to be careful about:
> + Allways run the `ping` command with the `-c4` flag. Else the ping will be eternal and a `ctrl-c` would need to be used. This can fuck thigs up. 
> + Never leave a router in configuration mode
> + All addresses must be given in [[1730832772 - CIDR Notation|CIDR]] notation. Even if the whole 32 bits are significant → ex: `123.23.23.2/32` 
> + Aunq el código tenga comentarios no se pueden añadir si son de linea

## Dudas: 
#duda: La notación CIDR impone parte de la condición para que una dirección sea diferente a otra? Pq si un PC tiene la dirección X.X.X.1 en la subnet X.X.X.0/25 tengo que referenciarlo como X.X.X.1/25 en vez de X.X.X.1/32? No sería el caso de que esa dirección viene dada por los primeros 32 bits?


## Router configurations: 
The routers have several modes to work in: 
+ **Terminal mode:** The initial mode of the router 
+ **Configuration mode:** Mode to change things, accessed using `configure terminal` 
## Parts: 
+ **FIRST PART:**[[1732043763 - Practica - Routers - 1|Practica - Routers - 1]] 
+ **SECOND PART:** [[1732043831 - Practica - Routers - 2|Practica - Routers - 2]]

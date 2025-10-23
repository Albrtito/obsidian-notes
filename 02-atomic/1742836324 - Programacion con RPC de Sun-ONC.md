---
id: 1742836324 - Programacion con RPC de Sun-ONC
aliases:
  - Programacion con RPC de Sun-ONC
tags:
  - Distri
---
# Programacion con RPC de Sun-ONC

Para saber si se ha registrado conrrectamente el servidor utilizar: 
```
rpcinfo -p ipAddress
```

**Remarks:** 

+ Usar flag -M para generar stubs multi-thread.
- Usar flag -a para generar todos los archivos necesarios(includio cliente y servidor)
- Usar también flag -N 
+ Solo hay que cambiar el archivo suma_server.c generado para el código del servidor y el archivo suma_client.c generado para el código del cliente. 

> [!attention] Cuidado con el clean del makefile
> Pq borra todo, todos los archivos creados por el RPC también. 
> Una vez que se crean los archivos con el RPC no volver a generarlo. (vas a perder todo lo que has hecho si lo haces) 


***

### Up
- [[1742832943 - Llamadas a procedimientos remotos|Llamadas a procedimientos remotos]]

### Down
- [[1742836514 - Definicion de interfaces con RPCs|Definicion de interfaces con RPCs]]

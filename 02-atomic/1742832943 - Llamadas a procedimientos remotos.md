---
aliases:
  - Llamadas a procedimientos remotos
  - Remote Procedure Calls
  - RPC
tags:
  - Distri
References: 
cssclasses:
---
# Llamadas a procedimientos remotos

> CASO ESPECÍFICO: Programacion con RPC de Sun/ONC


> [!NOTE] Objetivo: 
> Poder programar lo distribuido como si no lo fuese.
> + Hacer la comunicación como si fuese un proceso local. Una vez que se llama a esa función local se realizará toda la logica de conexión distribuida internamente. 


> [!CHECK] Idea: 
>  Obtener el código del servidor automáticamente b asado en las interfaces del cliente. 
>  A esto se dedican los RPCs, simplifican todo lo que se haría con sockets para hacerlo internamente. 

## Uso de la RPC
Las RPC generan el código (stub) del cliente y servidor a partir de un archivo `.x`
+ Del lado del servidor se han de implementar las funciones definidas. 
+ Del lado del cliente se haran **llamadas al stub del cliente** que a su vez se encargará de hacer toda la comunicación con el servidor. 

**Remarks:**
+ El cliente es el activo, es el que activa la comunicación con el servidor 
+ El server es un proceso pasivo esperando requests. 
### Stubs:
Piezas de código que realizan la comunicación entre servidor y cliente. 
>Lo que durante los laboratorios de la asignatura han sido proxy.c y servidor.c 

+ Se encargan de hacer toda la convesrsión de parámetros para el uso de sockets. 
+ **Stub servidor:** Se encarga de registrar el servicio para que el cliente pueda buscarlo

## Características de RPC: 
1. Existen dos tipos de RPC: 
	+ **Síncronas** Petición y respuesta
	+ **Asíncronas:** Solo admiten peticiones. El cliente no espera una respuesta (no hay salida)
2. Utilizan un lenguade de definición de interfaces (IDL)
3. Generan los stubs
4. Funcionan basados en un protcolo de comunicación

## IDL:
> Lenguaje de Definicion de Interfaces

Requiere tres tipos de parámetros: 
1. de **entrada (in)**
2. de **salida (out)**
3. de **entrada/salida (inout)**

Para transferir estos parámetros hace falta **aplanar los datos**, esto significa pasarlos a texto, normalmente dentro de un esquema de representación de datos (XML, JSON, XDR, CDR)

Para enviarse estos datos hace falta un protocolo que establezca: 
+ Formato de mensajes 
+ Formato de representación 

Tiene en cuenta la conversión de datos que puede ser: 
+ Simétrica
+ Asimétrica

Tiene en cuenta el tipado: 
+ Explicito 
+ Implicito 

Crea un servidio de enlace. Permite establecer la conexión, esto implica. 
+ Encontrar al servidor por parte del cliente
+ El servidor tiene que registrarse en algún lado con su IP y puerto abierto relacionados con un nombre. Esto lo guarda en el binder, una tabla de traducciones de nombres de servicio a dirección/puerto. 
Este servicio de enlace lo implementa el enlazador dinámico, junto a las interfaces que el servicio define. 
![[1742832943 - Llamadas a procedimientos remotosj.png]]

Se define el tipo de enlace que se genera entre cliente y servidor, que puede ser: 
+ No persistente 
	+ Tolera fallos
+ Persistente
	+ Tolera menos fallos
+ Híbrido 

## Fallos: 

> [!bug] Cliente no encuentra servidor 
> + El servidor puede estar caido 
> + Versión antigua del server en uso 
> El servidor le devuelve un -1 (ERROR) como error al cliente en estos casos.


> [!bug] Perdida del mensaje del cliente 
> + Se usa un timer, si se pasa se repite el mensaje 


> [!bug] Pérdida de respuesta:
> + Con operaciones que se pueden repetir las veces que sea (idempotentes) no pasa nada
> + Para las que no son idempotentes se ha de comprobar de alguna forma si esa respuesta se mando


> [!bug] Fallos en server 
> … 



> [!bug] Fallos en cliente: 
> + Si no se recibe respuesta reenviar (incluir identifiación de petición)
> + Usar la identifiación de petición para reenviar respuestas no idempotentes. 


***
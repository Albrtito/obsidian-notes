---
aliases:
  - Servicios distribuidos
tags:
  - Distri
References: 
cssclasses:
---
# Servicios distribuidos

> [!BUG] Problemas en la sincronización de los servicios distri: 
> + Uno de los grandes problemas con los que nos encontramos en los sistemas distribuidos es la **ausencia de un reloj común** para sincronizar los procesos. 
>+ La información relevante esta distribuida “puedo no tenerla yo”
> 

Dados dos procesos en un servicio distribuido se puede decir que: 
+ Son concurrentes o que un ocurre antes que otro. 
Esto se ve a través de los diagramas de espacio-tiempo:
![[1741624225 - Servicios distribuidosj.png]]

Un modelo distribuido puede ser **asíncrono o síncrono:**
+ **Asíncronos:** Aquellos en los que **no hay reloj común.**
	+ No suponemoss nada sobre la velocidad de un proceso
	+ Canales fiables sin límietes: Hay latencia sin límite
	+ Comunicación entre procesos es la única forma de sincronización. 

Los problemas que tenemos en estos casos son de reloj y lo solucionamos aplicando otras técnicas para crear relojes. 

## Tiempo en el sistema linux:
Par obtener el tiempo actual en unsistema linux podemos utilizar. 
+`clock_realtime` : Obtiene le código actualizándolo 
+`clock_monotonic` : Obtiene el código sin actualizar (el código de la máquina.)

## Sincronización de relojes físicos: 
Para un sistema distribuido **cad nodo posee un reloj físico NO SINCRONIZADO.** este reloj puede obtener la hora a través del satélite pues casi todo lo tecnológico posee un GPS. 
Utilizándo este me´todo podemos tener dos tipos de sincronización: 
+ **Externa:**  Equipos sincronizados con la misma fuente externa
+ **Interna:** Equipos sincronizados entre ellos poniendose de acuerdo en un mismo timestamp. 

Para plicar tenemos varios métodos: 
### En un sistema síncrono: 
En un sistema síncrono, siempre y cuando conozca el tiempo de transmisión se puede mandar un mensaje de P1 a P2 con el timestamp y añadirle el tiempo de transmisión. 
Como obtener este tiempo de transmisión es algo complicado se utiliza una meida entre el máximo y mínimo tiempo posible para esa transmisión. 
El problema es que en. un sistema asíncrono el tiempo de transmisión entre nodos no esta acotado, no hay un máximo ni mínimo. 

### Algoritmo de Cristian:
Se utiliza un servidor externo de tiempo al que se le pide el tiempo.
![[1741624225 - Servicios distribuidosj-1.png]]
Se cuenta la petición y la respuesta y se tiene en cuenta sumándolo al tiempo obtenido del servidor. 

### Algoritmo de Berkeley:
El servidor realizza un muestreo periódico de todas las máquinas para pedirles el tiempo. Luego calcula **un tiempo promedio** y le indica el cambio necesario a cada máquina. 
+ **APLICA UNA SINCRONIZACIÓN INTERNA**


## Sincronización de relojes lógicos: 

> [!NOTE] Def: 
> SE definen a través de la relación de causa-efecto entre dos procesos. Esto se usa con un send(m) y un recieve(m). Sabemos siempre que si un proceso lanza un send(m) y otro lo recibe entonces el send fue antes que el recibe. 
> 

Esto se define con el **algoritmo de Lamport:**
![[1741624225 - Servicios distribuidosj-2.png]]

No obstante esstos relojes solo te dan una ordenación parcialmente pues el número RL(a) no identifica el proceso del que procede. Aquí es donde entran los relojes vectoriales. 

### Relojes vectoriales:

> [!attention] EXAMEN:
> ESTO SIEMPRE CAE EN EXAMEN 

> [!NOTE] Rel Vec. 
> Desarrollado independientemente for Fidge, Mattern y Shmuck.
>  

***
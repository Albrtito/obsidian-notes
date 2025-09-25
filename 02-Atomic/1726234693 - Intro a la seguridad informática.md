---
aliases:
  - Intro a la seguridad informática
tags:
  - cripto
References: https://aulaglobal.uc3m.es/pluginfile.php/7291371/mod_resource/content/1/M1_Intro_Ciber_Cifrado_2425.pdf
cssclasses: 
sr-due: 2024-12-20
sr-interval: 48
sr-ease: 210
---
# Intro a la seguridad informática.

## Objetivos de seguridad:
Los objetivos de seguridad se dividen en lo que llamamos la **triada CIA**: (CIA Triad)
![[Screenshot 2024-09-16 at 3.12.04 PM.png]]
+ **Confidencialidad**: Conseguir que los datos se mantengan **secretos y privados**. Aquí es donde cogen importancia los algoritmos criptográficos de cifrado como [[1726493246 - Algorithm - AES|AES]] o [[1726510994 - ChaCha20|ChaCha20]].
+ **Integridad:** Los datos han de estar **libres de  alteraciones**, Se debe de poder comprobar si una alteración a ocurrido. Se utilizan [[1728307154 - Funciones hash|Funciones hash]] para cumplir este objetivo.
+ **Aviabilidad:** Recursos tienen que estar siembre al alcance del usuario que los necesite. Hacer que algo deje de funcionar sería una rotura de este sistema.(Ataque DDOS)
+ **Autenticación:** Poder comprobar que una entidad **es quien dice ser**. Para estso se usan Certificados y [[1731681118 - Firma digital|Firma digital]]
+ **No repudio:** Las actuaciones de una entidad han de poder ser trazadas, **poder “echar la culpa” de cada acto a la entidad correspondiente.** Para esto se utiliza la [[1731681118 - Firma digital|Firma digital]]

**Remarks:**
 + Estos objetivos se han de cumplir en cualquier proyecto
+ El objetivo se satisface a través de servicios, algunos ejemplos ya se han dado en las definiciones. A su vez, el servicio cumple con la implementación de un mecanismo.
## Amenazas y medidas: 
### Tipos de amenazas:
Clasificamos las amenazas en 4 tipos: 
1. **Interceptación:** Escuchar lo que se esta diciendo a través de un medio de comunicación
2. **Interrupción**: Hacer imposible el uso de un servicio
3. **Modificación:** 
4. **Generación:**
### Tipos de medidas:
Podemos clasificar las medidas de seguridad que se aplican para proteger un sistema según diferentes criterios. 

**Según activación:**
Según cuando se utilizan las medidas de protección, las dividimos en tres grupos: 
+ **Prevención**: Aquellas medidas para **prevenir posibles ataques futuros**
+ **Detección**: Medidas para detectar el ataque **cuando esta ocurriendo**
+ **Respuesta**: Medidas de actuación en caso de ataque.

**Según el tipo:**
+ Medidas **físicas**: Hay que **proteger el hardware** ademas del software. 
+ **Técnicas**/Software: **Cifrados**
+ **Administrativas**: 
+ **Legales**: **Medidas aplicadas en la ley**. En España tenemos la LOPD (Ley Orgánica de Protección de Datos)

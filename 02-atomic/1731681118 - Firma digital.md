---
aliases:
  - Firma digital
tags:
  - incomplete
  - cripto
References: 
cssclasses:
---
# Firma digital
+ La firma digital utiliza [[1728912947 - Cifrado asimetrico|Cifrado asimetrico]], se cifrará con la clave privada del receptor pero se **firmará con la clave privada del emisor**. 

## Esquema/Algoritmo:
1. Se generan las claves públicas y privadas
2. Se firma el documento/mensaje con la clave privada 
3. Se verifica la firma utilizando la clave pública de la persona que ha emitido la firma. 

Existen dos tipos de esquema de firma: 
+ **Determinista**: Si firmas el mismo mensaje siempre obtendrás el mismo resultado de firma. Obtendremos este tipo de esquema al usar RSA
+ **Aleatoria:** Si firmas el mismo mensaje obtendrás distintas firmas dependiendo d eun índice. Obtendremos este tipo de esquema pal usar GAMAL. 

Por otro lado podemos encapsular la firma y mensaje todo junto en el mismo bloque o separar ambas partes. 
+ El RSA encapsula todo en el mismo sitio 
+ El GAMAL crea una firma por separado 

Algoritmo generalizado: 
+ Se firma el resumen en vez del mensaje debido a optimimzación y para que no haya acceso al mensaje
+ Se comparan los hashes del mensaje y la firma. 
	+ El mensaje ha llegado bien (integridad)
	+ El mensaje ha tenido que ser enviado por emisor (Autenticación y no repudio)

### RSA: 
+ [[1731682077 - Algorithm - RSA|Algorithm - RSA]]

### EL GAMAL: 


***
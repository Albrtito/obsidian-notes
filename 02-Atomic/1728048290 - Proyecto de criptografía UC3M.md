---
aliases:
  - Proyecto de criptografía UC3M
  - CriptCript
tags:
  - cripto
References: 
cssclasses:
---
# Proyecto de criptografía UC3M

> [!NOTE] Enunciado:
> 

## Requisitos:
> [!attention] **REQUISITOS OBLIGATORIOS:**
> 1. Registro y autenticación de usuarios
> 2. Cifrado/descifrado simétrico y/o asimétrico (o con cifrado autenticado)
> 3. Generación/verificación de etiquetas de autenticación de mensajes (hash y HMAC) (o con cifrado autenticado)
> 4. Generación/verifiación de firma DIGITAL
> 5. Autenticación de las claves públicas mediante certificados (PKI)


> [!attention]  **REQUISITOS → En clase:**
> 
> 1. Se ha de tener contraseñas guardadas con gestiones hash. **Como mínimo** han de ser contraseñas que **el usuario conoce**
> 2. El intercambio de información ha de estar cifrado.
> 3. Debemos de comprobar que el mensaje ha llegado integro. → `fernet`


### 1. Registro y atuenticación de usuarios:
Como **mínimo:** Contraseña
**Extra:** Datos biométricos o tokens

### 2. Cifrado y descrifrado: 
+ Se ha de mostrar el reultado en un log o en un mensaje de depuración, junto el tipo de algoritmo y clave utilizada 
+ Claves han de tener una longitud adecuada

### 3. Generación/verificación de etiquetas de autenticación de mensajes
+ Info debe de estar cifrada y autenticada
+ MOstrar resultado en un log o en un mensaje de depuración. Tipo de algoritmo y clave utilizada

## Generación y almacenamiento de claves:

**Para cifrado simétrico:**
+ Clave cifrada por una contraseña del usuario en la base de datos
+ Se puede no almacenar la clave si: 
  + El usuario la memoriza
  + Se genera a partir de la contraseña del usuario

**Cifrado MAC:**
+ Se utiliza una única clave → Se sigue lo dicho en el cifrado simétrico

**Cifrados Asimétricos:**
+ Se guarda la clave pública y privada. Solo se puede acceder a la privada con una contraseña.  

## Implementación:
**Librerías:**
+ [pyca/Cryptography](https://cryptography.io/en/latest/)
+ [PyCrypto](https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/)

### Funciones: 

+ `fernet`: Con esta función no solo se cifra el mensaje sino que también se autentifica. 
  **Remark:** Si la usamos, explicar pq lo hacemos.

+ `HMAC`: 

### Contraseñas:
Tenemos distintos **tipos de contraseñas:**

1. A través de algo que el usuario conoce (contraseña)
2. A través de algo que el usuario tiene (tokens)
   + A día de hoy esto se da con otro dispositivo conocido
3. A través de cosas biométricas
4. Alguna mezcla de las anteriores

### Gestión de contraseñas: 

+ Para **almacenar contraseñas se utilizarán funciones hash**. Estas son funciones irreversibles. Solo obtenemos el mismo resultado con la contraseña. 
	> Utilizar función hash sha256
+ **Caducidad de contraseñas:** Cada cierto tiempo se pueden volver a pedir las contraseñas. 



***

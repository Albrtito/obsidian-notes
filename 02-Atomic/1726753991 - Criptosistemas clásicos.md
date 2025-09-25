---
aliases:
  - Criptosistemas clásicos
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2024-12-02
sr-interval: 30
sr-ease: 204
---
# Criptosistemas clásicos

**Referencias:**[Recurso web: Cifrar mensajes con cifradores clásicos](https://www.cryptool.org/en/cto/)
Los criptosistemas clásicos utilizan métodos clasicos de cifrado basados en la transposición y la sustitución como únicas operaciones matemáticas.[^1].
## Métodos de sustitución:
Necesitamos conocer el concepto de sustitución monoalfabética, polialfabética, monográfica y poligráfica

> [!NOTE] Definición:
> **Poligráfica/Monográfica:** Debido a que sustituye los grafos individualmente(Mono) o en grupos(Poli).

> [!NOTE] Definición:
> **Monoalfabética/Polialfabética:** Respecto al n**úmero de alfabetos criptados** que se crean. 
> + Mono → Uno
> + Poli→ Más de uno
### Monoalfabéticas:
+ Poligráfica
	>p.e: Cifradores de PLAYFAIR y HILL. Uso de matrices y equaciones lineales.
+ [[1726494310 - Sustitución monoalfabeto monográfica|Monográfica]]
### Polialfabéticas:
+ [[1726496164 - Sustitución polialfabética periódica|Periódica]]
+ [[1726497421 - Sustitución polialfabética no-periódica|No-Periódica]]
## Métodos de transposición:
+ **Por grupos**: 
	Se cambián grupos de caracteres entre ellos según una clave. 
	> p.e: La **escítala** es un mecanismo antiguo en el que, al enrolllar el pensaje en un bastón con **determinado diámetro**, el mensaje era descifrado. 
+ **Por series**:
	Se definen series numéricas. Cada serie con unos números en específico. Esos números representarn caracteres del mensaje. Se reordenan los caracteres según el orden de las series.
+ **Por columnas**
	Se disponen los símbolos siguiendo un cierto patrón geométrico. Se extraen siguiento una cierta trayectoria.

***
[^1]: [[1726520589 - Definition - Criptosistema#Técnicas matemáticas de cifrado]]

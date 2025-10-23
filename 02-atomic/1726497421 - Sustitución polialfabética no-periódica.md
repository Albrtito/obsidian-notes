---
aliases:
  - Sustitución polialfabética no-periódica
  - Método de Vernam
tags:
  - cripto
References: 
cssclasses: 
sr-due: 2025-01-21
sr-interval: 77
sr-ease: 269
---
# Sustitución polialfabética no-periódica

> [!NOTE] Definición: 
> Los alfabetos creados son aleatorios. Esto se consigue a través del método de Vernam. 

## Vernam: 
**Uso de una puerta XOR para comparar la clave con el mensaje y generar el cifrado.** 

+ Este cifrador es **incondicionalmente seguro** si: La clave es realmente aleatoria, se usa una sola vez y es de longitud igual o mayor que M.

> [!BUG] Problema: 
> Este meétodo es **imposible de implementar**, pues para ser completamente seguro necesitamos generar **números realmente aleatorios para usar como claves**, algo imposible
+ Para “solucionar” este problema usamos números pseudoaleatorios en los cifrados.


![[Screenshot 2024-09-16 at 7.13.37 PM.png]]

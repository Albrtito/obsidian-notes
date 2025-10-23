---
id: 1742836514 - Definicion de interfaces con RPCs
aliases:
  - Definicion de interfaces con RPCs
tags:
  - Distri
---
# Definicion de interfaces con RPCs

## Métodos del programa:

```c
program programName {
	version programVersion{
		int serviceName(params) = opNum;
		int serviceName(params) = opNum;
        struct <structName> serviceName(params) = opNum;
		...
		} = versionNum;
	} = programNum;
```

> **PRÁCTICA:** Usar el NIA como número de programa para que, si usando guernika, no haya conflictos 

## Esctructuras de datos:

Los archivos `.x` permiten el uso de esctucturas y distintos tipos de datos.

```c

struct <structName>{
    int <name>;
    string <name><<len>>;
    double <name>[<len>];
    float <name>;
    ...
};

```

**Remarks:** 

- La asignación a una variable de una longitud entre < > significa que acept arrays variables de hasta el número que sea de bytes. Si es [ ]  son arryays fijos.  

***

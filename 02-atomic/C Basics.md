Date: 2024-02-09
Class: #os 
References: 

---
+ **Including libraries and other .c code:** 
```C
#include <libraryName.h>
``` 
+ **Comments:** With `/*` for opening and `*/` for closing
+ Always **need a main function**
```c
int main(int argc, char **argv) 
{ 
printf(“Hello World\n”); 
return 0;
}
```
+ **EVERYTHING ENDS WITH A `;`**
### Printing: 
+ Always end with new line `\n` 
+ **Command:** `printf(string)`
### Functions: 

```c
int myFunction(int argument1, char **argv){

return int;
}

```
+ **Define everything** 
+ Takes some arguments defined as what they are
+ Has a type, based on what the function returns
+ Needs to return unless it's a `void` function, these functions are the ones that do not return

## Memory: 

Each type of variables will span a quantity of memory. This can be specified with brackets in the following way. 
**Variable Types:** `char, int, float, int64_t` 
+ char: single character (takes 1 byte)
+ int: a signed integer saved in 4 bytes
+ float: a 4 byte floating point
+ int64_t: Signed 8byte integer
`variableType [x]` : The variable type takes x bytes. 

When a variable is created the compiler puts it somewhere in memory, doesn't really matter where. 

#### Declaring variables: 

```c
char x; 
char y = 'e';
int z; 
int z = 34;
```


[Pointers](Pointers.md)

---
### Summary
Highlight ==what’s important!==

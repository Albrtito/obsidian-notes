---
aliases:
  - Intro to processes
tags:
  - os
"References:": 
cssclasses:
  - center-images
---
# Intro to processes: 
## Definition of a process

**Definition of a process:** A process is a **program in execution** ^ProcessDefinition

Whenever we execute a program a new process is created. This processes are the **units of management of the operating system**

For any program several processes can be created at the same time. The easiest example to understand this is with an example, maybe not an accurate one but a clear one. 
f.e:
	If we open a browser we’ll obtain a single window where we can open different tabs. This window is a process from the browser program. If we know open a new window of the browser we have created a new process of the browser program. 

Any process consist of: 
+ A set of instructions: Program text
+ A set of data: Variables, libraries, memory space. 

## Memory representation: 
Those instructions and data must be saved into memory. Each process occupies some memory space, that memory space is divided in the following way:

+ **Text**: Set of instructions. The programming of the process
+ **data:** Fixed data. (global variables, fixed memory space for data)
+ **heap:** Growing memory for variable data
+ **stack**: Also growing Memory

A deeper dive into memory management of the processes will be done → Then add this block into the new note and just reference it here. 

## Lifecycle of a process: 
Then what is it that we are doing when creating a process? We are telling the CPU to start working on it. 
When a process is created it’ll start running in the CPU. However the CPU cannot do everything, we’ll call this “things” that the CPU cannot do events. When the process requests an event the CPU blocks it so it can keep working on another process while it’s waiting for the event to finish. 

The following image describes how a process is run. 

![400](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2013.42.45.png)
+ Time-slice finished: This means that the CPU stops working on the process, but the process is not blocked as there is no event it needs waiting to.

With a one-processor CPU we’ll get: 

![400](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2013.46.57.png)
+ The processor takes a queue of processes and starts processing them in order, new processes are added to the list, terminated processes just exit the CPU directly
+ If a process needs to wait for an event, the CPU stops working on it and sends the process to the queue of processes waiting for that event. Once the event finishes, that process will go back to the queue of the CPU (in the last place)

For a multicore CPU we get the following model: 
![400](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2013.50.55.png)

**Remark:** See that for both models, the end of time-slice means taking the process back to the queue of the CPU

### Process creation: 

The OS provides a mechanism to allow a process to create other processes, the **System call** 
When a parent process creates a child process, it must share it’s resources with it’s children (this is so no process can infinitely duplicate until there is no resources left)left. 

When a process is created…
+ In terms of **execution** the parent waits until some or all of it’s children have terminated.
+ In terms of **memory space**, the child process is a clone of the parent process. The child process has already another program loaded in memory (what?)
#### Unix process creation:
In order to look at the process hierarchy of an UNIX system the command: `pstree` can be used. 
##### The fork model:
The unix family makes a distinction between process creation and new program execution. 

When creating a new process the system call is fork(). 
The child process may then invoke the **exec*()** system call in order to change its memory image with a different program. 

However there are some **inefficiencies** to the fork model: 
+ To much data is copied
+ If a new memory image is loaded, all copies are discarded.

Therefore many UNIX systems use COW.
##### The COW model (Copy On Write)
Copy on write is a technique to delay or avoid copying the data when performing a fork. With this model the fork **only copies the page table from parent, not the pages. Just creates a new PCB for the child.**

Structure created with the COW model:Two page tables redirecting to the same pages. 
![Screenshot 2024-04-11 at 16.35.29](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2016.35.29.png)



### Process termination:

When a process finishes all its allocated resources are freed up. 
+ This is notified to parent processes

A process may may terminate in one of 2 ways: Involuntary and voluntary.(kind of like with context switching)
+ **Involuntary**: Exceptions, aborted
+ **Voluntary:** exit() system call

After the termination there are two possible outcomes: 
1. The children are not affected
2. All children also terminate → **Cascade termination**
#### Unix process termination:
+ When the parent is terminated, all process depend from the **init** process. 
+ When a child is terminated, the process changes to **zombie** state until the parent process gets its termination code.
### PCB elimination: 
First of all it’s important to differ between the termination of a process and the elimination of the PCB. 
**Remember:** A PCB is the process control block. 
+ Theory said: When a parent get’s info from child, data structures can be removed (what this means? no idea.)


### Spawning to disk (swap) expanded lifecycle
When there are many processes in execution, performance may degrade du e to excessive paging (this phenomenon is called trashing). The solution for this is to create a suspended state where the OS sends a process to swap. 

**Swap:** Swap is a concrete area in the disk used to store the pages of processes that no longer have space in main memory.

The creation of swap creates **two new process states**
+ Blocked and suspended 
+ Ready and suspended
And results on the following diagram:

![Screenshot 2024-04-11 at 16.55.26](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2016.55.26.png)

## Scheduling:
Scheduling is how the OS decides which process is going to run next. During the process lifecycle we’ve only seen processes as in a queue. However 

## Process information: 
All processes need some information to run, this information is divided into three categories based on where it is stored: 
1. Information stored in the processor
2. Information stored in Memory
3. Additional information managed by operating system
## Processor state: 
The processor has two main states, user and privileged(kernel) mode. 
+ User mode makes all general registers, program counter, stack pointer and the user part of the status register aviable
+ Privileged mode: Use of the privileged part of the status register and the memory management registers.

**Context switch??** → What is that?

## Memory image of a process: 
Of course, a process cannot access every part of the computer, it would not be secure if the data of the process could be store anywhere. 
The memory image consists of **memory spaces that the process is authorised to use**

+ A **[trap](20240411%20-%20135931%20-%20System%20trap)** is generated if the process tries to access any address outside it’s memory image
+ The process memory storage could be virtual or physical memory

	+ If there is no virtual memory: Fixed size region is the best way to go. Using variable memory turns into a memory waste

	+ If there is virtual memory: We could use virtual reserve space. But it’s better to just have multiple regions (the definition of virtual memory) and this is not used

	+ **The best thing is to use virtual memory with multiple regions**
### Multiple regions: 

Using multiple regions and virtual memory, the gap between the data and stack can grow without a misusage of resources. 

![100](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2014.06.36.png)

But what if there are several growing data regions. In the previous example there where only two (easy). In current versions of OS systems processes have several growing data regions, these regions may differ in permissions or might be shared between processes. 

An example of the memory image of a process, with several variable data regions
	![400](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2014.10.38.png)

## OS process information: 
The OS has to manage the processes, what is done on it’s part to do so? What info is kept by the OS on processes?

### The process table:
The OS keeps information in a table called **process table**. Each entry in the table is called **process control block (PCB)** and keeps information about one process.

Which information? A lot, almost all there is.
+ Identification of the process 
+ Processor rate
+ Process control information 
+ I/O status info 
+ Memory management info
+ **Pointer to the page table (see below)**
+ ...

The information that is not in the PCB is due to efficiency and information sharing.
+ The PCB needs to be stored in memory : Fast but little info
+ If some info needs to be shared is not in the PCB → We use pointers to point to other PCBs
### Page table:
Outside of the PCB is stored the **page table**, for each process there is a Page. 
This table describes the process memory image. It is stored outside because it has a variable size and the memory sharing requires it to be external to PCB. 
### File position pointers
Outside of the PCB.

## Services:
What services does the OS have to deal with proceses?

+ We’ll be using the c language to interact with the OS (This during the OS UC3M course, although it is the main one used when working in OS)
### Fork:
This service duplicates **the process invoking the call**. After the duplication, parent process and child process go on running the same program. 
+ Child process inherits open files from parent process 
+ Pending alarms are deactivated

**Returns:**
+ -1 on error 
+ In parent process: Child process descriptor (pid in example below)
+ In child process: 0


**Call (c code):**
```c
#include <sys/types.h>
#inlclude <stdio.h>

// Call of the fork service
pid_t fork(void);

//usually called in the following way:
 
pid_t pid; //Declaration of a variable of type pid_t
pid = fork(); //call the fork function

```

### Exec:
Execute some program from the process that the service is being called. 
+ Same process runs another program
+ Open files remain open


This single service contains multiple library functions: 

+ **int exec1**(const char *path, const char *arg, …);
+ **int execv**(…)
+ **int execve**(…)
+ **int execvp**(const char *file, char *const argv[]);

Where: 

**path:** path to executable file 
**file:** Looks for the executable file in all subdirectories specified by path

**Returns:**
+ -1 on error 
+ If no error, no return


### Exit: 
Finalices a process execution.
**Call (c code)**
```c
void exit(status);
```

+ Status takes 0 if the process is exiting with no errors, if there has been an error and thats why the program it’s exiting, then it takes -1.

### Wait:
Takes a process from the ready queue until the child has terminated.
**Call:**

```c
wait()
```

**Return:**
+ If called from a parent process: Blocks process until child terminates and then **returns the PID of the terminated child**
### Usage of fork, exec, wait and exit:

![Screenshot 2024-04-11 at 15.48.21](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2015.48.21.png)

## Multitasking
Multitasking is when the processor is working on several processes at the same time. All these **processes are running at the same time**.

+ A multitasking system is called **multiprocess** while a system without multitasking would be **mono-process**
+ A multiprocess system has the ability to have several users running at the same time (while a monoprocess system can’t)
### Principles of multitasking: 
1. There’ll be a real parallelism between I/O and CPU
2. Process can alternate between the I/O and CPU
3. Several processes stored in memory at the same time. 
### Advantages of multitasking: 
+ Modularity (divide the program in multiple processes)
+ Allows multiple users
+ Takes advantages of the time spend on I/O
+ More time using the CPU
### Multiprogramming and Virtual memory:
At any time the OS divides the addressing space of a process into pages and stores a number of them in main memory. All the physical memory space is divided in page frames

## Context switching: 
Context switching is done when an OS assigns a processor to a new process. This means that the processor stops working on the process and starts working on a new process. 

This change between processes can be done in several ways. 
### Voluntary context switch:
A voluntary context switch is done when a process, for any reason, decides to go into blocked state. 
+ The process performs a call to the OS, starts waiting for an event.
+ The process that was running goes into blocked mode

### Involuntary context switch: 
This happens when the OS appropriates the CPU and kicks out any processes there could be running there. 
+ The process that has been kicked out goes into ready mode 


## Generating an executable ( using c as example): 
In order to generate an executable we need the following: 
+ **Compiler**: Compiles the c code into binary
	(input: c code “.c”, output: binary “.o”)
+ **Linker**: Link the binary code with the libraries, if there are several binary files (from several different c codes) it links them together. 
	  (input: binary files “.o”, output: executable file (no extension))

Example with two .c files a and b. 
![Screenshot 2024-04-11 at 16.09.33](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2016.09.33.png)

**Static libraries:** Are those pieces of code that are needed for the execution of the binaries.  (the .h)

If an static library needs to be added it’s done during the linking. 
![Screenshot 2024-04-11 at 16.11.41](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2016.11.41.png)

# Dynamic and static libraries: 
**Static libraries:** Are those pieces of code that are needed for the execution of the binaries.  (the .h)

The drawback of static libraries is that code could potentially be duplicated, we are loading and storing code that won’t be updated. The solution is to create **dynamic libraries (*.so)**

Dynamic libraries are loaded in memory and executed **at runtime**, the functions from those libraries may be shared by multiple processes

Example of how a dynamic library would be loaded.
![Screenshot 2024-04-11 at 16.15.38](../99%20-%20Meta/0.%20Attachments/Screenshot%202024-04-11%20at%2016.15.38.png)
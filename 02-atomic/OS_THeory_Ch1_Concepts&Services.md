# What is an OS?
+ Manager deciding which instruction is going to run at each time 
	+ Manage resources
+ Restriction of permissions and resources for use of the hardware
+ Running more than one program at the same time 
+ Most of the OS is interrupt driven. This means that most of the processes are actually handled by the interruption manager
+ **Remember:**[Computer Structure](Computer%20Structure) : 
	+ A ECall is a type of interruption
	+ Storage-Hierarchy: Where to look in case of a miss?
+ Manages data flow between the other storage units and the main memory
### Goals: 
1. Make life easy for the user. Be at the service of the user
2. Make the use easy
3. Use the hardware efficiently
4. Manage permissions between the users and the hardware
5. Provide not just what the hardware provides but more



### More than one Program, then more than one User
How to manage resources of the CU when there are several programs running. What if there are several users with several programs running for each of them. 
+ Multiprogramming: Organise the processes into jobs, the total jobs are kept in memory. When a job can be done in any part of the system it is retrieved and done. This way while the CU is working something can be written in memory (for example)
+ Timesharing: Give each job/user a fraction of the time, then go to the next one. Finally all of the jobs advance at the same speed although not at the top computer speed. 
### Dual-Mode
Separation between what the users can actually do and what the OS in a controlled environment will be able to do 
+ OS -> Kernel
In order to know the mode the mode bit is used

## Main services of the OS

### Process Management (CU Manager): 

+ There's an uni PC value for each of the programs running. This PC value is used while the program is running but the moment the program is stopped the PC value is saved and stored in memory
	+ The minimum required number of PC required for a process is 1. However in order to multithread, each thread must have it's unique PC value. 
	+ Suspend a program : Stop the program and save the PC value. 
	+ Resume a program : Look for it's PC value
	+ Process (counters) should be able to synchronise ¿?
	+ Careful with deadlock handling (when a program refers to another?¿)


### IO Manager
+ From the operating system point of view, every IO device is a file to which the OS writes and from which it reads data.

### Storage Management

## Protection and security
+ Identify users
+ Resources assigned to users (usually at this level of complexity everything is a file)
+ Assign permissions for each user for the resources of other users. 
+ This also relates with the kernel mode and it's capacity to protect the computer . 
## Structure of an OS: 
### Monolitic OS:
+ No clear or well defined structure
### Layered OS
+ Structured as a set of layers with clear and well defined interfaces
### Client-Server approach: 
+ 

# IO
+ When working with IO from the CU make them look like memory (from a microinstruction perspective)
+ Use control Register in the IO device to input commands 
+ Use the Status register to know when the command is done 
	+ Notified through an interrupt -> Created by the IO(signal goes outside the bus)
	+ During the fetch state, check out if any device has finished. If any device has finished run the **interruption handler**
+ Use the data registers to receive input and/or output
+ For high-speed IO it can transmit data directly into the memory
**Handling interrupts:**
1. States are saved in ra and sp
2. 3. Kernel Mode ^50bc9e
3. Type of interrupt 
4. Respective instructions to perform the interruption 

# OS startup: 
+ 
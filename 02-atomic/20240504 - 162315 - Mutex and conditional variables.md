---
aliases:
  - Mutex and conditional variables
tags:
  - os
"References:": 
cssclasses: 
sr-due: 2024-05-22
sr-interval: 10
sr-ease: 270
---
# Mutex and conditional variables:
## Mutex:
Mutes are synchronization mechanisms for threads.**Based on semaphores** we can say that: 
+ Mutex are binary semaphores

### Methods:
They perform atomic operations lock(m) and unlock(m) to block or unblock the mutex.
Then an implementation with critical sections would be:

```c
lock(m); /*entry into critical section */
<critical section>
unlock(s); /*exit from critical section */
```
**Remarks:**
+ Unlock operation must be performed by the thread that locked.
## Conditional variables:
They are synchronization variables associated to a mutex.
### Methods:
There are two atomic operations associated to conditional variables, wait and signal. 
+ Wait operation blocks the running thread and releases mutex.
+ Signal: Unblocks one or more threads suspended in the condition variable. Then the unlocked threads compete to acquire the resource 
**Remarks:**
+ It is convenient to run these two operations inside a **lock/unlock** block (from a mutex)
## Implementation:
**Thread A:**
The lock is the first thing to happen, if this thread gains control of the resource it’ll check wether the condition is met (while (resource is busy)). If the resource is not busy we can keep on, however if it is busy it’ll wait until the condition is met.
**Remark:**
+ It is really important to use the while
```c
lock(mutex); /*access to resource*/
<check data structures>
while (resource is busy){
	wait(condition,mutex);
}
<mark resource as busy>
unlock(mutex);

```

**Thread B:**

```c
lock(mutex); /*access to resource*/
<mark resource as free>
signal(condition,mutex);
unlock(mutex);

```

## POSIX services:
![POSIX-Mutex and Conditional var.](20240504%20-%20162928%20-POSIX%20-%20Mutex%20and%20Conditional%20var..md)

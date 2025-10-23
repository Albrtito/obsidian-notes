---
aliases:
  - POSIX - Semaphores
tags: 
"References:": 
cssclasses:
---
## Interfaces for the use of semaphores in POSIX.
In POSIX semaphores are implemented as a synchronization mechanism for processes or threads running in the same machine.There are two types of POSIX semaphores:

### Types:

+ **Named semaphores:**  These are semaphores that can be used by different processes just by knowing the name of the semaphores, it does not require shared memory to use them. 

```c
#inlcude <semaphore.h>
sem_t *semaphore; //named semaphore
```

Adding it as a pointer as it is pointing to the systems semaphore.

+ **Unnamed semaphores:** They can be only used by processes that created them (with threads) or using a shared memory region.
```c
#inlcude <semaphore.h>
sem_t semaphore; //unnamed semaphore semaphore
```

### Implementation of POSIX semaphores:
#### Methods:

**Initialisation of unnamed semaphore**
```c
init sem_init(sem_t *sem, int shared, int val);
```

**Destroy unnamed semaphore:**
```c
int sem_destroy(sem_t *sem)
```

**Open(create) a named semaphore:**
```c
sem_t *sem_open(char* name, int flag, mode_t mode, int val);
```

**Closes a named semaphore:*
```c
int sem_close(sem_t *sem);
```

**Delete a named semaphore:**
```c
int sem_unlink(char* name);
```

**Wait operation on a semaphore:**
```c
int sem_wait(sem_t *sem);
```

**Try wait operation on a semaphore:**
```c
int sem_trywait(sem_t *sem);
```

**Signal operation on a semaphore:**
```c
int sem_post(sem_t *sem);
```
#### Working with critical sections:

**Entering a critical section:**
```c
sem_wait("semaphore");
```
The code behind this would be similar to:

```c
sem_wait(s)
{
	s = s-1
		if(s<0)
		{
		<Block process>
		}
}

```
+ Add one to the semaphore
**Exiting a critical section**

```c
sem_post("semaphore");
```
The code behind this would be similar to: 

```c
sem_post(s)
{
	s = s+1;
	if (s<= 0)
	{
		<Unblock a process by wait operation>
	}
}

```
 + Post means unblocking one waiting process.



---
aliases:
  - POSIX-Mutex and Conditional var.
tags:
  - os
"References:": 
cssclasses: 
sr-due: 2024-05-26
sr-interval: 9
sr-ease: 250
---
# POSIX Interfaces for managing mutex and conditional variables:
## Mutex:

**Initialize mutex:**
```c
int pthread_mutex_init(pthread_mutex_t* mutex, pthread_mutexattr_t* attr);
```

**Destroy mutex:**
```c
int pthread_mutex_destroy(pthread_mutex_t* mutex);
```

**Try to get access to mutex:**
```c
int pthread_mutex_lock(pthread_mutex_t* mutex);
```
- Blocks thread if mutex is already acquired by other thread.

**Unblock mutex:**
```c
int pthread_mutex_unlock(pthread_mutex_t* mutex);
```

## Condition variables;

**Initialize a condition variable:**
```c
int pthread_cond_init(pthread_cond_t* cond, pthread_condattr_t* attr);
```

**Destroy a condition variable:**
```c
int pthread_cond_destroy(pthread_cond_t* cond);
```

**Unblock one or more threads:**
```c
int pthread_cond_signal(pthread_cond_t* cond);
```
- Unblocks one or more threads that are suspended in the condition variable `cond`.
- Has no effect if there is no thread waiting (difference with semaphores).

**Unblock all threads:**
```c
int pthread_cond_broadcast(pthread_cond_t* cond);
```
- All blocked threads in condition variable `cond` are unblocked.
- Has no effect if there is no thread waiting.

**Suspend thread until signal:**
```c
int pthread_cond_wait(pthread_cond_t* cond, pthread_mutex_t* mutex);
```
- Suspend thread until another thread signals condition variable `cond`.
- Automatically releases the mutex. When the thread is unblocked it contends again for the mutex.
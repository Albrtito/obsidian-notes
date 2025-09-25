---
Date: 2024-03-18
tags:
  - os
"References:": 
sr-due: 2024-05-23
sr-interval: 15
sr-ease: 150
cssclasses: 
aliases:
  - Problem -Producer-Consumer problem
---
# Producer-Consumer Problem: 
The producer-consumer problem is a possible solution for the race conditions involving  [[20240503 - 190310 -Semaphores Dijkstra method|Semaphores]] and [[20240504 - 162315 - Mutex and conditional variables|Mutex and conditional variables]]  **when the order of processes is importan**. Using semaphores is really tricky as it can easily not work. This is why sticking to algorithms such as this one is always a good idea.

This algorithm is based on a simple model: 

```mermaid
flowchart LR

Producer --> Buffer
Buffer --> Consumer

```

This is the basic model for **data transmission** (which is frankly most of the tings that will happen with process concurrency). A process (producer) produces some data and inputs it into the buffer. Another process (consumer) will take that data from the buffer and do somethings with it. We then have the following problem that needs to be fixed: **The consumer can only consume when something has been produced**, this is the key thing about this algorithm. If we didn't have any order issues we could just apply the semaphores without anything else. The order makes it necessary to use this algorithm (or any other).

Once we have identified this key issue we can identify other things about the model: 
+ The buffer can be of infinite size or with a fixed size
	+ In order to identify the starting and ending point of the buffer two pointers are used
	+ If the buffer is infinite then no problem
	+ If the buffer is finite, then it is used as a circular buffer (when getting to the end of the buffer go to the beginning.)
## Solutions: 
### Sol. and implementation with semaphores: 
We'll use semaphores not only to protect the critical sections of the code but also to signal when a producer has entered a value to the buffer (so that the consumer can start consuming)
If the producer doesn't produce then no signal is send to the consumer and the consumer will be kept asleep
**Remark:** When we talk about a process being asleep it means that it is being kept in standby until a signal is send. (this is what the semaphores do) 

There can be several implementations, for the OS course we have seen one with two semaphores, it goes in the following way: 
+ Creating new semaphores (with value 0) not to control critical sections but to control another thing. 
	+ Every time the producer produces anything the new semaphore adds one. Then this semaphore is tracking the elements there are in the buffer
	+ Then if the consumer wants to read some data in the buffer it'll subtract one for this new counter.
	+ If there is no data to read or other consumers are using the value, then the consumer wont be able to consume data. 
	+ The consumer waits for the producer to produce
---
## Code:  

```C
/*This program is used to create a producer-consumer system.
Both share a buffer that is initially started empty.
The producer puts elements in the buffer, and the consumer removes them. If the buffer becomes full, the producer must stop producing. If the buffer becomes empty, the consumer must stop consuming.
* Compile with  gcc -lpthread main.c
* 
*/
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define MAX_BUFFER 256
#define DATA_TO_PRODUCE 1024

sem_t holes; // semaphore “holes” keeps track of number unoccupied slots in the buffer at any given time 
sem_t elements; // semaphore “elements” keeps track of number occupied slots. 
sem_t mutex; // semaphore to protect shared buffer

int buffer[MAX_BUFFER]; // buffer to store produced and consumed elements

void producer(void);
void consumer(void);

int main(void) {
    pthread_t th1, th2;

    // initialize semaphores
    sem_init( & holes, 0, MAX_BUFFER);
    sem_init( & elements, 0, 0 );
    sem_init( & mutex, 0, 1);
  
    // create producer and consumer threads
    pthread_create( & th1, NULL, (void * ) producer, NULL);
    pthread_create( & th2, NULL, (void * ) consumer, NULL);

    // wait for threads to finish
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    // destroy semaphores
    sem_destroy( & holes);
    sem_destroy( & elements);
    sem_destroy( & mutex);

    exit(0);
}

void producer(void) {
    int pos = 0; // position in buffer to produce next element
    int dato; // data to produce

    for (int i = 0; i < DATA_TO_PRODUCE; i++) {
        dato = i; // produce data
        sem_wait( &holes); // wait for empty slot in buffer
      
        // critical section
        sem_wait( &mutex); 
        buffer[pos] = i; // put data in buffer
        sem_post( &mutex); 
      
        printf("produce %d \n", buffer[pos]); // print produced data
        pos = (pos + 1) % MAX_BUFFER; // update buffer position
        sem_post( &elements); // signal presence of element in buffer
    }
    pthread_exit(0);
}

void consumer(void) {
    int pos = 0; // position in buffer to consume next element
    int data; // data to consume

    for (int i = 0; i < DATA_TO_PRODUCE; i++) {
        sem_wait( &elements); // wait for element in buffer
      
        // critical section
        sem_wait( &mutex); 
        data = buffer[pos]; // get data from buffer
        sem_post( &mutex);
      
        pos = (pos + 1) % MAX_BUFFER; // update buffer position
        printf("Consume %d \n", data); // print consumed data
        sem_post( &holes); // signal presence of gap in buffer
    }
    pthread_exit(0);
}

```

### Sol. and implementation with mutex:
## Code: 
```c
#define MAX_BUFFER 1024 /* size of buffer*/
#define DATA_SIZE 100000 /* number of data items to be produced*/
pthread_mutex_t mutex; /* mutex to access shared buffer */
pthread_cond_t non_full; /* can we add more elements? */
pthread_cond_t non_empty; /* can we remove elements? */
int n_elements; /* number of elements in buffer */
int buffer[MAX_BUFFER]; /* common buffer */
int main() {
	//Initialise the threads
    pthread_t th1, th2;
    // Initialise the mutex and conditional variables
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&non_full, NULL);
    pthread_cond_init(&non_empty, NULL);
    // Create one producer and one consumer thread
    pthread_create(&th1, NULL, producer, NULL);
    pthread_create(&th2, NULL, consumer, NULL);
    // Wait for the threads to finish and join them
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    // Destoy the mutex and conditional variables.
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&non_full);
    pthread_cond_destroy(&non_empty);
    exit(0);
}
```

```c
void producer() { /* Producer code */
	// Initialization of variables
    int data, i ,pos = 0;
    // For each piece of data that needs to be created, create it.
    for(i=0; i < DATA_SIZE; i++ ) {
        data= i; /* generate data */
        pthread_mutex_lock(&mutex); /* access to buffer*/
        while (n_elements == MAX_BUFFER) /* when buffer is full*/
            pthread_cond_wait(&non_full, &mutex);
        buffer[pos] = data;
        pos = (pos + 1) % MAX_BUFFER; // Circular buffer, use remainder.
        n_elements ++; // Added an element.
        pthread_cond_signal(&non_empty); /* buffer is not empty */
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(0);
}
```

```c
void consumer() { /* consumer code */
    int dato, i ,pos = 0;
    for(i=0; i < DATA_SIZE; i++ ) {
        pthread_mutex_lock(&mutex); /* access to buffer */
        while (n_elements == 0) /* when buffer empty */
            pthread_cond_wait(&non_empty, &mutex);
        dato = buffer[pos];
        pos = (pos + 1) % MAX_BUFFER;
        n_elements --;
        pthread_cond_signal(&non_full); /* buffer is not full */
        pthread_mutex_unlock(&mutex);
        printf("Consumed %d \n", data); /* Use data*/
    }
    pthread_exit(0);
}
```
### Other solutions: 
Other solutions such as [Peterson’s Algorithm](https://www.geeksforgeeks.org/petersons-algorithm-in-process-synchronization/) have been proposed. However they are not reliable in modern day architectures. The way to go is to use mutex, **always mutex**

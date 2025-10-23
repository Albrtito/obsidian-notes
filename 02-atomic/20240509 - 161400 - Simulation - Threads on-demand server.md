---
aliases:
  - Simulation - Threads on-demand server
tags:
  - os
"References:": 
cssclasses:
---
# Simulation of a threads on-demand server: 
This simulation is done using [Semaphores](20240503%20-%20190310%20-Semaphores%20Dijkstra%20method.md).

**Remarks:**
+ Careful not to cause race conditions

One single thread is created in the main loop. This thread controls all the creation of other threads from that point forwards. This master thread is based on the receiver function.

## Functions: 

**Main:** 
The main function creates the receiver and initialises all the semaphores, etc. It also computes the time it takes the server each request. 

**Receiver:**
This acts as a master thread. It receives all the request and creates threads to manage the received requests. It uses the semaphore sparam to wait for the just created thread to copy the pointer to the request so it can keep using it’s pointer r. 
Finally it uses the semaphore snchildren to check whether a child has finished or not. 

**Service:** 
One thread based on this function is created for each of the requests. It manages and replies the requests in the reply_requests function. It uses the sparam semaphore to let know the receiver that the resource is copied and the snchildren semaphore to let know the receiver that the thread is going to exit. 

## Used library: 
This library contains the reply and receive function as well as an structure for the requests.
+ [Simulation - Request library Server simulation](20240509%20-%20155259%20-%20Simulation%20-%20Request%20library%20Server%20simulation.md)
## Code: 

```c
# include "request.h"
# include <stdio.h>
# include <time.h>
# include <sys/wait.h>
# include <time.h>
# include <stdlib.h>
# include <unistd.h>
# include <pthread.h>
# include <semaphore.h>

// NOT TESTED

sem_t snchildren;
sem_t sparam; 

void * service(void * r) {
    request_t req;
    // Copy the request
    copy_request(&req,(request_t*)r);
    // Signal the receiver that the request is copied
    sem_post(&sparam);

    // Start reply.
    fprintf(stderr, "Starting service\n");
    reply_request(&req);

    // Post that the reply has ended
    sem_post(&snchildren);
    fprintf(stderr, "Finishing service\n");
    pthread_exit(0);
    return NULL;
}


void * receiver(void * param) {
    const int MAX_REQUESTS = 5;
    int i, nservice = 0;
    request_t r;
    pthread_t th_child;

    // Start creating child threads to manage request
    for (i=0;i<MAX_REQUESTS;i++) {
        receive_request(&r);
        nservice++;
        pthread_create(&th_child, NULL, service, &r);
        // Wait for the child thread to copy the request befor continuing
        sem_wait(&sparam);
    }

    while (nservice>0) {
    fprintf(stderr, "Performing wait\n");
    // Whait for some children to post that it has ended.
    sem_wait(&snchildren);
    // If one child has ended, reduce the threads
    nservice--;
    fprintf(stderr, "Exiting from wait\n");
    }
    
    pthread_exit(0);
    return NULL;
}




int main(){
    time_t t1, t2; 
    double diff; 
    pthread_t thr;


    t1 = time(NULL);

    // Initizalisation of the semaphores
    sem_init(&snchildren, 0, 0);
    sem_init(&sparam, 0, 0);

    // Creation of the control thread
    pthread_create(&thr, NULL,receiver, NULL);
    // Wait for the thread to finish
    pthread_join(thr, NULL);

    // Destoy semaphores
    sem_destroy(&snchildren);
    sem_destroy(&sparam);

    // Compute time
    t2 = time(NULL);
    diff = difftime(t2,t1);
    printf("Time: %lf\n",diff);


    return 0;
}


```

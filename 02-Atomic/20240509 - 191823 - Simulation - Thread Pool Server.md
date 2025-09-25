---
aliases:
  - Simulation - Thread Pool Server
tags:
  - os
"References:": 
cssclasses: 
sr-due: 2024-05-31
sr-interval: 11
sr-ease: 272
---
# Simulation of a thread pool server. 
#duda :I don’t know why but this simulation is performing much worse than it is expected to. 

This simulation is using [Mutex and conditional variables](20240504%20-%20162315%20-%20Mutex%20and%20conditional%20variables.md) instead of semaphores. Just this makes it more flexible and easy to use. 
## Used library: 
This library contains the reply and receive function as well as an structure for the requests.
+ [Simulation - Request library Server simulation](20240509%20-%20155259%20-%20Simulation%20-%20Request%20library%20Server%20simulation.md)
All simulations now use their constants from a new constants file. (library .h)
## Code: 

```c
#include "request.h"
#include "constants.h"
#include <stdio.h>
#include <time.h>
#include <pthread.h>
#include <semaphore.h>
#define MAX_BUFFER 128


request_t buffer[MAX_BUFFER];
int n_elements;
int pos_service = 0;
pthread_mutex_t mutex;
pthread_cond_t non_full;
pthread_cond_t non_empty;
pthread_mutex_t mend;
int end=0;

void * receiver (void * param)
{

    request_t r;
    int i, pos=0;

    for (i=0;i<MAX_REQUESTS;i++)
    {
        receive_request(&r);
        // Lock the mutex to acces the buffer
        pthread_mutex_lock(&mutex);

        // Check for the conditional variable: The buffer is not full
        while (n_elements == MAX_BUFFER){pthread_cond_wait(&non_full, &mutex);}
        
        //Get the request into the buffer position 
        buffer[pos] = r;
        pos = (pos+1) % MAX_BUFFER;
        n_elements++;

        // Signal that the buffer is not empty anymore
        pthread_cond_signal(&non_empty);
        // Acces to the buffer ended, unlock the mutex
        pthread_mutex_unlock(&mutex);
    } // End of receive process

    
    fprintf(stderr,"Finishing receiver\n");
    // Final changes when the receiver finishes
    pthread_mutex_lock(&mend);
    end=1;
    pthread_mutex_unlock(&mend);

    pthread_mutex_lock(&mutex);
    pthread_cond_broadcast(&non_empty);
    pthread_mutex_unlock(&mutex);

    fprintf(stderr, "Finished receiver\n");
    pthread_exit(0);
    return NULL;
} /* receiver*/


void * service (void * param)
{
    request_t r;
    // Infinite loop
    for (;;) {
        // Lock the buffer
        pthread_mutex_lock(&mutex);
        // If the n_elements is  0 means that either nothing has 
        // been inputed into the queue or that there are no more requests.
        while (n_elements == 0) {
            // If end == 1 (changed by the receiver), then finish
            if (end==1) 
            {
            
            fprintf(stderr,"Finishing service\n");
            pthread_mutex_unlock(&mutex);
            pthread_exit(0);

            }
            // If end is not 1. Then wait for the queue not to be empty
            pthread_cond_wait(&non_empty, &mutex);
        } // while
        fprintf(stderr, "Serving position %d\n", pos_service);
        // Get the request from the buffer
        r = buffer[pos_service];
        // Update to get next request next time
        pos_service = (pos_service + 1) % MAX_BUFFER;
        // Alter the number of elemenst (one is being serviced)
        n_elements --;
        // The queue is not full (we've just taken out one)
        pthread_cond_signal(&non_full);
        pthread_mutex_unlock(&mutex);
        // Reply to the request as the request is allready copied locally.
        reply_request(&r);
    }
    pthread_exit(0);
    return NULL;
}/*Service*/

int main()
{
    time_t t1, t2;
    double diff;
    pthread_t thr;
    const int MAX_SERVICE = 5; int i;
    // Create an array of threads
    pthread_t ths[MAX_SERVICE];

    t1 = time(NULL);

    pthread_mutex_init(&mutex,NULL);
    pthread_cond_init(&non_full,NULL);
    pthread_cond_init(&non_empty,NULL);
    pthread_mutex_init(&mend,NULL);

    // Create the receiver thread
    pthread_create(&thr, NULL, receiver, NULL);

    // Create the service threads
    for (i=0;i<MAX_SERVICE;i++) {
        pthread_create(&ths[i], NULL, service, NULL);
    }
    pthread_join(thr, NULL);

    // Wait for all threads to finish
    for (i=0;i<MAX_SERVICE;i++) {
        pthread_join(ths[i],NULL);
    }

    // Destoy the mutex and conditional variables
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&non_full);
    pthread_cond_destroy(&non_empty);
    pthread_mutex_destroy(&mend);

    // Compute the time spent.
    t2 = time(NULL);
    diff = difftime(t2,t1);
    printf("Time: %lf\n",diff);

    return 0;
}


```

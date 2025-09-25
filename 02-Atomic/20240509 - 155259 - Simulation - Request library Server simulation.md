---
aliases:
  - Simulation - Request library Server simulation
tags:
  - os
"References:": 
cssclasses:
---
# Library holding request structure and methods.

The `request.h` library holds the structure with all the request data and the two methods for managing request. 
+ `receive_request(request_t*r){...}`: Manages receiving requests.
+ `reply_request(request_t*r){...}` : Manages **processing and replying** request. 

Because this is a simulated server all I/O times and CPU times are either simulated with some computation loop (CPU) or sleep() function (I/O)

## Code: 
```c
#ifndef REQUEST_H

#define REQUEST_H

struct request {
    long id;
    /* Rest of fields */
    int kind;
    char url[80];
    /* ... */
};

typedef struct request request_t;

void get_request (request_t * r);
void reply_request (request_t * r);

#endif


# include <stdio.h>
# include <time.h>
# include <sys/wait.h>
# include <time.h>
# include <stdlib.h>
# include <unistd.h>

static long reqid = 0;

void receive_request(request_t * r) {

    int delay;
    // Signal that the request is being recieved
    fprintf(stderr, "Receiving request\n");
    
    // Name the request to recieve.
    r->id = reqid++;

    /* Simulate I/O time*/
    delay = rand() % 5;
    sleep(delay);
    fprintf(stderr,"Request %ld received after %d seconds\n", r->id, delay);
}


void reply_request(request_t * r) {
    int delay, i;
    double x;
    
    // Start tith the reply of the request
    fprintf(stderr, "Sending reply %ld\n", r->id);
            
    /* Simulate processing time */
    for (i=0;i<1000000;i++) { x = 2.0 * i; }

    /* Simulate I/O time by creating some random sleep time */
    delay = rand() % 20;
    sleep(delay);

    // Signal the end of the reply
    fprintf(stderr, "Request %ld sent after %d seconds\n", r->id, delay);
}
```
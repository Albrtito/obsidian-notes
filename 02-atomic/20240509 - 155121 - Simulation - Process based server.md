---
aliases:
  - Implementation-Process based server
tags:
  - os
"References:": 
cssclasses: 
sr-due: 2024-06-01
sr-interval: 12
sr-ease: 270
---
# Simulation of a process based server: 

## .h
![Simulation - Request library Server simulation](20240509%20-%20155259%20-%20Simulation%20-%20Request%20library%20Server%20simulation.md)

## code:

```c
# include "request.h"
# include <stdio.h>
# include <time.h>
# include <sys/wait.h>
# include <time.h>
# include <stdlib.h>
# include <unistd.h>

int main()
{
    const int MAX_REQUESTS = 5; 
    int i;
    time_t t1,t2;
    request_t r; 
    int pid, nchildren = 0; 

    t1 = time(NULL);

    for(i = 0; i <MAX_REQUESTS; ++i){
        receive_request(&r);
        do{
            fprintf(stderr,"Checking children\n");
            // WNOHANG makes the waitpid return the pid of any dead processes
            // if there where any. If else the waitpid is returnet as 0.
            pid = waitpid(-1,NULL, WNOHANG); 
            // If  any dead processes where found, lower the number of children
            if(pid>0){nchildren --;}
        // Keep doing this to check for more dead children untill no dead children. then waitpit
        // returns 0 and the loop iteration ends. 
        }while(pid > 0);
    

    pid = fork(); // Create the children
    if (pid<0) {perror("Error creating child");} // Check for errors
    if (pid==0) { reply_request(&r); exit(0); } /* CHILD */
    if (pid!=0) { nchildren++; } /* PARENT*/

    }

    // All children where created. Just wait for them to finish
    fprintf(stderr,"Checking %d children \n", nchildren);
    while(nchildren >0){
        // // This waits blocks the process until some children ends.
        pid = waitpid (-1, NULL, 0); /*Blocking wait*/ 
        // When some children ends, lower the number of children and start again until
        // no childs left.
        if (pid>0){nchildren--;}
    }

    t2 = time(NULL);
    double diff = difftime(t2, t1); 
    
    printf("Time: %lf \n", diff);

    return 0;

}


```

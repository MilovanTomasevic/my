---
layout: page
title: MPI training
description: >
  High-performance computing (HPC)
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Setup

### Installation

```sh
apt-get install libopenmpi-dev 
apt-get install openmpi-bin 
```

### Compilation & Running OpenMP
```sh
gcc -o name name.c -fopenmp
./name
```

### Compilation & Running MPI

```sh
mpicc filename.c -o filename 
mpirun -np 1 ./filename # -lm
```

## Exercises

### mpi_hello_world.c

```c 
#include <mpi.h>
#include <stdio.h>

void main(int argc, char* argv[])
{
  int id = 0;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &id);
  printf("Hello world from %d\n", id);
  MPI_Finalize();
}
```
mpi_hello_world.c - exercises
{:.figure}

### mpi_pnt2pnt.c

```c 
#include <mpi.h>
#include <stdio.h>

void main(int argc, char* argv[])
{
  int id = 0;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &id);
  printf("Hello world from %d\n", id);
  MPI_Finalize();
}
```
mpi_pnt2pnt.c - exercises
{:.figure}

### mpi_pingpong.c

```c 
#include <mpi.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
        MPI_Init(&argc,&argv);

        // Get local rank
        int myRank;
        MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

        // Timing
        double timeStart;
        double timeEnd;
        timeStart = MPI_Wtime();

        // Repeated send/receive several times for accurate timing
        int i;
        int niter=1000;
        for(i = 0; i < niter; i++)
        {
                if(myRank == 0) // Work for process with rank 0
                {
                        MPI_Status status;
                        char ping[5] = "ping";
                        char pongReceive[5];
                        MPI_Send(ping, 5, MPI_CHAR, 1, 17, MPI_COMM_WORLD);
                        MPI_Recv(pongReceive, 5, MPI_CHAR, 1, 23, MPI_COMM_WORLD, &status);
                }
                else if(myRank == 1) // Work for process with rank 1
                {
                        MPI_Status status;
                        char pong[5] = "pong";
                        char pingReceive[5];
                        MPI_Send(pong, 5, MPI_CHAR, 0, 23, MPI_COMM_WORLD);
                        MPI_Recv(pingReceive, 5, MPI_CHAR, 0, 17, MPI_COMM_WORLD, &status);
                }
                else
                {
                }
        }

        // Timing
        timeEnd = MPI_Wtime();
        printf("Commucation time was %10.7f microseconds\n", ((timeEnd-timeStart)/(niter*2))*1000000);

        MPI_Finalize();
}
```
mpi_pingpong.c - exercises
{:.figure}

### mpi_pingpong_nonblocking.c

```c 
#include <mpi.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
        MPI_Init(&argc,&argv);

        // Get local rank
        int myRank;
        MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

        // Timing
        double timeStart;
        double timeEnd;
        timeStart = MPI_Wtime();

        // Repeated send/receive several times for accurate timing
        int i;
        int niter=1000;
        for(i = 0; i < niter; i++)
        {
                if(myRank == 0) // Work for process with rank 0
                {
                        MPI_Status status;
                        char ping[5] = "ping";
                        char pongReceive[5];
                        MPI_Send(ping, 5, MPI_CHAR, 1, 17, MPI_COMM_WORLD);
                        MPI_Recv(pongReceive, 5, MPI_CHAR, 1, 23, MPI_COMM_WORLD, &status);
                }
                else if(myRank == 1) // Work for process with rank 1
                {
                        MPI_Status status;
                        char pong[5] = "pong";
                        char pingReceive[5];
                        MPI_Send(pong, 5, MPI_CHAR, 0, 23, MPI_COMM_WORLD);
                        MPI_Recv(pingReceive, 5, MPI_CHAR, 0, 17, MPI_COMM_WORLD, &status);
                }
                else
                {
                }
        }

        // Timing
        timeEnd = MPI_Wtime();
        printf("Commucation time was %10.7f microseconds\n", ((timeEnd-timeStart)/(niter*2))*1000000);

        MPI_Finalize();
}
```
mpi_pingpong_nonblocking.c - exercises
{:.figure}

### mpi_pi.c

```c 
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
  MPI_Init(&argc, &argv);

  // Get rank and total size of the world
  int myRank, worldsize;
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &worldsize);

  // Initialize variables
  int i;
  double pi = 0;
  int niter = 100000000;

  // Timing
  double start,end;
  start=MPI_Wtime();

  // Calculate part of Leibnitz sum.
  // Work is distributed as follows:
  // Rank 0 sums element 0, worldsize, 2*worldsize...
  // Rank 1 sums element 1, 1+worldsize, 1+2*worldsize... etc.
  for(i = myRank; i < niter; i=i+worldsize)
  {
    pi = pi + pow(-1, i) * (4 / (2*((double) i)+1));
  }

  // Need to aggregate results!
  //double pi_total=0;
  //MPI_Reduce(&pi, &pi_total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  // Stop timing
  end=MPI_Wtime();

  // Print result for local rank
  printf("Rank %d: pi estimate is %f, obtained in %f seconds\n", myRank, pi, end-start);

  // Print aggregated result
  //if(myRank==0)
  //{
  //  printf("Pi estimate after reduce: %.20f\n", pi_total);
  //}

  MPI_Finalize();
}
```
mpi_pi.c - exercises
{:.figure}

### mpi_pi_advanced.c

```c 
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  MPI_Init(&argc, &argv);

  // Get rank and total size of the world
  int myRank, worldsize;
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &worldsize);

  // Initialize variables
  int i;
  double pi = 0;
  int niter = 100000000;

  // Timing
  double start,end;
  start=MPI_Wtime();

  // Calculate part of Leibnitz sum.
  // Work is distributed as follows:
  // Rank 0 sums element 0, worldsize, 2*worldsize...
  // Rank 1 sums element 1, 1+worldsize, 1+2*worldsize... etc.
  for(i = myRank; i < niter; i=i+worldsize)
  {
    pi = pi + pow(-1, i) * (4 / (2*((double) i)+1));
  }

  // Stop timing
  end=MPI_Wtime();

  // Print result for local rank
  printf("Rank %d: pi estimate is %f, obtained in %f seconds\n", myRank, pi, end-start);

  MPI_Finalize();
}
```
mpi_pi_advanced.c - exercises
{:.figure}

## Solutions

### mpi_hello_world.c

```c 
#include <mpi.h>
#include <stdio.h>

void main(int argc, char* argv[])
{
  int id = 0;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &id);
  printf("Hello world from %d\n", id);
  MPI_Finalize();
}

```
mpi_hello_world.c - solutions
{:.figure}

### mpi_pnt2pnt.c

```c 
#include <mpi.h>
#include <stdio.h>

void main(int argc, char* argv[])
{
  int id = 0;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &id);
  printf("Hello world from %d\n", id);
  MPI_Finalize();
}

```
mpi_pnt2pnt.c - solutions
{:.figure}

### mpi_pingpong.c

```c 
#include <mpi.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
        MPI_Init(&argc,&argv);

        // Get local rank
        int myRank;
        MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

        // Timing
        double timeStart;
        double timeEnd;
        timeStart = MPI_Wtime();

        // Repeated send/receive several times for accurate timing
        int i;
        int niter=1000;
        for(i = 0; i < niter; i++)
        {
                if(myRank == 0) // Work for process with rank 0
                {
                        MPI_Status status;
                        char ping[5] = "ping";
                        char pongReceive[5];
                        MPI_Send(ping, 5, MPI_CHAR, 1, 17, MPI_COMM_WORLD);
                        MPI_Recv(pongReceive, 5, MPI_CHAR, 1, 23, MPI_COMM_WORLD, &status);
                }
                else if(myRank == 1) // Work for process with rank 1
                {
                        MPI_Status status;
                        char pong[5] = "pong";
                        char pingReceive[5];
                        MPI_Recv(pingReceive, 5, MPI_CHAR, 0, 17, MPI_COMM_WORLD, &status);
                        MPI_Send(pong, 5, MPI_CHAR, 0, 23, MPI_COMM_WORLD);
                }
                else
                {
                }
        }

        // Timing
        timeEnd = MPI_Wtime();
        printf("Commucation time was %10.7f microseconds\n", ((timeEnd-timeStart)/(niter*2))*1000000);

        MPI_Finalize();
}
```
mpi_pingpong.c - solutions
{:.figure}

### mpi_pingpong_nonblocking.c

```c 
#include <mpi.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
        MPI_Init(&argc,&argv);

        // Get local rank
        int myRank;
        MPI_Comm_rank(MPI_COMM_WORLD, &myRank);

        // Timing
        double timeStart;
        double timeEnd;
        timeStart = MPI_Wtime();

        // Repeated send/receive several times for accurate timing
        int i;
        int niter=1000;
        for(i = 0; i < niter; i++)
        {
                if(myRank == 0) // Work for process with rank 0
                {
                        MPI_Status status;
                        MPI_Request request;
                        char ping[5] = "ping";
                        char pongReceive[5];
                        MPI_Isend(ping, 5, MPI_CHAR, 1, 17, MPI_COMM_WORLD, &request);
                        MPI_Recv(pongReceive, 5, MPI_CHAR, 1, 23, MPI_COMM_WORLD, &status);
                        MPI_Wait(&request, &status);
                }
                else if(myRank == 1) // Work for process with rank 1
                {
                        MPI_Status status;
                        MPI_Request request;
                        char pong[5] = "pong";
                        char pingReceive[5];
                        MPI_Isend(pong, 5, MPI_CHAR, 0, 23, MPI_COMM_WORLD, &request);
                        MPI_Recv(pingReceive, 5, MPI_CHAR, 0, 17, MPI_COMM_WORLD, &status);
                        MPI_Wait(&request, &status);
                }
                else
                {
                }
        }

        // Timing
        timeEnd = MPI_Wtime();
        printf("Commucation time was %10.7f microseconds\n", ((timeEnd-timeStart)/(niter*2))*1000000);

        MPI_Finalize();
}
```
mpi_pingpong_nonblocking.c - solutions
{:.figure}

### mpi_pi.c

```c 
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
  MPI_Init(&argc, &argv);

  // Get rank and total size of the world
  int myRank, worldsize;
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &worldsize);

  // Initialize variables
  int i;
  double pi = 0;
  int niter = 100000000;

  // Timing
  double start,end;
  start=MPI_Wtime();

  // Calculate part of Leibnitz sum.
  // Work is distributed as follows:
  // Rank 0 sums element 0, worldsize, 2*worldsize...
  // Rank 1 sums element 1, 1+worldsize, 1+2*worldsize... etc.
  for(i = myRank; i < niter; i=i+worldsize)
  {
    pi = pi + pow(-1, i) * (4 / (2*((double) i)+1));
  }

  // Need to aggregate results!
  double pi_total=0;
  MPI_Reduce(&pi, &pi_total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  // Stop timing
  end=MPI_Wtime();

  // Print result for local rank
  printf("Rank %d: pi estimate is %f, obtained in %f seconds\n", myRank, pi, end-start);

  // Print aggregated result
  if(myRank==0)
  {
    printf("Pi estimate after reduce: %.20f\n", pi_total);
  }

  MPI_Finalize();
}
```
mpi_pi.c - solutions
{:.figure}

### mpi_pi_v2.c

```c 
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  MPI_Init(&argc, &argv);

  // Get rank and total size of the world
  int myRank, worldsize;
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &worldsize);

  //initialize variables
  int i;
  double pi = 0;
  int niter = 100000000;

  // Devide iterations
  int niter_perrank = niter / worldsize;
  int imin_loop = myRank*niter_perrank;
  int imax_loop = (myRank+1)*niter_perrank;
  printf("Rank %d: calculates elements %d through %d\n", myRank, imin_loop, imax_loop); 
  // Get timing
  double start,end;
  start=MPI_Wtime();

// Calculate PI using Leibnitz sum
  for(i = imin_loop; i < imax_loop; i++)
  {
    pi = pi + pow(-1, i) * (4 / (2*((double) i)+1));
  }

  // Need to aggregate results!
  double pi_total=0;
  MPI_Reduce(&pi, &pi_total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

  // Stop timing
  end=MPI_Wtime();

  // Print result for local rank
  printf("Rank %d: pi estimate is %f, obtained in %f seconds\n", myRank, pi, end-start);

  // Print aggregated result
  if(myRank==0)
  {
    printf("Pi estimate after reduce: %f\n", pi_total);
  }

  MPI_Finalize();
}
```
mpi_pi_v2.c - solutions
{:.figure}

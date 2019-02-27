---
layout: project
title: 'HPC RIVR'
date: 1 Oct 2018
image: /assets/img/projects/ministarstvoobrazovanja1.jpg
screenshot: /assets/img/projects/minSLO.jpg
links:
  - title: Website
    url: http://www.mizs.gov.si/en/
  - title: Demo
    url: https://www.fis.unm.si/en/
caption: Ministry of Education, Science and Sport, Slovenia
description: >
  Milovan Tomašević works as a researcher at the Faculty of Information Studies in Novo Mesto within the project "HPC RIVER" ...
hide_description: true
accent_image: /assets/img/rudolf.gif
accent_color: rgb(0,191,255)

---


Milovan Tomašević works as a researcher at the [_Faculty of Information Studies in Novo Mesto_](https://www.fis.unm.si/en/){:target="_blank"} within the project _"SUPERVISION OF NATIONAL RESEARCH INFRASTRUCTURES - HPC RIVR", the Ministry of Education, Science and Sport, Slovenia, for the period 2018-2020th years_.

![](/assets/img/projects/fis.png)

[_Faculty of Information Studies in Novo Mesto_](https://www.fis.unm.si/en/){:target="_blank"}
{:.figure}


OpenMP is the dominant shared-memory programming model in computational science.

~~~c
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{

  //initialize variables
  int i;
  double pi = 0;
  int niter = 100000000;

  // Get timing
  double start,end;
  start=omp_get_wtime();

  // Calculate PI using Leibnitz sum
  /* Fork a team of threads */
#pragma omp parallel for reduction(+ : pi)
  for(i = 0; i < niter; i++)
  {
    pi = pi + pow(-1, i) * (4 / (2*((double) i)+1));
  } /* Reduction operation is done. All threads join master thread and disband */

  // Stop timing
  end=omp_get_wtime();

  // Print result
  printf("Pi estimate: %.20f, obtained in %f seconds\n", pi, end-start);
}
~~~
C Examples of Parallel Programming with OpenMP (Open Multi-Processing)
{:.figure}


The Message Passing Interface (MPI) is a library specification that allows HPC to pass information between its various nodes and clusters. HPC uses OpenMPI, an open-source, portable implementation of the MPI standard. OpenMPI contains a complete implementation of version 1.2 of the MPI standard and also MPI-2.

OpenMPI is both a runtime and compile-time environment for MPI-compliant code.

~~~c
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
~~~
Message Passing Interface (MPI) - C Examples
{:.figure}

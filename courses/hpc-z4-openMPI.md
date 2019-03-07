---
layout: page
title: Z4-openMPI
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

### Compilation & Running OpenACC

```sh
gcc -o izvrsna_dat izvorna_dat.c -fopenacc
./izvrsna_dat
```

## Primeri

### hello_world.c

~~~c
#include <stdio.h>

#include "mpi.h"

int main(int argc, char *argv[]) {
    int size, rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    printf("Hello World iz %d/%d.\n", rank, size);

    MPI_Finalize();

    return 0;
}

~~~
hello_world.c - primer
{:.figure}

### send_recv.c

~~~c
/**
 * MPI C implementacija sinhrone komunikacije izmedju dva MPI procesa.
 * Proces 0 salje poruku tipa MPI_INT procesu 1. Duzina poruke je 1.
 */

#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {

    int size, rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        int message = 1;
        printf("Proces %d salje poruku procesu %d.\n", rank, 1);
        MPI_Send(&message, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    } else if (rank == 1) {
        int message = 5;
        printf("Proces %d treba da primi poruku od procesa %d.\n", rank, 0);
        MPI_Recv(&message, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, NULL);
        printf("Proces %d primio poruku %d od procesa %d.\n", rank, message, 0);
    }

    MPI_Finalize();

    return 0;
}
~~~
send_recv.c - primer
{:.figure}

### send_recv_nonblocking.c

~~~c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        MPI_Request send_request;
        char *message = "Zdravo!";

        MPI_Issend(message, 8, MPI_CHAR, 1, 0, MPI_COMM_WORLD, &send_request);
        printf("Proces %d inicirao slanje poruke.\n", rank);

        printf("Proces %d radi nesto drugo dok se poruka salje...\n", rank);

        int flag = 0;
        MPI_Test(&send_request, &flag, NULL);
        if (flag != 0) {
            printf("Proces %d je poslao poruku. Sadrzaj bafera ce biti postavljen na \"!ovardZ\".\n", rank);
            message = "!ovardZ";
        } else {
            printf("Proces %d jos nije poslao poruku, pa ona nece biti prepisana.\n", rank);
        }
        printf("Proces %d trenutni tekst poruke: %s\n", rank, message);
    } else {
        MPI_Request receive_request;
        char message[8];

        // Immediate receive. Samo se inicira prijem poruke od procesa 0 iz MPI_COMM_WORLD
        // komunikatora, ali se ne ceka da poruka bude primljena. Nastavlja se dalje sa
        // izvrsavanjem dok sve dok poruka koju je poslao primalac ne bude neophodna za
        // dalji rad (u ovom slucaju to je do linije kada treba ispisati primljenu poruku).
        MPI_Irecv(message, 8, MPI_CHAR, 0, 0, MPI_COMM_WORLD, &receive_request);
        printf("Proces %d inicirao primanje poruke.\n", rank);

        printf("Proces %d radi nesto drugo dok se poruka prima...\n", rank);

        // MPI_Wait je blokirajuca operacija. Nakon sto se zavrsi u message baferu primaoca
        // ce biti poslata poruka. Do ovog trenutka je poruka mogla vec biti kopirana u bafer,
        // ali nema garancije za to.
        // Ukoliko je potrebna neka od informacija status strukture (npr. broj primljenih
        // karaktera), umesto NULL treba proslediti instancu MPI_Status strukture cija ce
        // polja biti popunjena po zavrsetku poziva.
        MPI_Wait(&receive_request, NULL);
        printf("Proces %d primio poruku: \"%s\"\n", rank, message);
    }

    MPI_Finalize();

    return 0;
}
~~~
send_recv_nonblocking.c - primer
{:.figure}

### ping_pong_printf_async.c

~~~c
/* Use the File->Save as selection to save this source code*/
/*                  pong.c Generic Benchmark code
 *               Dave Turner - Ames Lab - July of 1994+++
 *
 *  Most Unix timers can't be trusted for very short times, so take this
 *  into account when looking at the results.  This code also only times
 *  a single message passing event for each size, so the results may vary
 *  between runs.  For more accurate measurements, grab NetPIPE from
 *  http://www.scl.ameslab.gov/ .
 */
#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char **argv)
{
   int myproc, size, other_proc, nprocs, i, last;
   double t0, t1, time;
   double *a, *b;
   double max_rate = 0.0, min_latency = 10e6;
   MPI_Request request, request_a, request_b;
   MPI_Status status;

#if defined (_CRAYT3E)
   a = (double *) shmalloc (132000 * sizeof (double));
   b = (double *) shmalloc (132000 * sizeof (double));
#else
   a = (double *) malloc (132000 * sizeof (double));
   b = (double *) malloc (132000 * sizeof (double));
#endif

   for (i = 0; i < 132000; i++) {
      a[i] = (double) i;
      b[i] = 0.0;
   }

   MPI_Init(&argc, &argv);
   MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
   MPI_Comm_rank(MPI_COMM_WORLD, &myproc);

   if (nprocs != 2) {
	   printf("Error: You don't have two processors available.");
	   exit (1);
   }

   other_proc = (myproc + 1) % 2;

   printf("Hello from %d of %d\n", myproc, nprocs);
   MPI_Barrier(MPI_COMM_WORLD);

/* Timer accuracy test */

   t0 = MPI_Wtime();
   t1 = MPI_Wtime();

   while (t1 == t0) t1 = MPI_Wtime();

   if (myproc == 0)
      printf("Timer accuracy of ~%f usecs\n\n", (t1 - t0) * 1000000);

/* Communications between nodes 
 *   - Blocking sends and recvs
 *   - No guarantee of prepost, so might pass through comm buffer
 */

   for (size = 8; size <= 1048576; size *= 2) {
      for (i = 0; i < size / 8; i++) {
         a[i] = (double) i;
         b[i] = 0.0;
      }
      last = size / 8 - 1;

      MPI_Barrier(MPI_COMM_WORLD);
      t0 = MPI_Wtime();

      if (myproc == 0) {

         MPI_Send(a, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD);
         MPI_Recv(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD, &status);

      } else {

         MPI_Recv(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD, &status);

         b[0] += 1.0;
         if (last != 0)
         b[last] += 1.0;

         MPI_Send(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD);

      }

      t1 = MPI_Wtime();
      time = 1.e6 * (t1 - t0);
      MPI_Barrier(MPI_COMM_WORLD);

      if ((b[0] != 1.0 || b[last] != last + 1)) {
         printf("ERROR - b[0] = %f b[%d] = %f\n", b[0], last, b[last]);
         exit (1);
      }
      for (i = 1; i < last - 1; i++)
         if (b[i] != (double) i)
            printf("ERROR - b[%d] = %f\n", i, b[i]);
      if (myproc == 0 && time > 0.000001) {
         printf(" %7d bytes took %9.0f usec (%8.3f MB/sec)\n",
                     size, time, 2.0 * size / time);
         if (2 * size / time > max_rate) max_rate = 2 * size / time;
         if (time / 2 < min_latency) min_latency = time / 2;
      } else if (myproc == 0) {
         printf(" %7d bytes took less than the timer accuracy\n", size);
      }
   }

/* Async communications
 *   - Prepost receives to guarantee bypassing the comm buffer
 */

   MPI_Barrier(MPI_COMM_WORLD);
   if (myproc == 0) printf("\n  Asynchronous ping-pong\n\n");

   for (size = 8; size <= 1048576; size *= 2) {
      for (i = 0; i < size / 8; i++) {
         a[i] = (double) i;
         b[i] = 0.0;
      }
      last = size / 8 - 1;

      MPI_Irecv(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD, &request);
      MPI_Barrier(MPI_COMM_WORLD);
      t0 = MPI_Wtime();

      if (myproc == 0) {

         MPI_Send(a, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD);
         MPI_Wait(&request, &status);

      } else {

         MPI_Wait(&request, &status);

         b[0] += 1.0;
         if (last != 0)
         b[last] += 1.0;

         MPI_Send(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD);
      }

      t1 = MPI_Wtime();

      time = 1.e6 * (t1 - t0);
      MPI_Barrier(MPI_COMM_WORLD);

      if ((b[0] != 1.0 || b[last] != last + 1))
         printf("ERROR - b[0] = %f b[%d] = %f\n", b[0], last, b[last]);

      for (i = 1; i < last - 1; i++)
         if (b[i] != (double) i)
            printf("ERROR - b[%d] = %f\n", i, b[i]);
      if (myproc == 0 && time > 0.000001) {
         printf(" %7d bytes took %9.0f usec (%8.3f MB/sec)\n",
                  size, time, 2.0 * size / time);
         if (2 * size / time > max_rate) max_rate = 2 * size / time;
         if (time / 2 < min_latency) min_latency = time / 2;
      } else if (myproc == 0) {
         printf(" %7d bytes took less than the timer accuracy\n", size);
      }
   }

/* Bidirectional communications
 *   - Prepost receives to guarantee bypassing the comm buffer
 */

   MPI_Barrier(MPI_COMM_WORLD);
   if (myproc == 0) printf("\n  Bi-directional asynchronous ping-pong\n\n");

   for (size = 8; size <= 1048576; size *= 2) {
      for (i = 0; i < size / 8; i++) {
         a[i] = (double) i;
         b[i] = 0.0;
      }
      last = size / 8 - 1;

      MPI_Irecv(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD, &request_b);
      MPI_Irecv(a, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD, &request_a);
      MPI_Barrier(MPI_COMM_WORLD);

      t0 = MPI_Wtime();

      MPI_Send(a, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD);
      MPI_Wait(&request_b, &status);

      b[0] += 1.0;
      if (last != 0)
      b[last] += 1.0;

      MPI_Send(b, size/8, MPI_DOUBLE, other_proc, 0, MPI_COMM_WORLD);
      MPI_Wait(&request_a, &status);

      t1 = MPI_Wtime();
      time = 1.e6 * (t1 - t0);
      MPI_Barrier(MPI_COMM_WORLD);

      if ((a[0] != 1.0 || a[last] != last + 1))
         printf("ERROR - a[0] = %f a[%d] = %f\n", a[0], last, a[last]);
      for (i = 1; i < last - 1; i++)
      if (a[i] != (double) i)
         printf("ERROR - a[%d] = %f\n", i, a[i]);
      if (myproc == 0 && time > 0.000001) {
         printf(" %7d bytes took %9.0f usec (%8.3f MB/sec)\n",
                    size, time, 2.0 * size / time);
         if (2 * size / time > max_rate) max_rate = 2 * size / time;
         if (time / 2 < min_latency) min_latency = time / 2;
      } else if (myproc == 0) {
         printf(" %7d bytes took less than the timer accuracy\n", size);
      }
   }

   if (myproc == 0)
      printf("\n Max rate = %f MB/sec  Min latency = %f usec\n",
               max_rate, min_latency);

   MPI_Finalize();
   return (0);
}
~~~
ping_pong_printf_async.c - primer
{:.figure}

### ping_pong_printf_variablelen.c

#### MPI_Probe
~~~c
int MPI_Probe(
  int source,
  int tag,
  MPI_Comm comm,
  MPI_Status *status
);
~~~

##### Parameters

- source
  - [in] source rank, or MPI_ANY_SOURCE (integer)
- tag
  - [in] tag value or MPI_ANY_TAG (integer)
- comm
  - [in] communicator (handle)
- status
  - [out] status object (Status)

#### MPI_Get_count
~~~c
int MPI_Get_count(
  MPI_Status *status,
  MPI_Datatype datatype,
  int *count
);
~~~

##### Parameters

- status
  - [in] return status of receive operation (Status)
- datatype
  - [in] datatype of each receive buffer element (handle)
- count
  - [out] number of received elements (integer)

#### MPI_Probe sample code

~~~c
#include "mpi.h"
#include <stdio.h>
 
#define MAX_BUF_SIZE_LG 22
#define NUM_MSGS_PER_BUF_SIZE 5
char buf[1 << MAX_BUF_SIZE_LG];
 
/* 
* This program verifies that MPI_Probe() is operating properly in the face of
* unexpected messages arriving after MPI_Probe() has
* been called.
*/
int main(int argc, char **argv)
{
    int p_size;
    int p_rank;
    int msg_size_lg;
    int errs = 0;
    int mpi_errno;
 
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &p_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &p_rank);
 
    for (msg_size_lg = 0; msg_size_lg <= MAX_BUF_SIZE_LG; msg_size_lg++)
    {
        const int msg_size = 1 << msg_size_lg;
        int msg_cnt;
        printf( "testing messages of size %d\n", msg_size );fflush(stdout);
        for (msg_cnt = 0; msg_cnt < NUM_MSGS_PER_BUF_SIZE; msg_cnt++)
        {
            MPI_Status status;
            const int tag = msg_size_lg * NUM_MSGS_PER_BUF_SIZE + msg_cnt;

            printf( "Message count %d\n", msg_cnt );fflush(stdout);
            if (p_rank == 0)
            {
                int p;

                for (p = 1; p < p_size; p ++)
                {
                    /* Wait for synchronization message */
                    MPI_Recv(NULL, 0, MPI_BYTE, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);
                    if (status.MPI_TAG != tag)
                    {
                        printf("ERROR: unexpected message tag from MPI_Recv(): lp=0, rp=%d, expected=%d, actual=%d, count=%d\n", status.MPI_SOURCE, status.MPI_TAG, tag, msg_cnt);fflush(stdout);
                    }
 
                    /* Send unexpected message which hopefully MPI_Probe() is already waiting for at the remote process */
                    MPI_Send (buf, msg_size, MPI_BYTE, status.MPI_SOURCE, status.MPI_TAG, MPI_COMM_WORLD);
                }
            }
            else
            {
                int incoming_msg_size;
 
                /* Send synchronization message */
                MPI_Send(NULL, 0, MPI_BYTE, 0, tag, MPI_COMM_WORLD);
                /* Perform probe, hopefully before the master process can send its reply */
                MPI_Probe(MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
                MPI_Get_count(&status, MPI_BYTE, &incoming_msg_size);
                if (status.MPI_SOURCE != 0)
                {
                    printf("ERROR: unexpected message source from MPI_Probe(): p=%d, expected=0, actual=%d, count=%d\n", p_rank, status.MPI_SOURCE, msg_cnt);fflush(stdout);
                }
                if (status.MPI_TAG != tag)
                {
                    printf("ERROR: unexpected message tag from MPI_Probe(): p=%d, expected=%d, actual=%d, count=%d\n", p_rank, tag, status.MPI_TAG, msg_cnt);fflush(stdout);
                }
                if (incoming_msg_size != msg_size)
                {
                    printf("ERROR: unexpected message size from MPI_Probe(): p=%d, expected=%d, actual=%d, count=%d\n", p_rank, msg_size, incoming_msg_size, msg_cnt);fflush(stdout);
                }
 
                /* Receive the probed message from the master process */
                MPI_Recv(buf, msg_size, MPI_BYTE, 0, tag, MPI_COMM_WORLD, &status);
                MPI_Get_count(&status, MPI_BYTE, &incoming_msg_size);
                if (status.MPI_SOURCE != 0)
                {
                    printf("ERROR: unexpected message source from MPI_Recv(): p=%d, expected=0, actual=%d, count=%d\n", p_rank, status.MPI_SOURCE, msg_cnt);fflush(stdout);
                }
                if (status.MPI_TAG != tag)
                {
                    printf("ERROR: unexpected message tag from MPI_Recv(): p=%d, expected=%d, actual=%d, count=%d\n", p_rank, tag, status.MPI_TAG, msg_cnt);fflush(stdout);
                }
                if (incoming_msg_size != msg_size)
                {
                    printf("ERROR: unexpected message size from MPI_Recv(): p=%d, expected=%d, actual=%d, count=%d\n", p_rank, msg_size, incoming_msg_size, msg_cnt);fflush(stdout);
                }
            }
        }
    }
 
    MPI_Finalize();
    return 0;
}

~~~
MPI_Probe.c - primer
{:.figure}

#### MPI_Get_count sample code

~~~
#include "mpi.h"
#include <stdio.h>
 
/* Receive partial datatypes and check that MPI_Getelements gives the correct version */
 
int main( int argc, char *argv[] )
{
    int errs = 0;
    MPI_Datatype outtype, oldtypes[2];
    MPI_Aint offsets[2];
    int blklens[2];
    MPI_Comm comm;
    int size, rank, src, dest, tag;
 
    MPI_Init( &argc, &argv );
 
    comm = MPI_COMM_WORLD;
    MPI_Comm_rank( comm, &rank );
    MPI_Comm_size( comm, &size );
    if (size < 2) {
        printf( "This test requires at least 2 processes\n" );fflush(stdout);
        MPI_Abort( MPI_COMM_WORLD, 1 );
    }
 
    src = 0;
    dest = 1;
 
    if (rank == src) {
        int buf[128], position, cnt;
        /* sender */
        /* Create a datatype and send it (multiple of sizeof(int)) */
        /* Create a send struct type */
        oldtypes[0] = MPI_INT;
        oldtypes[1] = MPI_CHAR;
        blklens[0] = 1;
        blklens[1] = 4*sizeof(int);
        offsets[0] = 0;
        offsets[1] = sizeof(int);
        MPI_Type_struct( 2, blklens, offsets, oldtypes, &outtype );
        MPI_Type_commit( &outtype );
 
        buf[0] = 4*sizeof(int);
        MPI_Send( buf, 1, outtype, dest, 0, comm );
        MPI_Type_free( &outtype );
 
        /* Create a datatype and send it (not a multiple of sizeof(int)) */
        /* Create a send struct type */
        oldtypes[0] = MPI_INT;
        oldtypes[1] = MPI_CHAR;
        blklens[0] = 1;
        blklens[1] = 4*sizeof(int)+1;
        offsets[0] = 0;
        offsets[1] = sizeof(int);
        MPI_Type_struct( 2, blklens, offsets, oldtypes, &outtype );
        MPI_Type_commit( &outtype );
 
        buf[0] = 4*sizeof(int) + 1;
        MPI_Send( buf, 1, outtype, dest, 1, comm );
        MPI_Type_free( &outtype );
 
        /* Pack data and send as packed */
        position = 0;
        cnt = 7;
        MPI_Pack( &cnt, 1, MPI_INT, buf, 128*sizeof(int), &position, comm );
        MPI_Pack( "message", 7, MPI_CHAR, buf, 128*sizeof(int), &position, comm );
        MPI_Send( buf, position, MPI_PACKED, dest, 2, comm );
    }
    else if (rank == dest) {
        MPI_Status status;
        int buf[128], i, elms, count;
        /* Receiver */
        /* Create a receive struct type */
        oldtypes[0] = MPI_INT;
        oldtypes[1] = MPI_CHAR;
        blklens[0] = 1;
        blklens[1] = 256;
        offsets[0] = 0;
        offsets[1] = sizeof(int);
        MPI_Type_struct( 2, blklens, offsets, oldtypes, &outtype );
        MPI_Type_commit( &outtype );
 
        for (i=0; i<3; i++) {
            tag = i;
            MPI_Recv( buf, 1, outtype, src, tag, comm, &status );
            MPI_Get_elements( &status, outtype, &elms );
            if (elms != buf[0] + 1) {
                errs++;
                printf( "For test %d, Get elements gave %d but should be %d\n", i, elms, buf[0] + 1 );fflush(stdout);
            }
            MPI_Get_count( &status, outtype, &count );
            if (count != MPI_UNDEFINED) {
                errs++;
                printf( "For partial send, Get_count did not return MPI_UNDEFINED\n" );fflush(stdout);
            }
        }
        MPI_Type_free( &outtype );
    }
 
    MPI_Finalize();
    return errs;
}
~~~
MPI_Get_count.c - primer
{:.figure}

### bcast.c

~~~c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, root = 0;

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int token;
    if (rank == root) token = 123;
    printf("Vrednost zetona procesa %d je %d.\n", rank, token);     // Zeton svakog procesa koji nije root proces neinicijalizovan.
    MPI_Barrier(MPI_COMM_WORLD);                                    // Ne mora da se navodi pre MPI_Bcast, navedeno je samo da
                                                                    // bi svi procesi ispisali svoje vrednosti zetona pre nego se odradi
                                                                    // MPI_Bcast, da se ispisi nakon pre i nakon primanja zetona ne mesaju.
    MPI_Bcast(&token, 1, MPI_INT, root, MPI_COMM_WORLD);
    printf("Proces %d primio token %d.\n", rank, token);

    MPI_Finalize();

    return 0;
}
~~~
bcast.c - primer
{:.figure}

### scatter.c

~~~c
/**
 * OpenMPI program koji demonstrira rad MPI_Scatter funkcije.
 * 
 * Korenski proces (odredjen vrednoscu promenljive 'root') generise niz 'data' duzine 'datalen'
 * elemenata, pocevsi od vrednosti 0, pa do datalen-1. Vrednosti elemenata niza se dalje dele
 * procesima gde svaki proces dobija 'datalen / size' elemenata originalnog niza (size je broj
 * procesa u MPI_COMM_WORLD komunikatoru).
 * 
 * Ocekivani rezultat (za originalni niz duzine 8 i 4 procesa):
 *  proces 0 dobija elemente 0, 1
 *  proces 1 dobija elemente 2, 3
 *  proces 2 dobija elemente 4, 5
 *  proces 3 dobija elemente 6, 7
 *  
 * Pretpostavka:
 *  Program ce biti pozvan sa vrednoscu 1, 2, 4 ili 8 za opciju -np.
 * 
 * Napomena:
 *  Ispis moze biti u proizvoljnom redosledu.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size, root = 0, datalen = 8;  // mozete menjati vrednosti za root i datalen,
                                            // ali i nakon promene datalen mora biti deljivo brojem
                                            // procesa inace primer nece raditi dobro
                                            // 'root' mora imati vrednost ranka nekog od postojecih
                                            // procesa

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int *data = NULL;                       // niz koji sadrzi sve podatke
    int *partial_data = NULL;               // niz koji ce sadrzati delove niza 'data' nakon scatter poziva
    int piecelen = datalen / size;          // svaki proces dobija istu kolicinu podataka
    if (rank == root) {                     // samo proces koji deli podatke inicijalizuje niz 'data'
        data = (int *) malloc(sizeof(int) * datalen);
        for (int i = 0; i < datalen; i++) {
            data[i] = i;
        }
        assert(data != NULL);
    }
    partial_data = (int *) malloc(sizeof(int) * piecelen);
    assert(partial_data != NULL);

    MPI_Scatter(data, piecelen, MPI_INT, partial_data, piecelen, MPI_INT, root, MPI_COMM_WORLD);

    for (int i = 0; i < piecelen; i++) {
        printf("Proces %d dobio element %d.\n", rank, partial_data[i]);
    }
    free(partial_data);
    free(data);

    MPI_Finalize();

    return 0;
}
~~~
scatter.c - primer
{:.figure}

### gather.c

~~~c
/**
 * OpenMPI C program koji demonstrira rad MPI_Gather funkcije.
 * 
 * Svi procesi osim korenskog (odredjen vrednoscu promenljive 'root') generisu niz 'partial_data'
 * duzine 'piecelen' i svaki od nizova inicijalizuju vrednostima od 'piecelen' do 1 dodatim na
 * vrednost ranka procesa. Pozivom MPI_Gather funkcije vrednosti se iz 'partial_data' nizova
 * svih procesa kopiraju u 'data' niz korenskog procesa po rastucoj vrednosti ranka procesa.
 * 
 * Ocekivani rezultat (za 'partila_data' nizove duzine 2 elementa i 4 procesa):
 *  proces 0, partial_data = [2, 1]
 *  proces 1, partial_data = [3, 2]
 *  proces 2, partial_data = [4, 3]
 *  proces 3, partial_data = [5, 4]
 *  proces 0, data = [2, 1, 3, 2, 4, 3, 5, 4]
 *  
 * Pretpostavka:
 *  Program ce biti pozvan sa vrednoscu 1, 2, 4 ili 8 za opciju -np.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size, root = 0, datalen = 8;  // mozete menjati vrednosti za root i datalen,
                                            // ali i nakon promene datalen mora biti deljivo brojem
                                            // procesa inace primer nece raditi dobro
                                            // 'root' mora imati vrednost ranka nekog od postojecih
                                            // procesa

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int *data = NULL;                       // niz koji ce nakon poziva gather funkcije sadrzati sve podatke iz partial_data nizova
    int *partial_data = NULL;               // nizovi koje imaju svi procesi
    int piecelen = datalen / size;          // svaki proces dobija istu kolicinu podataka

    partial_data = (int *) malloc(sizeof(int) * piecelen);
    assert(partial_data != NULL);

    // svaki proces inicijalizuje svoju instancu niza vrednostima od
    // piecelen-1 do 0 (tim redosledom)
    for (int i = 0; i < piecelen; i++) {
        partial_data[i] = rank + piecelen - i;
    }

    if (rank == root) {                     // samo korenski proces alocira prostor za niz koji ce sadrzati sve podatke
        data = (int *) malloc(sizeof(int) * datalen);
        assert(data != NULL);
    }

    MPI_Gather(partial_data, piecelen, MPI_INT, data, piecelen, MPI_INT, root, MPI_COMM_WORLD);

    if (rank == root) {
        printf("Rezultujuci niz nakon poziva MPI_Gather funkcije: ");
        for (int i = 0; i < datalen; i++) {
            printf("%d ", data[i]);
        } printf("\n");
        free(data);
    }
    free(partial_data);

    MPI_Finalize();

    return 0;
}
~~~
gather.c - primer
{:.figure}

### allgather.c

~~~c
/**
 * OpenMPI C program koji demonstrira rad MPI_Allgather funkcije.
 * 
 * Svaki od procesa iz MPI_COMM_WORLD komunikatora pravi po jedan zeton
 * koji ima vrednost ranka tog procesa (promenljiva 'token'). Posto svaki
 * proces nakon poziva MPI_Allgather funkcije treba da primi tokene svih
 * procesa iz komunikatora, svaki od procesa alocira niz 'data' duzine
 * ukupnog broja procesa u komunikatoru. Nakon poziva allgather funkcije
 * nizovi data svih procesa ce biti popunjeni i to tako sto se vrednosti u
 * nizove upisuju u skladu sa rastucom vrednoscu ranka procesa koji salje
 * vrednost. Nakon sto svaki niz popuni svoj niz 'data', svaki proces u
 * komunikatoru ispisuje vrednosti svog niza.
 * 
 * Ocekivani rezultati (u slucaju pokretanja 4 procesa):
 *  proces 0 -> token=0, data nepoznate vrednosti
 *  proces 1 -> token=1, data nepoznate vrednosti 
 *  proces 2 -> token=2, data nepoznate vrednosti
 *  proces 3 -> token=3, data nepoznate vrednosti
 *  <- nakon MPI_Allgather poziva ->
 *  proces 0 -> token=0, data = [0, 1, 2, 3]
 *  proces 1 -> token=1, data = [0, 1, 2, 3]
 *  proces 2 -> token=2, data = [0, 1, 2, 3]
 *  proces 3 -> token=3, data = [0, 1, 2, 3]
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <mpi.h>

int main(int argc, char *argv[]) {

    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int *data = (int *) malloc(sizeof(int) * size);     // svaki proces alocira prostor za 'size' zetona 
                                                        // (1 svoj, size-1 zetona preostalih procesa iz komunikatora)
    assert(data != NULL);

    int token = rank;
    MPI_Allgather(&token, 1, MPI_INT, data, 1, MPI_INT, MPI_COMM_WORLD);

    // Da bi se sprecilo preplitanje ispisa vise procesa na konzolu, ispisi
    // se vrse sekvencijalno, tako sto vrednost svog niza ispisuje samo jedan
    // proces koji je na redu, dok svi ostali cekaju na barijeri.
    // Ovo usporava izvrsavanje programa, ali u ovom slucaju je bitno jasno 
    // ilustrovati efekat izvrsavanja allgather funkcije, pa se vreme izvrsavanja
    // zanemaruje.
    for (int next_rank = 0; next_rank < size; next_rank++) {
        if (rank == next_rank) {
            printf("Elementi niza procesa %d: ", next_rank);
            for (int j = 0; j < size; j++) {
                printf("%d ", data[j]);
            } printf("\n");
        }
        MPI_Barrier(MPI_COMM_WORLD);
    }

    free(data);

    MPI_Finalize();

    return 0;
}
~~~
gather.c - primer
{:.figure}

###  reduce.c 

~~~c
/**
 * OpenMPI C program koji demonstrira rad MPI_Reduce funkcije.
 * 
 * Svaki proces unutar MPI_COMM_WORLD komunikatora pravi po jedan zeton,
 * koji prima vrednost ranka procesa i promenljivu result. Nakon poziva
 * MPI_reduce funkcije, 'result' promenljiva procesa ranga 0 ce imati 
 * vrednost sume rangova svih procesa.
 * 
 * Ocekivani rezultat:
 *  Samo ispis promenljive 'result' procesa 0 treba da sadrzi sumu rangova
 *  svih pokrenutih niti, dok ostali rezultati imaju neku neodredjenu vrednost.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <mpi.h>

int main(int argc, char *argv[]) {

    int rank, size, root = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int token = rank, result;
    MPI_Reduce(&token, &result, 1, MPI_INT, MPI_SUM, root, MPI_COMM_WORLD);

    printf("Proces %d: result = %d.\n", rank, result);

    MPI_Finalize();

    return 0;
}

~~~
reduce.c - primer
{:.figure}

### allreduce.c

~~~c
/**
 * OpenMPI C program koji demonstrira rad MPI_Reduce funkcije.
 * 
 * Svaki proces unutar MPI_COMM_WORLD komunikatora pravi po jedan zeton,
 * koji prima vrednost ranka procesa i promenljivu result. Nakon poziva
 * MPI_reduce funkcije, 'result' promenljiva procesa ranga 0 ce imati 
 * vrednost sume rangova svih procesa.
 * 
 * Ocekivani rezultat:
 *  Samo ispis promenljive 'result' procesa 0 treba da sadrzi sumu rangova
 *  svih pokrenutih niti, dok ostali rezultati imaju neku neodredjenu vrednost.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <mpi.h>

int main(int argc, char *argv[]) {

    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int token = rank, result;
    MPI_Allreduce(&token, &result, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

    printf("Proces %d: result = %d.\n", rank, result);

    MPI_Finalize();

    return 0;
}
~~~
allreduce.c - primer
{:.figure}

## Zadaci

### MatrixVectorMultiplication

#### ReadMe

##### Kompajliranje
Zadatak je moguće kompajlirati:

- direktno iz komandne linije ili
- korišćenjem cmake alata

U prvom slučaju, dodatne opcije kompajliranja je potrebno dodati u formatu ``-opcija``. U drugom slučaju je potrebno
dodati opciju u liniju ``set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${MPI_C_COMPILE_FLAGS}")`` u ``CMakeLists.txt`` datoteci.

###### Kompajliranje iz terminala
Ukoliko želite da koristite izgenerisane ulazne podatke u ``hdf5`` formatu neophodno je imati instaliranu podršku za ovaj
format podataka. Na Ubuntu operativnim sistemina, hdf5 paket možete instalirati pokretanjem sledećih komandi:
```sh
sudo apt install libhdf5-dev 
```
Zatim se pozicinonirati u korenski direktorijum zadatka i pokrenuti:
```sh
h5cc utils/*.h utils/*.c main.c
```
Ukoliko ne želite da koristite ulazne podatke u hdf5 formatu, zadatak možetekompajlirati na sledeći način:
```sh
gcc main.c -DDISABLE_HDF5
```
Ukoliko isključite podršku za učitavanje generisanih ulaznih podataka, potrebno je da 
modifikujete izvorni kod tako da na neki drugi način obezbedite učitavanje ulaznih podataka, ali je obavezno koristiti
vrednosti iz parova datoteka m3x3.h5, v3x1.h5 i m5x5.h5, v5x1.h5 zbog testiranja rešenja zadatka.

###### Kompajliranje ``cmake`` alatom
Ukoliko nemate instalirane ``cmake`` i ``make`` pakete nećete moći ovako da kompajlirate zadatak.

Instalacija na Ubuntu operativnim sistemima:
```sh
sudo apt install cmake make -y
```
Nakon uspešne instalacije, potrebno je da se pozicionirate u korenski direktorijum zadatka i pokrenete sledeće naredbe:

```sh
mkdir build && cd build
cmake ..
make -j4
```
Ukoliko hoćete da iskompajlirate program bez podrške za ``hdf5`` paket, liniju ``cmake ..`` treba zameniti sa 
``cmake -DENABLE_HDF5=OFF ..``. Ukoliko isključite podršku za učitavanje generisanih ulaznih podataka, potrebno je da 
modifikujete izvorni kod tako da na neki drugi način obezbedite učitavanje ulaznih podataka.

##### Pokretanje programa
Pozicionirati se u direktorijum u kojem se nalazi izvršna datoteka i pokrenuti ``mpiexec -np <N> ./a.out``, ili drugi 
naziv ukoliko je drugačije specificirano tokom kompajliranja. ``<N>`` zameniti konkretnim brojem koji predstavlja broj 
procesa koje hoćete da stvorite.

#### main.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#ifndef DISABLE_HDF5
#include "utils/h5_matrix_utils.h"
#endif

#define MFILENAME "../input_data/m3x3.h5"   // modifikovati putanju po potrebi
#define VFILENAME "../input_data/v3x1.h5"   // modifikovati putanju po potrebi

// TODO implementirati sekvencijalnu varijantu mnozenja matrice i vektora.
// Dodati potrebne parametre i u main-u meriti vreme izvrsavanja.
// Za merenje vremena koristiti funkciju MPI_Wtime().
void matrix_vector_multiply();

// TODO implementirati OpenMPI varijantu mnozenja matrice i vektora.
// Dodati potrebne parametre i u main-u meriti vreme izvrsavanja.
// U main-u ispisati oba vremena izvrsavanja.
// Za merenje vremena koristiti funkciju MPI_Wtime().
void matrix_vector_multiply_mpi();

int main() {
    
    float *matrix = NULL, *vector = NULL;
    unsigned long long mrows, mcols, vrows, vcols;
    
#ifndef DISABLE_HDF5
    printf("Matrica:\n");
    matrix = h5_load_matrix(MFILENAME, &mrows, &mcols);
    print_float_matrix(matrix, mrows, mcols);
    assert(matrix != NULL);
#else
    printf("HDF podrska onemogucena!\n");
#endif

#ifndef DISABLE_HDF5
    printf("Vektor:\n");
    vector = h5_load_matrix(VFILENAME, &vrows, &vcols);
    print_float_vector(vector, vrows);
    assert(vector != NULL);
#else
    printf("HDF podrska onemogucena!\n");
#endif
    
    if (vector != NULL) free(vector);
    if (matrix != NULL) free(matrix);
    
    return 0;
}
~~~
main.c - zadatak
{:.figure}

#### CMakeLists.txt

~~~sh
cmake_minimum_required(VERSION 3.5)
project(MatrixVectorMultiplication)

find_package(HDF5)
find_package(MPI)

# additional options
option(ENABLE_HDF5 "Enable HDF5 support." ON)

set(CMAKE_C_STANDARD 11)
set(SOURCE_FILES main.c)

add_executable(MatrixVectorMultiplication ${SOURCE_FILES})

if(ENABLE_C_MPI)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${MPI_C_COMPILE_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${MPI_C_LINK_FLAGS}")
    include_directories(${MPI_C_INCLUDE_PATH})
endif()

if(ENABLE_HDF5)
    if(HDF5_FOUND)
        include_directories(${HDF5_INCLUDE_DIR})
        target_link_libraries(MatrixVectorMultiplication ${HDF5_C_LIBRARIES})
        set(HDF5_SOURCE_FILES utils/h5defs.h utils/h5_matrix_utils.c utils/h5_matrix_utils.h)
        target_sources(MatrixVectorMultiplication PUBLIC ${HDF5_SOURCE_FILES})
    else()
        message(FATAL_ERROR "HDF5 support has been requested, but no HDF5 library was found!")
    endif()
else()
    add_definitions(-DDISABLE_HDF5)
    message(STATUS "HDF5 support disabled.")
endif()

~~~
CMakeLists.txt - zadatak
{:.figure}

#### utils

##### h5defs.h

~~~c
#ifndef MATRIXUTILITIES_H5DEFS_H
#define MATRIXUTILITIES_H5DEFS_H

#include <stdlib.h>
#include <hdf5.h>

// Checks for error during hdf5 library function call (nonzero return value).
#define H5STATUS(e) \
    (if (e < 0) { printf("\nHDF5 error on line %d\n\n", __LINE__ ); exit 1; })

#endif //MATRIXUTILITIES_H5DEFS_H
~~~
h5defs.h - zadatak
{:.figure}

##### h5_matrix_utils.h

~~~c
#ifndef MATRIXUTILITIES_H5_MATRIX_UTILS_H
#define MATRIXUTILITIES_H5_MATRIX_UTILS_H

#include <hdf5.h>
#include "h5defs.h"

/* Move this to a separate file */
float *generate_float_matrix(unsigned long long rows, unsigned long long cols);
double *generate_double_matrix(unsigned int rows, unsigned int cols);               // TODO implement
int *generate_int_matrix(unsigned int rows, unsigned int cols);                     // TODO implement
void print_float_matrix(float *matrix, unsigned long long rows, unsigned long long cols);
void print_float_vector(float *vector, unsigned long long len);
/* **************************** */

/**
 * Generates matrix data and saves it to the hdf5 file.
 *
 * @param filename Name of the output file.
 * @param rows Number of rows in the generated matrix.
 * @param cols Number of columns in the generated matrix.
 */
void h5_save_matrix(const char *filename, unsigned int rows, unsigned int cols);

/**
 * ???
 * Loads matrix data from file specified and returns it to the caller as an
 * twodimensional array.
 *
 * @return A pointer to the loaded matrix data.
 */
void *h5_load_matrix(const char *filename, unsigned long long *rows, unsigned long long *cols);

#endif //MATRIXUTILITIES_H5_MATRIX_UTILS_H
~~~
h5_matrix_utils.h - zadatak
{:.figure}

##### h5_matrix_utils.c

~~~c
#include <time.h>
#include "h5_matrix_utils.h"

void h5_save_matrix(const char *filename, unsigned int rows, unsigned int cols) {

    hid_t file_id, dataspace_id, dataset_id;
    herr_t status;
    hsize_t dims[2];
    
    dims[0] = rows;
    dims[1] = cols;
    
    /* Create a new file */
    H5CHECK( file_id = H5Fcreate(filename, H5F_ACC_TRUNC, H5P_DEFAULT, H5P_DEFAULT) );
    
    /* Create dataspace for dataset. */
    H5CHECK( dataspace_id = H5Screate_simple(2, dims, NULL) );
    
    /* Create dataset. */
    H5CHECK( dataset_id = H5Dcreate(file_id, "/dset", H5T_IEEE_F64LE, dataspace_id, H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT) );
    
    /* Write data to file */
    float *data = generate_float_matrix(rows, cols);
    H5CHECK( H5Dwrite(dataset_id, H5T_NATIVE_FLOAT, H5S_ALL, H5S_ALL, H5P_DEFAULT, data) );
    free(data);
    
    /* Close dataset. */
    H5CHECK( H5Dclose(dataset_id) );
    
    /* Close dataspace. */
    H5CHECK( H5Sclose(dataspace_id) );
    
    /* Close the file */
    H5CHECK( H5Fclose(file_id) );
}

void *h5_load_matrix(const char *filename, unsigned long long *rows, unsigned long long *cols) {
    hid_t file_id, dataset, dspace;// parmset;
    int parm, ndims;
    float *data;
    
    /* Open an existing file */
    H5CHECK( file_id = H5Fopen(filename, H5F_ACC_RDONLY, H5P_DEFAULT) );
    
    /* Locate the datasets. */
    H5CHECK( dataset = H5Dopen(file_id, "/dset", H5P_DEFAULT) );
    
    /* Get dataset dimensions to allocate space for it. */
    H5CHECK( dspace = H5Dget_space(dataset) );
    H5CHECK( ndims = H5Sget_simple_extent_ndims(dspace) );
    hsize_t dims[ndims];
    H5CHECK( H5Sget_simple_extent_dims(dspace, dims, NULL) );
    
    data = (float *) malloc(dims[0] * dims[1] * sizeof(float));
    *rows = 0; *rows = dims[0];
    *cols = 0; *cols = dims[1];
    
    /* Read data back */
    H5CHECK( H5Dread(dataset, H5T_NATIVE_FLOAT, H5S_ALL, H5S_ALL, H5P_DEFAULT, data) );
    
    /* Terminate access to the datasets */
    H5CHECK( H5Dclose(dataset) );
    
    /* Close the file. */
    H5CHECK( H5Fclose(file_id) );
    
    return data;
}

float *generate_float_matrix(unsigned long long rows, unsigned long long cols) {
    
    float *data = (float *) malloc(rows * cols * sizeof(float));
    if (data == NULL) {
        fprintf(stderr, "Error allocating data for a matrix.\n");
        exit(1);
    }
    
    srand((unsigned int) time(NULL));
    for (int i = 0; i < rows * cols; i++) {
        data[i] = (rand() % 10000) / 100.f;
    }
    
    return data;
}

void print_float_matrix(float *matrix, unsigned long long rows, unsigned long long cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%f ", matrix[i * rows + j]);
        } printf("\n");
    }
}

void print_float_vector(float *vector, unsigned long long len) {
    for (int i = 0; i < len; i++) {
        printf("%f ", vector[i]);
    } printf("\n");
}
~~~
h5_matrix_utils.c - zadatak
{:.figure}

##### gch files

- [h5defs.h.gch](../high-performance-computing/v3/utils/h5defs.h.gch){:target="_blank"}
- [h5_matrix_utils.h.gch](../high-performance-computing/v3/utils/h5_matrix_utils.h.gch){:target="_blank"}

#### input_data

- [v3x1.h5](../high-performance-computing/v3/input_data/v3x1.h5){:target="_blank"} 
- [m3x3.h5](../high-performance-computing/v3/input_data/m3x3.h5){:target="_blank"} 
- [v5x1.h5](../high-performance-computing/v3/input_data/v5x1.h5){:target="_blank"} 
- [m5x5.h5](../high-performance-computing/v3/input_data/m5x5.h5){:target="_blank"} 

## MatrixMultiplication

#### ReadMe
##### Kompajliranje
Zadatak je moguće kompajlirati:

- direktno iz komandne linije ili
- korišćenjem cmake alata

U prvom slučaju, dodatne opcije kompajliranja je potrebno dodati u formatu ``-opcija``. U drugom slučaju je potrebno
dodati opciju u liniju ``set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${MPI_C_COMPILE_FLAGS}")`` u ``CMakeLists.txt`` datoteci.

###### Kompajliranje iz terminala
Ukoliko želite da koristite izgenerisane ulazne podatke u ``hdf5`` formatu neophodno je imati instaliranu podršku za ovaj
format podataka. Na Ubuntu operativnim sistemina, hdf5 paket možete instalirati pokretanjem sledećih komandi:
```sh
sudo apt install libhdf5-dev 
```
Zatim se pozicinonirati u korenski direktorijum zadatka i pokrenuti:
```sh
h5cc utils/*.h utils/*.c main.c
```
Ukoliko ne želite da koristite ulazne podatke u hdf5 formatu, zadatak možetekompajlirati na sledeći način:
```sh
gcc main.c -DDISABLE_HDF5
```
Ukoliko isključite podršku za učitavanje generisanih ulaznih podataka, potrebno je da 
modifikujete izvorni kod tako da na neki drugi način obezbedite učitavanje ulaznih podataka, ali je obavezno koristiti
vrednosti date u datotekama m3x3.h5 i m5x5.h5. Da bi se postiglo množenje dve matrice, svaku od prethodno navedenih
matrica pomnožiti samu sobom, ali rešenje napraviti tako da bude nezavisno od podataka koji se nalaze
u matricama (dakle ne treba da bude specifičnosti koje koriste činjenicu da se množe dve iste matrice).

###### Kompajliranje ``cmake`` alatom
Ukoliko nemate instalirane ``cmake`` i ``make`` pakete nećete moći ovako da kompajlirate zadatak.

Instalacija na Ubuntu operativnim sistemima:
```sh
sudo apt install cmake make -y
```
Nakon uspešne instalacije, potrebno je da se pozicionirate u korenski direktorijum zadatka i pokrenete sledeće naredbe:

```sh
mkdir build
cd build
cmake ..
make -j4
```
Ukoliko hoćete da iskompajlirate program bez podrške za ``hdf5`` paket, liniju ``cmake ..`` treba zameniti sa 
``cmake -DENABLE_HDF5=OFF ..``. Ukoliko isključite podršku za učitavanje generisanih ulaznih podataka, potrebno je da 
modifikujete izvorni kod tako da na neki drugi način obezbedite učitavanje ulaznih podataka.

##### Pokretanje programa
Pozicionirati se u direktorijum u kojem se nalazi izvršna datoteka i pokrenuti ``mpiexec -np <N> ./a.out``, ili drugi 
naziv ukoliko je drugačije specificirano tokom kompajliranja. ``<N>`` zameniti konkretnim brojem koji predstavlja broj 
procesa koje hoćete da stvorite.

#### main.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#ifndef DISABLE_HDF5
#include "utils/h5_matrix_utils.h"
#endif

#define M1FILENAME "../input_data/m3x3.h5"   // modifikovati putanju po potrebi
#define M2FILENAME "../input_data/m3x3.h5"   // modifikovati putanju po potrebi

// TODO implementirati sekvencijalnu varijantu mnozenja matrice i vektora.
// Dodati potrebne parametre i u main-u meriti vreme izvrsavanja.
// Za merenje vremena koristiti funkciju MPI_Wtime().
void matrix_multiply();

// TODO implementirati OpenMPI varijantu mnozenja matrice i vektora.
// Dodati potrebne parametre i u main-u meriti vreme izvrsavanja.
// U main-u ispisati oba vremena izvrsavanja.
// Za merenje vremena koristiti funkciju MPI_Wtime().
void matrix_multiply_mpi();

int main() {
    
    float *matrix1 = NULL, *matrix2 = NULL, *result = NULL;
    unsigned long long rows, cols;
    
#ifndef DISABLE_HDF5
    printf("Matrica 1:\n");
    matrix1 = h5_load_matrix(M1FILENAME, &rows, &cols);
    print_float_matrix(matrix1, rows, cols);
    assert(matrix1 != NULL);
#else
    printf("HDF podrska onemogucena!\n");
#endif

#ifndef DISABLE_HDF5
    printf("Matrica 2:\n");
    matrix2 = h5_load_matrix(M2FILENAME, &rows, &cols);
    print_float_matrix(matrix2, rows, cols);
    assert(matrix2 != NULL);
#else
    printf("HDF podrska onemogucena!\n");
#endif
    
    // Primer ispisa matrice (upotrebiti za ispis rezultata)
    // Pri odbrani zadatka ispis rezultata se gleda samo za male matrice
    // (3x3 i 5x5).
    printf("\nTODO ovde ispisati rezultat\n");
    print_float_matrix(matrix1, rows, cols);
    
    
    if (matrix1 != NULL) free(matrix1);
    if (matrix2 != NULL) free(matrix2);
    
    return 0;
}
~~~
main.c - zadatak
{:.figure}

#### CMakeLists.txt

~~~sh
cmake_minimum_required(VERSION 3.5)
project(MatrixMultiplication)

find_package(MPI REQUIRED)
find_package(HDF5)

# additional options
option(ENABLE_HDF5 "Enable HDF5 support." ON)

set(CMAKE_C_STANDARD 11)
set(SOURCE_FILES main.c)

add_executable(MatrixMultiplication ${SOURCE_FILES})

if(MPI_C_FOUND)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${MPI_C_COMPILE_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${MPI_C_LINK_FLAGS}")
    include_directories(${MPI_C_INCLUDE_PATH})
endif()

if(ENABLE_HDF5)
    if(HDF5_FOUND)
        include_directories(${HDF5_INCLUDE_DIR})
        target_link_libraries(MatrixMultiplication ${HDF5_C_LIBRARIES})
        set(HDF5_SOURCE_FILES utils/h5defs.h utils/h5_matrix_utils.c utils/h5_matrix_utils.h)
        target_sources(MatrixMultiplication PUBLIC ${HDF5_SOURCE_FILES})
    else()
        message(FATAL_ERROR "HDF5 support has been requested, but no HDF5 library was found!")
    endif()
else()
    add_definitions(-DDISABLE_HDF5)
    message(STATUS "HDF5 support disabled.")
endif()

~~~
CMakeLists.txt - zadatak
{:.figure}

#### utils

##### h5defs.h

~~~c
#ifndef MATRIXUTILITIES_H5DEFS_H
#define MATRIXUTILITIES_H5DEFS_H

#include <stdlib.h>
#include <hdf5.h>

// Checks for error during hdf5 library function call (nonzero return value).
#define H5STATUS(e) \
    (if (e < 0) { printf("\nHDF5 error on line %d\n\n", __LINE__ ); exit 1; })

#endif //MATRIXUTILITIES_H5DEFS_H
~~~
h5defs.h - zadatak
{:.figure}

##### h5_matrix_utils.h

~~~c
#ifndef MATRIXUTILITIES_H5_MATRIX_UTILS_H
#define MATRIXUTILITIES_H5_MATRIX_UTILS_H

#include <hdf5.h>
#include "h5defs.h"

/* Move this to a separate file */
float *generate_float_matrix(unsigned long long rows, unsigned long long cols);
double *generate_double_matrix(unsigned int rows, unsigned int cols);               // TODO implement
int *generate_int_matrix(unsigned int rows, unsigned int cols);                     // TODO implement
void print_float_matrix(float *matrix, unsigned long long rows, unsigned long long cols);
void print_float_vector(float *vector, unsigned long long len);
/* **************************** */

/**
 * Generates matrix data and saves it to the hdf5 file.
 *
 * @param filename Name of the output file.
 * @param rows Number of rows in the generated matrix.
 * @param cols Number of columns in the generated matrix.
 */
void h5_save_matrix(const char *filename, unsigned int rows, unsigned int cols);

/**
 * ???
 * Loads matrix data from file specified and returns it to the caller as an
 * twodimensional array.
 *
 * @return A pointer to the loaded matrix data.
 */
void *h5_load_matrix(const char *filename, unsigned long long *rows, unsigned long long *cols);

#endif //MATRIXUTILITIES_H5_MATRIX_UTILS_H
~~~
h5_matrix_utils.h - zadatak
{:.figure}

##### h5_matrix_utils.c

~~~c
#include <time.h>
#include "h5_matrix_utils.h"

void h5_save_matrix(const char *filename, unsigned int rows, unsigned int cols) {

    hid_t file_id, dataspace_id, dataset_id;
    herr_t status;
    hsize_t dims[2];
    
    dims[0] = rows;
    dims[1] = cols;
    
    /* Create a new file */
    H5CHECK( file_id = H5Fcreate(filename, H5F_ACC_TRUNC, H5P_DEFAULT, H5P_DEFAULT) );
    
    /* Create dataspace for dataset. */
    H5CHECK( dataspace_id = H5Screate_simple(2, dims, NULL) );
    
    /* Create dataset. */
    H5CHECK( dataset_id = H5Dcreate(file_id, "/dset", H5T_IEEE_F64LE, dataspace_id, H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT) );
    
    /* Write data to file */
    float *data = generate_float_matrix(rows, cols);
    H5CHECK( H5Dwrite(dataset_id, H5T_NATIVE_FLOAT, H5S_ALL, H5S_ALL, H5P_DEFAULT, data) );
    free(data);
    
    /* Close dataset. */
    H5CHECK( H5Dclose(dataset_id) );
    
    /* Close dataspace. */
    H5CHECK( H5Sclose(dataspace_id) );
    
    /* Close the file */
    H5CHECK( H5Fclose(file_id) );
}

void *h5_load_matrix(const char *filename, unsigned long long *rows, unsigned long long *cols) {
    hid_t file_id, dataset, dspace;// parmset;
    int parm, ndims;
    float *data;
    
    /* Open an existing file */
    H5CHECK( file_id = H5Fopen(filename, H5F_ACC_RDONLY, H5P_DEFAULT) );
    
    /* Locate the datasets. */
    H5CHECK( dataset = H5Dopen(file_id, "/dset", H5P_DEFAULT) );
    
    /* Get dataset dimensions to allocate space for it. */
    H5CHECK( dspace = H5Dget_space(dataset) );
    H5CHECK( ndims = H5Sget_simple_extent_ndims(dspace) );
    hsize_t dims[ndims];
    H5CHECK( H5Sget_simple_extent_dims(dspace, dims, NULL) );
    
    data = (float *) malloc(dims[0] * dims[1] * sizeof(float));
    *rows = 0; *rows = dims[0];
    *cols = 0; *cols = dims[1];
    
    /* Read data back */
    H5CHECK( H5Dread(dataset, H5T_NATIVE_FLOAT, H5S_ALL, H5S_ALL, H5P_DEFAULT, data) );
    
    /* Terminate access to the datasets */
    H5CHECK( H5Dclose(dataset) );
    
    /* Close the file. */
    H5CHECK( H5Fclose(file_id) );
    
    return data;
}

float *generate_float_matrix(unsigned long long rows, unsigned long long cols) {
    
    float *data = (float *) malloc(rows * cols * sizeof(float));
    if (data == NULL) {
        fprintf(stderr, "Error allocating data for a matrix.\n");
        exit(1);
    }
    
    srand((unsigned int) time(NULL));
    for (int i = 0; i < rows * cols; i++) {
        data[i] = (rand() % 10000) / 100.f;
    }
    
    return data;
}

void print_float_matrix(float *matrix, unsigned long long rows, unsigned long long cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%f ", matrix[i * rows + j]);
        } printf("\n");
    }
}

void print_float_vector(float *vector, unsigned long long len) {
    for (int i = 0; i < len; i++) {
        printf("%f ", vector[i]);
    } printf("\n");
}
~~~
h5_matrix_utils.c - zadatak
{:.figure}

#### input_data

- [m3x3.h5](../high-performance-computing/v4/input_data/m3x3.h5){:target="_blank"} 
- [m5x5.h5](../high-performance-computing/v4/input_data/m5x5.h5){:target="_blank"} 

## Rešenja

### communicators.c

~~~c
#include <stdio.h>

#include "mpi.h"

int main(int argc, char *argv[]) {

    int wsize, wrank, nsize, nrank;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &wsize);
    MPI_Comm_rank(MPI_COMM_WORLD, &wrank);

    MPI_Comm ncomm;

    MPI_Comm_split(MPI_COMM_WORLD, wrank % 2, wrank, &ncomm);

    MPI_Comm_size(ncomm, &nsize);
    MPI_Comm_rank(ncomm, &nrank);

    printf("MPI_COMM_WORLD rank: %d/%d - ncomm rank: %d/%d\n", wrank, wsize, nrank, nsize);

    MPI_Comm_free(&ncomm);
    MPI_Finalize();

    return 0;
}
~~~
communicators.c - rešenje
{:.figure}

### ping_pong.c

~~~c
// Author: Wes Kendall
// Copyright 2011 www.mpitutorial.com
// This code is provided freely with the tutorials on mpitutorial.com. Feel
// free to modify it for your own use. Any distribution of the code must
// either provide a link to www.mpitutorial.com or keep this header intact.
//
// Ping pong example with MPI_Send and MPI_Recv. Two processes ping pong a
// number back and forth, incrementing it until it reaches a given value.
//
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  const int PING_PONG_LIMIT = 10;

  // Initialize the MPI environment
  MPI_Init(NULL, NULL);
  // Find out rank, size
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // We are assuming at least 2 processes for this task
  if (world_size != 2) {
    fprintf(stderr, "World size must be two for %s\n", argv[0]);
    MPI_Abort(MPI_COMM_WORLD, 1);
  }

  int ping_pong_count = 0;
  int partner_rank = (world_rank + 1) % 2;
  while (ping_pong_count < PING_PONG_LIMIT) {
    if (world_rank == ping_pong_count % 2) {
      // Increment the ping pong count before you send it
      ping_pong_count++;
      MPI_Send(&ping_pong_count, 1, MPI_INT, partner_rank, 0, MPI_COMM_WORLD);
      printf("p%d sent ping_pong_count to p%d and incremented it to %d.\n",
             world_rank, partner_rank, ping_pong_count);
    } else {
      MPI_Recv(&ping_pong_count, 1, MPI_INT, partner_rank, 0, MPI_COMM_WORLD,
               MPI_STATUS_IGNORE);
      printf("p%d received ping_pong_count %d from p%d.\n",
             world_rank, ping_pong_count, partner_rank);
    }
  }
  MPI_Finalize();
}
~~~
ping_pong.c - rešenje
{:.figure}

### ring.c

~~~c
// Author: Wes Kendall
// Copyright 2011 www.mpitutorial.com
// This code is provided freely with the tutorials on mpitutorial.com. Feel
// free to modify it for your own use. Any distribution of the code must
// either provide a link to www.mpitutorial.com or keep this header intact.
//
// Example using MPI_Send and MPI_Recv to pass a message around in a ring.
//
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  // Initialize the MPI environment
  MPI_Init(NULL, NULL);
  // Find out rank, size
  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  int token;
  // Receive from the lower process and send to the higher process. Take care
  // of the special case when you are the first process to prevent deadlock.
  if (world_rank != 0) {
    MPI_Recv(&token, 1, MPI_INT, world_rank - 1, 0, MPI_COMM_WORLD,
             MPI_STATUS_IGNORE);
    printf("Process %d received token %d from process %d\n", world_rank, token,
           world_rank - 1);
  } else {
    // Set the token's value if you are process 0
    token = -1;
  }
  MPI_Send(&token, 1, MPI_INT, (world_rank + 1) % world_size, 0,
           MPI_COMM_WORLD);
  // Now process 0 can receive from the last process. This makes sure that at
  // least one MPI_Send is initialized before all MPI_Recvs (again, to prevent
  // deadlock)
  if (world_rank == 0) {
    MPI_Recv(&token, 1, MPI_INT, world_size - 1, 0, MPI_COMM_WORLD,
             MPI_STATUS_IGNORE);
    printf("Process %d received token %d from process %d\n", world_rank, token,
           world_size - 1);
  }
  MPI_Finalize();
}
~~~
ring.c - rešenje
{:.figure}

### bcast.c

~~~c
// Author: Wes Kendall
// Copyright 2011 www.mpitutorial.com
// This code is provided freely with the tutorials on mpitutorial.com. Feel
// free to modify it for your own use. Any distribution of the code must
// either provide a link to www.mpitutorial.com or keep this header intact.
//
// An example of a function that implements MPI_Bcast using MPI_Send and
// MPI_Recv
//
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

void my_bcast(void* data, int count, MPI_Datatype datatype, int root,
              MPI_Comm communicator) {
  int world_rank;
  MPI_Comm_rank(communicator, &world_rank);
  int world_size;
  MPI_Comm_size(communicator, &world_size);

  if (world_rank == root) {
    // If we are the root process, send our data to everyone
    int i;
    for (i = 0; i < world_size; i++) {
      if (i != world_rank) {
        MPI_Send(data, count, datatype, i, 0, communicator);
      }
    }
  } else {
    // If we are a receiver process, receive the data from the root
    MPI_Recv(data, count, datatype, root, 0, communicator, MPI_STATUS_IGNORE);
  }
}

int main(int argc, char** argv) {
  MPI_Init(NULL, NULL);

  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

  int data;
  if (world_rank == 0) {
    data = 100;
    printf("Process 0 broadcasting data %d\n", data);
    my_bcast(&data, 1, MPI_INT, 0, MPI_COMM_WORLD);
  } else {
    my_bcast(&data, 1, MPI_INT, 0, MPI_COMM_WORLD);
    printf("Process %d received data %d from root process\n", world_rank, data);
  }

  MPI_Finalize();
}
~~~
bcast.c - rešenje
{:.figure}

### avg.c

~~~c
// Author: Wes Kendall
// Copyright 2012 www.mpitutorial.com
// This code is provided freely with the tutorials on mpitutorial.com. Feel
// free to modify it for your own use. Any distribution of the code must
// either provide a link to www.mpitutorial.com or keep this header intact.
//
// Program that computes the average of an array of elements in parallel using
// MPI_Scatter and MPI_Gather
//
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>
#include <assert.h>

// Creates an array of random numbers. Each number has a value from 0 - 1
float *create_rand_nums(int num_elements) {
  float *rand_nums = (float *)malloc(sizeof(float) * num_elements);
  assert(rand_nums != NULL);
  int i;
  for (i = 0; i < num_elements; i++) {
    rand_nums[i] = (rand() / (float)RAND_MAX);
  }
  return rand_nums;
}

// Computes the average of an array of numbers
float compute_avg(float *array, int num_elements) {
  float sum = 0.f;
  int i;
  for (i = 0; i < num_elements; i++) {
    sum += array[i];
  }
  return sum / num_elements;
}

int main(int argc, char** argv) {
  if (argc != 2) {
    fprintf(stderr, "Usage: avg num_elements_per_proc\n");
    exit(1);
  }

  int num_elements_per_proc = atoi(argv[1]);
  // Seed the random number generator to get different results each time
  srand(time(NULL));

  MPI_Init(NULL, NULL);

  int world_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
  int world_size;
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);

  // Create a random array of elements on the root process. Its total
  // size will be the number of elements per process times the number
  // of processes
  float *rand_nums = NULL;
  if (world_rank == 0) {
    rand_nums = create_rand_nums(num_elements_per_proc * world_size);
  }

  // For each process, create a buffer that will hold a subset of the entire
  // array
  float *sub_rand_nums = (float *)malloc(sizeof(float) * num_elements_per_proc);
  assert(sub_rand_nums != NULL);

  // Scatter the random numbers from the root process to all processes in
  // the MPI world
  MPI_Scatter(rand_nums, num_elements_per_proc, MPI_FLOAT, sub_rand_nums,
              num_elements_per_proc, MPI_FLOAT, 0, MPI_COMM_WORLD);

  // Compute the average of your subset
  float sub_avg = compute_avg(sub_rand_nums, num_elements_per_proc);

  // Gather all partial averages down to the root process
  float *sub_avgs = NULL;
  if (world_rank == 0) {
    sub_avgs = (float *)malloc(sizeof(float) * world_size);
    assert(sub_avgs != NULL);
  }
  MPI_Gather(&sub_avg, 1, MPI_FLOAT, sub_avgs, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

  // Now that we have all of the partial averages on the root, compute the
  // total average of all numbers. Since we are assuming each process computed
  // an average across an equal amount of elements, this computation will
  // produce the correct answer.
  if (world_rank == 0) {
    float avg = compute_avg(sub_avgs, world_size);
    printf("Avg of all elements is %f\n", avg);
    // Compute the average across the original data for comparison
    float original_data_avg =
      compute_avg(rand_nums, num_elements_per_proc * world_size);
    printf("Avg computed across original data is %f\n", original_data_avg);
  }

  // Clean up
  if (world_rank == 0) {
    free(rand_nums);
    free(sub_avgs);
  }
  free(sub_rand_nums);

  MPI_Barrier(MPI_COMM_WORLD);
  MPI_Finalize();
}
~~~
avg.c - rešenje
{:.figure}


---
layout: page
title: Z7-openACC
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

### ptraliasing.c

~~~c
void assign(int *a, int *b, int size) {
    #pragma acc kernels
    {
        for (int i = 0; i < size - 1; i++)
            a[i] = b[i + 1];
    }
}

int main() {
    return 0;
}
~~~
ptraliasing.c
{:.figure}

### parallel.c

~~~c
#include <stdio.h>
#include <stdlib.h>

#ifdef _OPENACC
#include <openacc.h>
#endif

int main() {

	float *values = (float *) malloc(sizeof(float) * size);

	#pragma acc parallel
	for (int i = 0; i < 1024; i++)
		values[i] = 1.f;

	free(values);

	return 0;
}
~~~
parallel.c
{:.figure}

### parallelloop.c

~~~c
#include <stdlib.h>
#include <openacc.h>

#define N 1024
#define M 1024

int main() {

  float *A = (float *) malloc(N * M * sizeof(float));

  #pragma acc parallel loop gang
  for (int i=0; i<N; i++)
      #pragma acc loop vector
      for (int j=0; j<M; j++)
        A[i * N + j] = 1.f;
    
  free(A);

  return 0;
}
~~~
parallelloop.c
{:.figure}

### data.c

~~~c
#include <stdlib.h>

#define N 1024

int main() {

  float *x = (float *) malloc(sizeof(float) * N);
  float *y = (float *) malloc(sizeof(float) * N);

  #pragma acc data
  {
    #pragma acc parallel loop
    for (int i=0; i<N; i++) {
      y[i] = 0.0f;
      x[i] = (float)(i+1);
    }
    #pragma acc parallel loop
    for (int i=0; i<N; i++) {
      y[i] = 2.0f * x[i] + y[i];
    }
  }

  free(x); free(y);

  return 0;
}
~~~
data.c
{:.figure}

### matrixop.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MSIZE 64
//#define PRINT

int main(int argc, char *argv[]) {

    int *randomMatrix = (int *) calloc(MSIZE * MSIZE * sizeof(int));

    clock_t t1, t2;
    t1 = clock();
    int i, j;
    #pragma acc kernels
    {
        for(i = 0; i < MSIZE; i++) {
            for(j = 0; j < MSIZE; j++) {
                randomMatrix[j * MSIZE + i] = randomMatrix[j * MSIZE + i] + 2;
              }
        }
    }
    t2 = clock();

#ifdef PRINT
  for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        printf("matrica[%d,%d] = %d\n", i, j, randomMatrix[i * MSIZE + J);
      }
  }
#endif

    free(randomMatrix);
    printf("Elapsed Time: %f ms\n",((float)(t2 - t1) / 1000000.0F ) * 1000);
    return 0;
}

~~~
matrixop.c
{:.figure}

### matrixop-coalesced.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MSIZE 64
//#define PRINT

int main(int argc, char *argv[]) {

  int *randomMatrix = (int *) calloc(MSIZE * MSIZE * sizeof(int));

  clock_t t1, t2;
  t1 = clock();
  int i, j;
  #pragma acc kernels
  {
      for(i = 0; i < MSIZE; i++)
          for(j = 0; j < MSIZE; j++)
              randomMatrix[i * MSIZE + j] = randomMatrix[i * MSIZE + j] + 2;
  }
  t2 = clock();

#ifdef PRINT
  for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        printf("matrica[%d,%d] = %d\n", i, j, randomMatrix[i * MSIZE + J);
      }
  }
#endif

  free(randomMatrix);
  printf("Elapsed Time: %f ms\n",((float)(t2 - t1) / 1000000.0F ) * 1000);

  return 0;
}
~~~
matrixop-coalesced.c
{:.figure}

### matrixinit.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <openacc.h>

#define MSIZE 64
//#define PRINT

int main(int argc, char *argv[]) {

  int *randomMatrix = (int *) malloc(MSIZE * MSIZE * sizeof(int));

  clock_t t1, t2;
  t1 = clock();
  #pragma acc kernels
  {
    for(int i = 0; i < MSIZE; i++) {
        for(int j = 0; j < MSIZE; j++) {
            randomMatrix[i * MSIZE + j] = (i + j) % 2;
        }
      }
  }
  t2 = clock();

#ifdef PRINT
  for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        printf("matrica[%d,%d] = %d\n", i, j, randomMatrix[i * MSIZE + J);
      }
  }
#endif

  free(randomMatrix);
  printf("Elapsed Time: %f ms\n",((float)(t2 - t1) / 1000000.0F ) * 1000);
}
~~~
matrixinit.c
{:.figure}

### matrixinitdiv.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <openacc.h>

#define MSIZE 64
//#define PRINT

int main(int argc, char *argv[]) {
  
  int *randomMatrix = (int *) malloc(MSIZE * MSIZE * sizeof(int));

  clock_t t1, t2;
  t1 = clock();
  #pragma acc kernels
  {
    for(int i = 0; i < MSIZE; i++) {
        for(int j = 0; j < MSIZE; j++) {
            if ((i + j) % 2) {
                randomMatrix[i * MSIZE + j] = 1;
            } else {
                randomMatrix[i * MSIZE + j] = 0;
            }
        }
      }
  }
  t2 = clock();

#ifdef PRINT
  for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        printf("matrica[%d,%d] = %d\n", i, j, randomMatrix[i * MSIZE + J);
      }
  }
#endif

  free(randomMatrix);
  printf("Elapsed Time: %f ms\n",((float)(t2 - t1) / 1000000.0F ) * 1000);

  return 0;
}
~~~
matrixinitdiv.c
{:.figure}
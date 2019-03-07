---
layout: page
title: Z1-openMP
description: >
  High-performance computing (HPC)
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

```c
#include <stdio.h>

#include "omp.h"

int main() {

    // Ukoliko se ova linija stavi izvan parallel konstrukta, id je uvek 0.
    // Izgleda da je to id jedine niti koja je aktivna, a koja ce kasnije
    // postati master nit.
    // int id = omp_get_thread_num();

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        printf("Hello(%d)", id);
        printf(" world!(%d)\n", id);
    }

    return 0;
}
```
hello_world.c
{:.figure}

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

## Zadaci

### Pi.c

```c 
#include <stdio.h>
#include <omp.h>

static long num_steps = 100000;

double step;
void serial_code();

int main() {
    printf("*************** Sekvencijalna implementacija ***************\n");
    serial_code();
    printf("************************************************************\n");
}

void serial_code() {
    double start = omp_get_wtime();
    int i;
    double x, pi, sum = 0.0;

    step = 1.0 / (double) num_steps;

    for (i = 0; i < num_steps; i++) { 
        double x = (i + 0.5) * step;printf("%s\n", );
        sum = sum + 4.0 / (1.0 + x * x);
    }

    pi = step * sum;
    double end = omp_get_wtime();

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

```
Pi.c - zadatak
{:.figure}

### mandelbrot.c

```c
// mandelbrot.c

/**
 * OpenMP paralelizovan Mandelbrotov algoritam. Program ne daje ispravne rezultate
 * zbog stetnog preplitanja koje se pojavljuje u njemu. Pronaci i otkloniti greske koje
 * su uzrok stetnom preplitanju. Ocekivani izlaz ispravnog programa za promenljivu area
 * je oko 1.512, dok je ocekivani izlaz za promenljivu error oko 0.0052.
 * 
 * Smernice:
 *  - Proveriti da li vrednosti promenljivih zadatih u zadatku utice na rezultat (npr.
 *  promena vrednosti promenljive eps).
 *  - Videti kako promena broja niti utice na tacnost rezultata. Pokrenuti program iz 
 *  terminala sa OMP_NUM_THREADS=1 && ./a.out. Izmeniti vrednosti zadate za broj niti
 *  i naziv izvrsne datoteke tako da odgovaraju zadatku.
 *  - Videti kako vise pokretanja iste izvrsne datoteke sa fiksiranim brojem niti utice
 *  na rezultat.
 */

#include <stdio.h>
#include <omp.h>

#define NPOINTS 1000
#define MXITR 1000

void testpoint(void);
struct d_complex {
    double r; double i;
};
struct d_complex c;
int numoutside = 0;

int main(){
    int i, j;
    double area, error, eps = 1.0e-5;
    #pragma omp parallel for default(shared) private(c, eps)
    for (i = 0; i < NPOINTS; i++) {
        for (j = 0; j < NPOINTS; j++) {
            c.r = -2.0 + 2.5 * (double)(i) / (double)(NPOINTS) + eps;
            c.i = 1.125 * (double)(j) / (double)(NPOINTS) + eps;
            testpoint();
        }
    }
    area = 2.0 * 2.5 * 1.125 * (double)(NPOINTS*NPOINTS-numoutside) / (double)(NPOINTS*NPOINTS);
    error = area / (double)NPOINTS;

    printf("area = %lf, error = %lf\n", area, error);

    return 0;
}

void testpoint(void){
    struct d_complex z;
    int iter;
    double temp;
    z = c;
    for (iter = 0; iter < MXITR; iter++){
        temp = (z.r * z.r) - (z.i * z.i) + c.r;
        z.i = z.r * z.i * 2 + c.i;
        z.r = temp;
        if ((z.r * z.r + z.i * z.i) > 4.0) {
            numoutside++;
            break;
        }
    }
}
```
mandelbrot.c - zadatak 
{:.figure}

### linkedlist.c

```c
// Linked.c

#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

#ifndef N
#define N 5
#endif
#ifndef FS
#define FS 38
#endif

struct node {
    int data;
    int fibdata;
    struct node* next;
};

int fib(int n) {
    int x, y;
    if (n < 2) {
        return (n);
    } else {
        x = fib(n - 1);
        y = fib(n - 2);
        return (x + y);
    }
}

// Funkcija koja procesira svaki element liste. Za svaki element
// liste se racuna vrednost n-tog elementa Fibonacijevog niza.
// Zadatak funkcije nije narocito bitan. Ono sto jeste bitno je da
// je racunanje n-tog elementa Fibonacijevog niza vremenski zahtevan
// posao.
void processwork(struct node* p) 
{
    int n;
    n = p->data;
    p->fibdata = fib(n);
}

// Inicijalizacija liste. U listu se uvezuje N elemenata i svakom
// se dodeljuje redni broj elementa Fibonacijevog niza koji je
// potrebno sracunati (od FS + 1, pa nadalje).
struct node* init_list(struct node* p) {
    int i;
    struct node* head = NULL;
    struct node* temp = NULL;
    
    head = malloc(sizeof(struct node));
    p = head;
    p->data = FS;
    p->fibdata = 0;
    for (i = 0; i < N; i++) {
        temp = malloc(sizeof(struct node));
        p->next = temp;
        p = temp;
        p->data = FS + i + 1;
        p->fibdata = i + 1;
    }
    p->next = NULL;
    return head;
}

int main(int argc, char *argv[]) {
    double start, end;
    struct node *p = NULL;
    struct node *temp = NULL;
    struct node *head = NULL;
    
	printf("Process linked list\n");
    printf("  Each linked list node will be processed by function 'processwork()'\n");
    printf("  Each ll node will compute %d fibonacci numbers beginning with %d\n", N, FS);      

    p = init_list(p);
    head = p;
    start = omp_get_wtime();

    {  // TODO paralelizujete izvrsavanje ove petlje
        while (p != NULL) {
            processwork(p);
            p = p->next;
        }
    }
    end = omp_get_wtime();

    // Oslobadjanje memorije zauzete za listu.
    p = head;
    while (p != NULL) {
        printf("%d : %d\n", p->data, p->fibdata);
        temp = p->next;
        free(p);
        p = temp;
    }  
    free(p);

    printf("Compute Time: %f seconds\n", end - start);
    return 0;
}
```
linkedlist.c - zadatak 
{:.figure}

## Rešenja

### Pi.c

```c 
/**
 * Program koji racuna vrednost integrala funkcije 4/(1+x^2). Numericki,
 * ova vrednost je jednaka broju pi.
 *
 * Originalni materijal za ovaj primer je preuzet iz niza prezentacija
 * "Introduction to OpenMP" ciji je autor Tim Mattson
 */

#include <stdio.h>
#include <omp.h>

#define NUM_THREADS 2
#define PADDING 8

#define PRINT_SEQ_RES 1
#define PRINT_PRL_RES_BASIC 1
#define PRINT_PRL_RES_NO_FALSE_SHARING 1
#define PRINT_PRL_RES_SYNCHRONIZATION 1
#define PRINT_PRL_RES_FOR_CONSTRUCT 1

static long num_steps = 100000000;

double step;
void serial_code();
void parallel_code_incorrect();
void parallel_code();
void parallel_code_no_false_sharing();
void parallel_code_synchronization();
void parallel_code_for_construct();

int main() {

#if PRINT_SEQ_RES
    printf("*************** Sekvencijalna implementacija ***************\n");
    serial_code();
    printf("************************************************************\n");
#endif
#if PRINT_SEQ_RES
    printf("************ Neispravna paralelna implementacija ************\n");
    parallel_code_incorrect();
    printf("************************************************************\n");
#endif
#if PRINT_PRL_RES_BASIC
    printf("***************** Paralelna implementacija *****************\n");
    parallel_code();
    printf("************************************************************\n");
#endif
#if PRINT_PRL_RES_NO_FALSE_SHARING
    printf("***** Paralelna implementacija (nema laznog deljenja) ******\n");
    parallel_code_no_false_sharing();
    printf("************************************************************\n");
#endif
#if PRINT_PRL_RES_SYNCHRONIZATION
    printf("******** Paralelna implementacija (sinhronizacija) *********\n");
    parallel_code_synchronization();
    printf("************************************************************\n");
#endif
#if PRINT_PRL_RES_FOR_CONSTRUCT
    printf("******** Paralelna implementacija (for konstrukcija) ********\n");
    parallel_code_for_construct();
    printf("************************************************************\n");
#endif

    return 0;
}

/*
 * Sekvencijalna implementacija programa.
 */
void serial_code() {
    double start = omp_get_wtime();     // trenutak pocetka merenja vremena
    int i;
    double x, pi, sum = 0.0;

    step = 1.0 / (double) num_steps;

    for (i = 0; i < num_steps; i++) { 
        double x = (i + 0.5) * step;
        sum = sum + 4.0 / (1.0 + x * x);
    }

    pi = step * sum;
    double end = omp_get_wtime();       // trenutak zavrsetka merenja vremena

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

/*
 * OpenMP paralelizovana verzija sekvencijalnog programa. Rezultat izvrsavanja programa
 * je netacan, jer u kodu postoji stetno preplitanje (parallel konstrukcija).
 */ 
void parallel_code_incorrect() {
    double start = omp_get_wtime();
    int i;
    double x, pi, sum = 0.0;

    step = 1.0 / (double) num_steps;

    #pragma omp parallel
    {
        for (i = 0; i < num_steps; i++) { 
            double x = (i + 0.5) * step;
            sum = sum + 4.0 / (1.0 + x * x);
        }
    }

    pi = step * sum;
    double end = omp_get_wtime();

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

/**
 * OpenMP paralelizovana verzija sekvencijalnog programa sa uklonjenim stetnim preplitanjem
 * (parallel konstrukcija + lokalni podaci)
 */
void parallel_code() {
    double start = omp_get_wtime();

    int i, nthreads;
    double x, pi, sum[NUM_THREADS];

    step = 1.0 / (double) num_steps;

    // Funkcijom omp_set_num_threads programer zapravo zahteva odredjeni broj niti,
    // sto ne znaci nuzno da ce zahtevani broj niti stvarno biti i pokrenut. Okruzenje
    // moze da odluci da napravi manji broj niti od zahtevanog.
    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int i, id, nthrds;
        id = omp_get_thread_num();
        // Kako zahtevani broj niti i broj napravljenih niti mogu biti razliciti, 
        // potrebno je unutar pralelnog regiona proveriti koliko je niti stvarno
        // napravljeno i aktivirano.
        nthrds = omp_get_num_threads();

        // Kako je neophodno sabrati sve parcijalne rezultate izvan paralelog regiona
        // (dovoljno je da) jedna od niti sacuva informaciju o broju aktivnih niti
        // unutar paralelnog regiona. Kada se paralelni region zavrsi, sve niti koje 
        // su vrsile racun osim master niti ce biti unistene i ova informacija vise
        // nece biti dostupna.
        if (id == 0) nthreads = nthrds;

        // Round-robin raspodela intervala. Stetno preplitanje uklonjeno
        // tako sto svaka nit ima svoju promenljivu u koju upisuje rezultat
        // racunanja.
        for (i = id, sum[id] = 0; i < num_steps; i += nthrds) { 
            double x = (i + 0.5) * step;
            sum[id] = sum[id] + 4.0 / (1.0 + x * x);    // ova linija dovodi do laznog deljenja (false sharing)
        }
    }
    for (i = 0; i < nthreads; i++) pi += sum[i];  
    pi *= step;  

    double end = omp_get_wtime();

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

/**
 * Paralelni OpenMP program u kojem nema laznog deljenja rezultata (rezultat promenljive
 * sum). Lazno deljenje je eliminisano uvodjenjem PADDING parametra.
 */
void parallel_code_no_false_sharing() {
    double start = omp_get_wtime();

    int i, nthreads;
    double x, pi, sum[NUM_THREADS][PADDING];

    step = 1.0 / (double) num_steps;

    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int i, id, nthrds;
        id = omp_get_thread_num();
        nthrds = omp_get_num_threads();

        if (id == 0) nthreads = nthrds;

        for (i = id, sum[id][0] = 0; i < num_steps; i += nthrds) { 
            double x = (i + 0.5) * step;
            sum[id][0] = sum[id][0] + 4.0 / (1.0 + x * x);
        }
    }
    for (i = 0; i < nthreads; i++) pi += sum[i][0];
    pi *= step;    

    double end = omp_get_wtime(); 

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

/**
 * Paralelni OpenMP program u kojem nema laznog deljenja rezultata (rezultat promenljive
 * sum). Lazno deljenje je eliminisano uvodjenjem sinhronizacije izmedju niti.
 */
void parallel_code_synchronization() {
    double start = omp_get_wtime();
    int i, nthreads;
    double x, pi = 0.0, sum = 0.0;

    step = 1.0 / (double) num_steps;

    omp_set_num_threads(NUM_THREADS);
    #pragma omp parallel
    {
        int i, id, nthrds;
        double x, sum = 0.0;

        id = omp_get_thread_num();
        nthrds = omp_get_num_threads();

        if (id == 0) nthreads = nthrds;

        for (i = id; i < num_steps; i += nthrds) { 
            x = (i + 0.5) * step;
            sum += 4.0 / (1.0 + x * x);
        }
        #pragma omp critical // moze i atomic
        pi += sum;
    }
    pi *= step;

    double end = omp_get_wtime();

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

/** 
 * Verzija programa paralelizovana OpenMP for konstrukcijom i redukcionom klauzom.
 */
void parallel_code_for_construct() {
    double start = omp_get_wtime();
    int i;
    double x, pi, sum = 0.0;

    step = 1.0 / (double) num_steps;

    {
        #pragma omp parallel for reduction(+:sum)
        for (i = 0; i < num_steps; i++) { 
            double x = (i + 0.5) * step;
            sum = sum + 4.0 / (1.0 + x * x);
        }
    }

    pi = step * sum;
    double end = omp_get_wtime();

    printf("pi = %lf\n", pi);
    printf("Time elapsed: %lf\n", end - start);
}

```
Pi.c - rešenje
{:.figure}

### mandelbrot.c

```c
#include <stdio.h>
#include <omp.h>

#define NPOINTS 1000
#define MXITR 1000

struct d_complex {
    double r; double i;
};
struct d_complex c;
int numoutside = 0;

void testpoint(struct d_complex);

int main(){
    int i, j;
    double area, error, eps = 1.0e-5;

    // Ispravka linije 33 iz mandelbrot.c datoteke
    // Prethodna verzija ove linije: #pragma omp parallel for default(shared) private(c, eps)
    //  1.  private(eps) ce kao posledicu imati kreiranje privatne promenljive eps za svaku
    //      nit, ali ta nova promenljiva ce ostati neinicijalizovana. 
    //      Resenje: zameniti sa firstprivate(eps)
    //  2.  nedostaje private(j) - openmp for konstrukt ce brojacku promenljivu i automatski
    //      proglasiti privatnom. Medjutim, to ne vazi za promenljivu j koja je deklarisana
    //      izvan paralelnog regiona i koja ce biti deljena izmedju niti.
    //      Resenje: Dodati j u private klauzu ili umesto toga dodati collapse(2) (u ovom
    //      slucaju se moze koristiti jer su petlje savrseno ugnjezdene).
    #pragma omp parallel for default(none) private(j, c)\
            firstprivate(eps)
    for (i = 0; i < NPOINTS; i++) {
        for (j = 0; j < NPOINTS; j++) {
            c.r = -2.0 + 2.5 * (double)(i) / (double)(NPOINTS) + eps;
            c.i = 1.125 * (double)(j) / (double)(NPOINTS) + eps;

            // Ispravka linije 38 iz mandelbrot.c datoteke
            // Prethodna verzija ove linije: testpoint();
            // Ako se ne prosledi privatna kopija verzija promenljive c, funkcija
            // testpoint ce raditi na statickoj, tj. globalno vidljivoj verziji 
            // promenljive c.
            testpoint(c);
        }
    }
    area = 2.0 * 2.5 * 1.125 * (double)(NPOINTS*NPOINTS-numoutside) / (double)(NPOINTS*NPOINTS);
    error = area / (double)NPOINTS;

    printf("area = %lf, error = %lf\n", area, error);
}

void testpoint(struct d_complex c){
    struct d_complex z;
    int iter;
    double temp;
    z = c;
    for (iter = 0; iter < MXITR; iter++){
        temp = (z.r * z.r) - (z.i * z.i) + c.r;
        z.i = z.r * z.i * 2 + c.i;
        z.r = temp;
        if ((z.r * z.r + z.i * z.i) > 4.0) {
            {
                #pragma omp atomic
                numoutside++;
            }
            break;
        }
    }
}
```
mandelbrot.c - rešenje 
{:.figure}

### linkedlist.c

```c
#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

#ifndef N
#define N 5
#endif
#ifndef FS
#define FS 38
#endif

struct node {
    int data;
    int fibdata;
    struct node* next;
};

int fib(int n) {
    int x, y;
    if (n < 2) {
        return (n);
    } else {
        x = fib(n - 1);
        y = fib(n - 2);
        return (x + y);
    }
}

// Funkcija koja procesira svaki element liste. Za svaki element
// liste se racuna vrednost n-tog elementa Fibonacijevog niza.
// Zadatak funkcije nije narocito bitan. Ono sto jeste bitno je da
// je racunanje n-tog elementa Fibonacijevog niza vremenski zahtevan
// posao.
void processwork(struct node* p) 
{
    int n;
    n = p->data;
    p->fibdata = fib(n);
}

// Inicijalizacija liste. U listu se uvezuje N elemenata i svakom
// se dodeljuje redni broj elementa Fibonacijevog niza koji je
// potrebno sracunati (od FS + 1, pa nadalje).
struct node* init_list(struct node* p) {
    int i;
    struct node* head = NULL;
    struct node* temp = NULL;
    
    head = malloc(sizeof(struct node));
    p = head;
    p->data = FS;
    p->fibdata = 0;
    for (i = 0; i < N; i++) {
        temp = malloc(sizeof(struct node));
        p->next = temp;
        p = temp;
        p->data = FS + i + 1;
        p->fibdata = i + 1;
    }
    p->next = NULL;
    return head;
}

int main(int argc, char *argv[]) {
    double start, end;
    struct node *p = NULL;
    struct node *temp = NULL;
    struct node *head = NULL;
    
	printf("Process linked list\n");
    printf("  Each linked list node will be processed by function 'processwork()'\n");
    printf("  Each ll node will compute %d fibonacci numbers beginning with %d\n", N, FS);      

    p = init_list(p);
    head = p;
    start = omp_get_wtime();

    {  
        #pragma omp parallel
        {
            #pragma omp single
            while (p != NULL) {
                {
                    #pragma omp task firstprivate(p)
                    processwork(p);
                }
                p = p->next;
            }
        }
    }
    end = omp_get_wtime();

    // Oslobadjanje memorije zauzete za listu.
    p = head;
    while (p != NULL) {
        printf("%d : %d\n", p->data, p->fibdata);
        temp = p->next;
        free(p);
        p = temp;
    }  
    free(p);

    printf("Compute Time: %f seconds\n", end - start);
    return 0;
}
```
linkedlist.c - rešenje 
{:.figure}
---
layout: page
title: Z2-openMP
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

### Matrix Transpose

#### ReadMe

##### Kompajliranje
Zadatak je moguće kompajlirati:

- direktno iz komandne linije ili
- korišćenjem cmake alata

U prvom slučaju, dodatne opcije kompajliranja je potrebno dodati u formatu ``-opcija``. U drugom slučaju je potrebno
dodati opciju u liniju ``set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")`` u ``CMakeLists.txt`` datoteci.

###### Kompajliranje iz terminala
Ukoliko želite da koristite izgenerisane ulazne podatke u ``hdf5`` formatu neophodno je imati instaliranu podršku za ovaj
format podataka. Na Ubuntu operativnim sistemina, hdf5 paket možete instalirati pokretanjem sledećih komandi:
```sh
sudo apt install libhdf5-dev 
```
Zatim se pozicinonirati u korenski direktorijum zadatka i pokrenuti:
```sh
h5cc utils/*.h utils/*.c main.c -fopenmp
```
Ukoliko ne želite da koristite ulazne podatke u hdf5 formatu, zadatak možetekompajlirati na sledeći način:
```sh
gcc main.c -fopenmp -DDISABLE_HDF5
```
Ukoliko isključite podršku za učitavanje generisanih ulaznih podataka, potrebno je da 
modifikujete izvorni kod tako da na neki drugi način obezbedite učitavanje ulaznih podataka.

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
Pozicionirati se u direktorijum u kojem se nalazi izvršna datoteka i pokrenuti ``./a.out``, ili drugi naziv ukoliko 
je drugačije specificirano tokom kompajliranja.

#### main.c

```c
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#ifndef DISABLE_HDF5
#include "utils/h5_matrix_utils.h"
#endif

/**
 * Sekvencijalni program za transponovanje matrice.
 *
 * @param matrix    Pokazivac na blok memorije koji sadrzi matricu. Elementi matrice su tipa float.
 * @param rows      Broj vrsta ulazne matrice.
 * @param cols      Broj kolona ulazne matrice.
 * @return          Pokazivac na blok memorije u kojem se nalazi transponovana matrica. Pozivalac programa
 *                  je duzan da prihvati vrednost ovog pokazivaca i oslobodi zauzetu memoriju kada mu
 *                  transponovana matrica vise ne treba.
 */
float *transpose(float *matrix, unsigned long long rows, unsigned long long cols) {
    
    float *tmatrix = (float *) malloc(cols * rows * sizeof(float));
    
    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            tmatrix[i * rows + j] = matrix[j * rows + i];
        }
    }
    return tmatrix;
}

int main(int argc, char *argv[]) {
    
    if (argc != 2) {
        fprintf(stdout, "Program pozvan sa neispravnim brojem argumenata.\nPrimer poziva: ./transponovanje m3x3.h5");
        exit(1);
    }
    
    double start = omp_get_wtime();
    
    const char *input_file = argv[1];
    unsigned long long rows, cols;
    
    float *matrix = NULL, *tmatrix = NULL;
#ifndef DISABLE_HDF5
    matrix = h5_load_matrix(input_file, &rows, &cols);
#else
    printf("HDF5 podrska onemogucena!");
#endif
    
    
    printf("\n===================================\n");
    printf("===== Netransponovana matrica =====\n");
    printf("===================================\n");
    assert(matrix != NULL);
    //print_float_matrix(matrix, rows, cols);   // otkomentarisati za ispis netransponovane matrice
    
    printf("\n===================================\n");
    printf("====== Transponovana matrica ======\n");
    printf("===================================\n");
    tmatrix = transpose(matrix, rows, cols);
    assert(tmatrix != NULL);
    //print_float_matrix(tmatrix, rows, cols);  // otkomentarisati za ispis transponovane matrice
    
    free(matrix);   // dealociraj originalnu matricu
    free(tmatrix);  // dealociraj transponovanu matricu
    
    printf("\nVreme izvrsavanja: %lf\n", omp_get_wtime() - start);
    
    return 0;
}
```
main.c - zadatak 
{:.figure}

#### CMakeLists.txt

```sh
cmake_minimum_required(VERSION 3.5)
project(TransposeMatrix)

find_package(HDF5)
find_package(OpenMP)

# additional options
option(ENABLE_HDF5 "Enable HDF5 support." ON)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
set(SOURCE_FILES main.c)

add_executable(TransposeMatrix ${SOURCE_FILES})

if(ENABLE_HDF5)
    if(HDF5_FOUND)
        include_directories(${HDF5_INCLUDE_DIR})
        target_link_libraries(TransposeMatrix ${HDF5_C_LIBRARIES})
        set(HDF5_SOURCE_FILES utils/h5defs.h utils/h5_matrix_utils.c utils/h5_matrix_utils.h)
        target_sources(TransposeMatrix PUBLIC ${HDF5_SOURCE_FILES})
    else()
        message(FATAL_ERROR "HDF5 support has been requested, but no HDF5 library was found!")
    endif()
else()
    add_definitions(-DDISABLE_HDF5)
    message(STATUS "HDF5 support disabled.")
endif()
```
CMakeLists.txt - zadatak 
{:.figure}

#### utils

##### h5defs.h

```c
#ifndef MATRIXUTILITIES_H5DEFS_H
#define MATRIXUTILITIES_H5DEFS_H

#include <stdlib.h>
#include <hdf5.h>

// Checks for error during hdf5 library function call (nonzero return value).
#define H5STATUS(e) \
    (if (e < 0) { printf("\nHDF5 error on line %d\n\n", __LINE__ ); exit 1; })

#endif //MATRIXUTILITIES_H5DEFS_H
```
h5defs.h - zadatak 
{:.figure}

##### h5_matrix_utils.h

```c
#ifndef MATRIXUTILITIES_H5_MATRIX_UTILS_H
#define MATRIXUTILITIES_H5_MATRIX_UTILS_H

#include <hdf5.h>
#include "h5defs.h"

/* Move this to a separate file */
float *generate_float_matrix(unsigned long long rows, unsigned long long cols);
double *generate_double_matrix(unsigned int rows, unsigned int cols);               // TODO implement
int *generate_int_matrix(unsigned int rows, unsigned int cols);                     // TODO implement
void print_float_matrix(float *matrix, unsigned long long rows, unsigned long long cols);
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

```
h5_matrix_utils.h - zadatak 
{:.figure}

##### h5_matrix_utils.c

```c
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

```
h5_matrix_utils.h - zadatak 
{:.figure}

### Genetic Algorithm

#### ReadMe

##### Kompajliranje

Zadatak je moguće kompajlirati:

- direktno iz komandne linije ili
- korišćenjem cmake alata

U prvom slučaju, dodatne opcije kompajliranja je potrebno dodati u formatu ``-opcija``. U drugom slučaju je potrebno
dodati opciju u liniju ``set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")`` u ``CMakeLists.txt`` datoteci.

###### Kompajliranje iz terminala
Pozicionirati se u korenski direktorijum:
```sh
gcc main.c -fopenmp
```
Moguće je još proslediti i opcije ``-DLARGE`` (kompleksan primer), ``-DMEDIUM`` (srednje kompleksan primer) i ``-DSMALL``
(jednostavan primer). Ukoliko se ne specificira ni jedna od navedenih opcija, program će biti pokrenut nad jednostavnim
primerom. 

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

##### Pokretanje programa
Pozicionirati se u direktorijum u kojem se nalazi izvršna datoteka i pokrenuti ``./a.out``, ili drugi naziv ukoliko 
je drugačije specificirano tokom kompajliranja.

#### main.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <time.h>
#include <string.h>

#ifdef LARGE
    #define TARGET "SUSE and the University of Delaware have joined the OpenMP ARB, a group of leading hardware and software vendors and research organizations creating the standard for the most popular shared-memory parallel programming model in use today."
    #define NCHROMOSOMES 237+1
    #define NINDIVIDUALS 2000
#elif MEDIUM
    #define TARGET "Parallel programming is funny!"
    #define NCHROMOSOMES 30+1
    #define NINDIVIDUALS 1000
#else
    #define TARGET "~OpenMP~"
    #define NCHROMOSOMES 8+1
    #define NINDIVIDUALS 1000
#endif

#define NITERATIONS 1000
#define SELECTION_PERCENT 70
#define MUTATION_PERCENT 5

/**
 * Jedna jedinka u populaciji. Jedinka ima svoj identifikator koji se koristi samo pri
 * ispisu, hromozome koji su predstavljeni stringom i meru adaptacije - fitnes. Sto je
 * fitnes veci, to je jedinka manje adaptirana.
 */
struct Individual {
    int id;
    char chromosomes[NCHROMOSOMES];
    float fitness;
};
typedef struct Individual individual_t;

/**
 * Populaciju cini niz jedinki. Na nivou populacije se cuva fitnes kako bi se lakse
 * pratilo da li populacija evaluira ka resenju problema.
 */
static individual_t *population;
static unsigned long int total_fitness;

/** Funkcije za rad sa populacijom. */

/**
 * Inicijalizuje populaciju stvaranjem NINDIVIDUALS jedinki.
 * Hromozomi svake jedinke se nasumicno biraju medju vidljivim ascii
 * karakterima (od koda 32 do koda 126). Po zavrsetku ove funkcije
 * fitnes svake od jedinki ce biti 0.
 */
void initialize();

/**
 * Racuna fitnes za svaku od jedinki iz populacije. Vrednost fitnesa
 * odgovara broju korespodentnih karaktera koji se razlikuju u TARGET
 * stringu i hromozomu jedinke. Ukoliko nema razlike izmedju ova dva
 * stringa, fitnes jedinke ce biti 0.
 *
 * Svaki put kada se pozove ova metoda, staticka
 * promenljiva total_fitnes se postavi na vrednost 0, a zatim se u nju
 * akumulira sracunata vrednost fitnesa svake jedinke iz populacije.
 */
void calculate_fitness();

/**
 * Sortiranje populacije jedinki u rastucem redosledu prema fitnesu.
 * Za sortiranje se koristi bubble sort algoritam.
 */
void sort();

/**
 * Stvaranje nove populacije selektovanjem i ukrstanjem roditelja izabranih
 * iz postojece populacije.
 *
 * NINDIVIDUALS puta se biraju po dva roditelja iz prvih SELECTION_PERCENT
 * procenata postojece generacije. Zatim se formira jedinka potomak tako sto
 * se za svaki od njenih hromozoma nasumicno bira jedan od korespodentnih
 * hromozoma prvog ili drugog roditelja. Kada se odrede hromozomi nove jedinke,
 * funkcija sracuna i vrednost fitnesa za tu jedinku.
 *
 * Nakon sto se napravi citava nova populacija, pretodna populacija se brise, a
 * u narednoj iteraciji se iz nove populacije biraju roditelji za dalje ukrstanje.
 */
void crossover_select();

/**
 * Mutira nasumicno odabran hromozom nasumicno odabrane jedinke iz populacije.
 * Sa MUTATION_PERCENT je odredjen ukupan procenat jedinki koje ce biti mutirane.
 */
void mutate();

// helper functions

/**
 * Ispis jedne jedinke iz populacije.
 *
 * @param i     Pokazivac na jedinku cije podatke treba ispisati.
 */
void print_individual(individual_t *i);

/**
 * Ispis svih jedinki populacije.
 */
void print_population();

/**
 * Funkcija omotac koja poziva prosledjenu funkciju pri cemu meri vreme njenog
 * izvrsavanja i izmereno vreme dodaje na prosledjenu adresu.
 *
 * @param f     Funkcija koju treba izvrsiti.
 * @param time  Pokazivac na vrednost koja se uvecava izmerenim vremenom izvrsavanja
 *              funkcije f.
 */
void timer(void (*f)(void), double *time);

/* Promenljive za merenje vremena izvrsavanja razlicitih funkcija. */
static double init_time = 0;
static double fitness_time = 0;
static double sort_time = 0;
static double crossselect_time = 0;
static double mutation_time = 0;

int main() {
    srand(time(NULL));
    
    double start = omp_get_wtime();
    
    // alokacija prostora za inicijalnu populaciju
    population = (individual_t *) calloc(NINDIVIDUALS, sizeof(individual_t));
    
    // inicijalizacija populacije
    timer( initialize, &init_time);
    
    // racunanje fitnesa za svaku jedinku
    timer( calculate_fitness, &fitness_time);
    
    // sortiranje
    timer( sort, &sort_time);
    
    int niterations = NITERATIONS;
    while (niterations--) {
        printf("\n===== ITERACIJA %d =====\nNajbolja jedinka: ", niterations);
        print_individual(&population[0]);
        printf("Fitnes populacije: %ld\n", total_fitness);
        
        // selekcija i ukrstanje
        timer( crossover_select, &crossselect_time );
    
        // mutacija
        timer( mutate, &mutation_time);
    
        // sortiranje
        timer( sort, &sort_time);
        
        // Ukoliko su hromozomi najbolje jedinke iz populacije jednaki ciljnom stringu, algoritam
        // se zavrsava
        if (memcmp(population[0].chromosomes, TARGET, NCHROMOSOMES * sizeof(char)) == 0)
            break;
    }
    
    double total_time = omp_get_wtime() - start;
    
    printf("\n===== Statistika izvrsavanja =====\n");
    printf("- Najbolja jedinka: ");
    print_individual(&population[0]);
    printf("- Ukupno vreme izvrsavanja:   %lf\n", total_time);
    printf("- Inicijalizacija populacije: %lf%%\n", (init_time / total_time) * 100);
    printf("- Racunanje fitnesa:          %lf%%\n", (fitness_time / total_time) * 100);
    printf("- Sortiranje populacije:      %lf%%\n", (sort_time / total_time) * 100);
    printf("- Inicijalizacija populacije: %lf%%\n", (init_time / total_time) * 100);
    printf("- Selekcija i ukrstanje:      %lf%%\n", (crossselect_time / total_time) * 100);
    printf("- Mutacija:                   %lf%%\n", (mutation_time / total_time) * 100);
    
    /* Unistavanje populacije */
    free(population);
    
    return 0;
}

void initialize() {
    total_fitness = 0;
    for (int i = 0; i < NINDIVIDUALS; i++) {
        for (int j = 0; j < NCHROMOSOMES-1; j++) {
            population[i].id = i;
            population[i].chromosomes[j] = (char) (32 + rand() % 95);
        }
    }
}

int calculate_fitness_individual(individual_t *i) {
    int difference = 0;
    for (int j = 0; j < NCHROMOSOMES - 1; j++) {
        // sto se vise karaktera razlikuje u ciljnom i trenutnom hromozomu, to je veca vrednost razlike
        if (TARGET[j] != i->chromosomes[j]) difference++;
    }
    total_fitness += difference;
    return difference;
}

void calculate_fitness() {
    total_fitness = 0;
    for (int i = 0; i < NINDIVIDUALS; i++) {
        population[i].fitness = calculate_fitness_individual(&population[i]);
    }
}

void sort() {
    int i, j;
    individual_t tmp, *i1, *i2;
    
    for (i = 0; i < NINDIVIDUALS - 1; i++)
        for (j = 0; j < NINDIVIDUALS - i - 1; j++) {
            i1 = &population[j];
            i2 = &population[j + 1];
            if (i1->fitness > i2->fitness) {
                tmp = *i2;
                *i2 = *i1;
                *i1 = tmp;
            }
        }
}

void crossover_select() {
    
    /* Prostor za novu generaciju */
    individual_t *new_population = (individual_t *) calloc(NINDIVIDUALS, sizeof(individual_t));
    total_fitness = 0;
    
    individual_t *i1, *i2;          // pokazivaci na roditelje nove jedinke
    individual_t *new_individual;   // pokazivac na novu jedinku
    int crossidx = 0;               // redni broj gena na kojem se vrsi promena
    int lb = (int) (NINDIVIDUALS * (SELECTION_PERCENT / 100.0));    // top 70% za ukrstanje
    
    for (int i = 0; i < NINDIVIDUALS; i++) {
        new_individual = &new_population[i];
        
        /* Izaberi dve jedinke */
        i1 = &population[rand() % lb];
        i2 = &population[rand() % lb];
        
        /* Ukrsti ih i napravi novu jedinku. */
        for (int j = 0; j < NCHROMOSOMES - 1; j++) {
            if (rand() % 2 == 0) {
                new_individual->chromosomes[j] = i1->chromosomes[j];
            } else {
                new_individual->chromosomes[j] = i2->chromosomes[j];
            }
        }
        new_individual->id = i;
        new_individual->fitness = calculate_fitness_individual(new_individual);
    }
    
    /* Stara populacija se menja novom */
    free(population);
    population = new_population;
}

void mutate() {
    int nindividuals = (int) (NINDIVIDUALS * (MUTATION_PERCENT / 100.0));
    while (nindividuals--) {
        int idx = rand() % NCHROMOSOMES;
        char value = (char) (32 + rand() % 94);
        //printf("%d %d %c\n", rand() % NINDIVIDUALS, idx, value);
        population[rand() % NINDIVIDUALS].chromosomes[idx] = value;
    }
}

void print_individual(individual_t *i) {
    printf("id: %d, hromozomi: %s, fitnes: %f\n", i->id, i->chromosomes, i->fitness);
}

void print_population() {
    for (int i = 0; i < NINDIVIDUALS; i++) {
        print_individual(&population[i]);
    }
}

void timer(void (*f)(void), double *time) {
    double start = omp_get_wtime();
    (*f)();
    double stop = omp_get_wtime();
    *time += (stop - start);
}

```
main.c - zadatak 
{:.figure}

#### CMakeLists.txt

```sh
cmake_minimum_required(VERSION 3.5)
project(GeneticAlgorithm)

find_package(OpenMP)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
set(SOURCE_FILES main.c)

add_executable(GeneticAlgorithm ${SOURCE_FILES})

```
CMakeLists.txt - zadatak 
{:.figure}

### Bisection

#### ReadMe

##### Kompajliranje
Zadatak je moguće kompajlirati:

- direktno iz komandne linije ili
- korišćenjem cmake alata

U prvom slučaju, dodatne opcije kompajliranja je potrebno dodati u formatu ``-opcija``. U drugom slučaju je potrebno
dodati opciju u liniju ``set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")`` u ``CMakeLists.txt`` datoteci.

###### Kompajliranje iz terminala
Pozicionirati se u korenski direktorijum:
```sh
gcc main.c -fopenmp -lm
```
Dodatne opcije kompajliranja:

- ``-DFX``   - kompajlirati program tako da evaluira funkciju x-1 nad intervalom [-5, 5] (jedan koren).
- ``-DFPOW`` - kompajlirati program tako da evaluira funkciju pow(x, 2) - 2 nad intervalom [15, 19] (nema korena).
- ``-DFSIN`` - - kompajlirati program tako da evaluira funkciju sin(x) nad intervalom [-4, 10] (jedan koren).

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

##### Pokretanje programa
Pozicionirati se u direktorijum u kojem se nalazi izvršna datoteka i pokrenuti ``./a.out``, ili drugi naziv ukoliko 
je drugačije specificirano tokom kompajliranja.

#### main.c

```c
#include <stdio.h>
#include <math.h>
#include <omp.h>

#define MAX_ITERS 1000
#define TOLERANCE 0.0000000001
#define STEP 1

#ifdef FX
    static double lower_bound = -5.f;
    static double upper_bound = 5.f;
#elif FPOW
    static double lower_bound = 15.f;
    static double upper_bound = 19.f;
#else
    static double lower_bound = -4.f;
    static double upper_bound = 10.f;
#endif

/**
 * Funkcija za koju treba pronaci korene.
 *
 * @param x - Vrednost nezavisne promenljive x.
 * @return Vrednost funkcije za zadatu vrednost promenljive x.
 */
double f(double x) {
#ifdef FX   // jedan koren nad intervalom
    return x - 1;
#elif FPOW  // nema korena nad intervalom
    return pow(x, 2) - 2;
#else //FSIN  // vise korena nad intervalom
    return sin(x);
#endif
}

/**
 * Funkcija koja metodom bisekcije racuna koren zadate funkcije. Pretpostavka je da je funkcija
 * nad zadatim intervalom monotona, odnosno da nema prevoja, jer metoda vraca samo prvi koren
 * funkcije koji pronadje.
 *
 * @param f         Funkcija ciji se koren trazi.
 * @param a         Pocetak intervala nad kojim se trazi koren funkcije. Podrazumeva se da vazi a < b.
 * @param b         Kraj intervala nad kojim se trazi koren funkcije. Podrazumeva se da vazi b > a.
 * @param xroot     Pokazivac na promenljivu u kojoj ce se nalaziti koren funkcije. Ukoliko funkcija
 *                  nad zadatim intervalom nema korena, vrednost ove promenljive je nepoznata.
 * @param maxiters  Maksimalan broj bisekcija koji ce biti izvrsen pre nego se odustane od trazenja
 *                  korena nad zadatim intervalom.
 * @param tol       Preciznost do na koju se trazi resenje. Veca preciznost dovodi do preciznijeg resenja,
 *                  ali povecava broj iteracija.
 */
double bisection(double (*f)(double), double a, double b, double *xroot, int maxiters, double tol) {
    
    double xp, fxp;  // pocetna tacka intervala u kom se trazi koren, vrednost funkcije u tacki
    double xk, fxk;  // krajnja tacka intervala u kom se trazi koren, vrednost funkcije u tacki
    double xmid;     // sredisnja tacka intervala u kom se trazi koren (xp - xk) / 2
    double fxmid;    // f(xmid)
    double dx;       // duzina intervala
    
    if (f(a) * f(b) > 0) return -1;     // nema korena u zadatom intervalu
    xp = a; xk = b;
    for (int i = 0; i < maxiters; i++) {
        dx = fabs(xk - xp) / 2;
        xmid = xp + dx;
        fxmid = f(xmid);
    
        if (fxmid == 0 || dx < tol) {
            *xroot = xmid;
            return 0;
        }
        
        if (f(xp) * fxmid < 0) {        // koren u podintervalu [xp, xmid]
            xk = xmid;
        } else if (f(xk) * fxmid < 0) { // koren u podintervalu [xmid, xk]
            xp = xmid;
        }
        
        //printf("--- Iteracija %d, xp = %lf, xk = %lf, xmid=%lf\n", i, xp, xk, xmid);
    }
    
    return 0;
}

/**
 * Funkcija za pronalazenje vise korena zadate funkcije f nad intervalom [a, b].
 *
 * Funkcija deli zadati interval na podintervale ne vece od zadatog koraka (videti step parametar).
 * Nad svakim dobijenim podintervalom [xp, xk] se metodom bisekcije pronalazi koren funkcije.
 * Ukoliko nad podintervalom [xp, xk] postoji vise korena funkcije, funkcija bisection ce vratiti
 * samo jedan. U slucaju da trenutna vrednost parametra sa trenutnom vrednoscu parametra step
 * ne mogu biti pronadjeni svi koreni funkcije, potrebno je smanjiti vrednost ovog parametra i
 * pokusati opet.
 *
 * @param f         Funkcija za koju se traze svi koreni nad intervalom [a, b].
 * @param a         Pocetak intervala nad kojim se traze koreni funkcije. Podrazumeva se da vazi a < b.
 * @param b         Kraj intervala nad kojim se traze koreni funkcije. Podrazumeva se da vazi b > a.
 * @param xroot     Pokazivac na promenljivu u kojoj ce se nalaziti koren funkcije. Ukoliko funkcija
 *                  nad zadatim intervalom nema korena, vrednost ove promenljive je nepoznata.
 * @param maxiters  Maksimalan broj bisekcija koji ce biti izvrsen pre nego se odustane od trazenja
 *                  korena nad zadatim intervalom.
 * @param tol       Preciznost do na koju se trazi resenje. Veca preciznost dovodi do preciznijeg resenja,
 *                  ali povecava broj iteracija.
 * @param step      Velicina podintervala [xp, xk] intervala [a, b] nad kojim ce biti trazeni koreni.
 */
void find_roots(double (*f)(double), double a, double b, double *xroot, int maxiters, double tol, double step) {
    double xp = a, xk = b;
    double dx = fabs(xk - xp) / 2;
    double xroot1, xroot2;
    
    if (fabs(xk - xp) < step) {
        if (bisection(f, xp, xk, xroot, maxiters, tol)) {
            printf("Interval [%lf, %lf]: Nema korena.\n", xp, xk);
        } else {
            printf("Interval [%lf, %lf]: Ima koren u %lf.\n", xp, xk, *xroot);
        }
    } else {
        find_roots(f, xp, xp + dx, &xroot1, maxiters, tol, step);
        find_roots(f, xp + dx, xk, &xroot2, maxiters, tol, step);
    }
}

int main() {
    
    double start = omp_get_wtime();
    
    double xroot, lb = lower_bound, ub = upper_bound;
    find_roots(f, lb, ub, &xroot, MAX_ITERS, TOLERANCE, STEP);

    double end = omp_get_wtime();
    printf("Ukupno trajanje: %lf\n", end - start);
    
    return 0;
}

```
main.c - zadatak
{:.figure}

#### CMakeLists.txt

```sh
cmake_minimum_required(VERSION 3.5)
project(BisectionMethod)

find_package(OpenMP)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS} -lm")
set(SOURCE_FILES main.c)

add_executable(BisectionMethod ${SOURCE_FILES})
target_link_libraries(BisectionMethod -lm)

```
CMakeLists.txt - zadatak
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
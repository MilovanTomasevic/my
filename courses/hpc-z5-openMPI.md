---
layout: page
title: Z5-openMPI
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
// Hello World iz hibridnog OpenMPI + OpenMP programa.

#include <stdio.h>
#include <mpi.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    #pragma omp parallel
    {
        printf("Hello World iz procesa %d i niti %d.\n", rank, omp_get_thread_num());
    }

    MPI_Finalize();

    return 0;
}
~~~
hello_world.c
{:.figure}

## Zadaci 

### MatrixMultiplicationHybrid

#### ReadMe

##### Kompajliranje
Zadatak je moguće kompajlirati:

- direktno iz komandne linije ili
- korišćenjem cmake alata

U prvom slučaju, dodatne opcije kompajliranja je potrebno dodati u formatu ``-opcija``. U drugom slučaju kompajlerske opcije
se dodaju u promenljivu ``CMAKE_C_FLAGS``, a linkerske u ``CMAKE_EXE_LINKER_FLAGS``
 u datoteci ``CMakeLists.txt`` .

###### Kompajliranje iz terminala
Ukoliko želite da koristite izgenerisane ulazne podatke u ``hdf5`` formatu neophodno je imati instaliranu podršku za ovaj
format podataka. Na Ubuntu operativnim sistemina, hdf5 paket možete instalirati pokretanjem sledećih komandi:
```sh
sudo apt install libhdf5-dev 
```
Zatim se pozicinonirati u korenski direktorijum zadatka i pokrenuti:
```sh
h5cc utils/*.h utils/*.c main.c $(mpicc --showme:compile) $(mpicc --showme:link) -fopenmp
```
Ukoliko ne želite da koristite ulazne podatke u hdf5 formatu, zadatak možetekompajlirati na sledeći način:
```sh
mpicc main.c -DDISABLE_HDF5 -fopenmp
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
Pozicionirati se u direktorijum u kojem se nalazi izvršna datoteka i pokrenuti 
``OMP_NUM_THREADS=<Nomp> mpiexec -np <Nmpi> ./a.out``, ili drugi 
naziv ukoliko je drugačije specificirano tokom kompajliranja. ``<Nmpi>`` zameniti konkretnim brojem koji predstavlja broj 
MPI procesa. ``<Nomp>`` zameniti konkretnim brojem koji predstavlja broj niti po
procesu.


#### main.c

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <mpi.h>
#include <omp.h>

#ifndef DISABLE_HDF5
#include "utils/h5_matrix_utils.h"
#endif

#define M1FILENAME "../input_data/m3x3.h5"   // modifikovati putanju po potrebi
#define M2FILENAME "../input_data/m3x3.h5"   // modifikovati putanju po potrebi

void matrix_multiply_openmp(float *matrix1, float *matrix2, float *result) {
    // TODO implementirati OpenMP varijantu mnozenja matrica
}

void matrix_multiply_mpi(int *argc, char ***argv, float *matrix1,
                         float *matrix2, float *result) {
    // TODO implementirati OpenMPI varijantu mnozenja matrica
}

void matrix_multiply_hybrid(int *argc, char ***argv, float *matrix1,
                            float *matrix2, float *result) {
    // TODO Implementirati hibridnu OpenMP-OpenMPI varijantnu mnozenja matrica
}

int main(int argc, char *argv[]) {
    
    float *matrix1 = NULL, *matrix2 = NULL, *result = NULL;
    unsigned long long rows, cols;
    
#ifndef DISABLE_HDF5
    matrix1 = h5_load_matrix(M1FILENAME, &rows, &cols);
    assert(matrix1 != NULL);
#else
    printf("HDF podrska onemogucena!\n");
#endif

#ifndef DISABLE_HDF5
    matrix2 = h5_load_matrix(M2FILENAME, &rows, &cols);
    assert(matrix2 != NULL);
#else
    printf("HDF podrska onemogucena!\n");
#endif
    
    /**************************************************************************/
    /******************************** NAPOMENE ********************************/
    /**************************************************************************/
    /*
     Dat je primer cuvanja matrice u hdf5 formatu (upotrebiti za cuvanje rezultata)
     Pri odbrani ce biti koriscen alat h5diff za poredjenje rezultata
     prethodno generisane sekvencijalne verzije mnozenja matrica i rezultata
     dobijenog iz hibridnog resenja (manje rezlike u rezultatima na odredjenim
     decimalama su moguce usled aritmetike razlomljenih brojeva i nece se
     tretirati kao greska.
     
     Izgenerisati rezultate za sve date ulazne matrice (od 3x3 do 10240x10240)
     i smestiti ih u isti direktorijum direktorijum. Zadrzati konvenciju
     davanja imena datotekama rezultata.*/
    /*************************************************************************/
    matrix_multiply_hybrid(&argc, &argv, matrix1, matrix2, result);
    assert(result != NULL);
    
    char filename[15];
    sprintf(filename, "result%dx%d", rows, cols); // Pretpostavka je da ime datoteke nikada
                                                  // nece biti duze od 14 karaktera. Po potrebi promeniti.
    h5_save_float_matrix(filename, matrix1, rows, cols);
    
    if (matrix1 != NULL) free(matrix1);
    if (matrix2 != NULL) free(matrix2);
    if (result  != NULL) free(result);
    
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
find_package(OpenMP REQUIRED)
find_package(HDF5)

# additional options
option(ENABLE_HDF5 "Enable HDF5 support." ON)

set(CMAKE_C_STANDARD 11)
set(SOURCE_FILES main.c)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${MPI_C_COMPILE_FLAGS} ${OpenMP_C_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${MPI_C_LINK_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")

add_executable(MatrixMultiplication ${SOURCE_FILES})
include_directories(${MPI_C_INCLUDE_PATH})
target_link_libraries(MatrixMultiplication ${MPI_C_LIBRARIES})

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
void h5_generate_matrix(const char *filename, unsigned int rows, unsigned int cols);

/**
 * Creates hdf5 file containing the data of rows x cols dimension.
 * @param filename If file should be saved to the working directory then just filename
 * otherwise absolute or relative path to the file.
 * @param data Pointer to the matrix data to be saved. If memory less then
 * rows x columns is allocated, function might exit ungracefully.
 * @param rows Input matrix row number.
 * @param cols Input matrix column number.
 */
void h5_save_float_matrix(const char *filename, float *data, unsigned int rows, unsigned int cols);

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


void h5_generate_matrix(const char *filename, unsigned int rows, unsigned int cols) {
    float *data = generate_float_matrix(rows, cols);
    h5_save_float_matrix(filename, data, rows, cols);
    free(data);
}

void h5_save_float_matrix(const char *filename, float *data, unsigned int rows, unsigned int cols) {
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
    H5CHECK( H5Dwrite(dataset_id, H5T_NATIVE_FLOAT, H5S_ALL, H5S_ALL, H5P_DEFAULT, data) );
    
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
            printf("%f ", matrix[i * cols + j]);
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

- [m3x3.h5](../high-performance-computing/v5/input_data/m3x3.h5){:target="_blank"} 
- [m5x5.h5](../high-performance-computing/v5/input_data/m5x5.h5){:target="_blank"} <br>
- [statistika.csv](../high-performance-computing/v5/statistika.csv){:target="_blank"}



~~~c
// Hello World iz hibridnog OpenMPI + OpenMP programa.

#include <stdio.h>
#include <mpi.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    #pragma omp parallel
    {
        printf("Hello World iz procesa %d i niti %d.\n", rank, omp_get_thread_num());
    }

    MPI_Finalize();

    return 0;
}
~~~
hello_world.c
{:.figure}

## Rešenja 

### pi_openmp.c

~~~c
/**
 * Program koji racuna vrednost integrala funkcije 4/(1+x^2). Numericki,
 * ova vrednost je jednaka broju pi.
 *
 * Originalni materijal za ovaj primer je preuzet iz niza prezentacija
 * "Introduction to OpenMP" ciji je autor Tim Mattson
 */

#include <stdio.h>
#include <omp.h>

static long num_steps = 100000000;
double step;

int main() {

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

    return 0;
}
~~~
pi_openmp.c
{:.figure}

### pi_sekvencijalni.c

~~~c
/**
 * Program koji racuna vrednost integrala funkcije 4/(1+x^2). Numericki,
 * ova vrednost je jednaka broju pi.
 *
 * Originalni materijal za ovaj primer je preuzet iz niza prezentacija
 * "Introduction to OpenMP" ciji je autor Tim Mattson
 */

#include <stdio.h>
#include <omp.h>

static long num_steps = 100000000;

double step;

int main() {

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

    return 0;
}
~~~
pi_sekvencijalni.c
{:.figure}
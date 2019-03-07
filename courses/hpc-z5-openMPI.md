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

## Predavanja 

### nbody_basic.c

~~~c
/* File:     nbody_basic.c
 * Purpose:  Implement a 2-dimensional n-body solver that uses the 
 *           straightforward n^2 algorithm.  This version directly
 *           computes all the forces.
 *
 * Compile:  gcc -g -Wall -o nbody_basic nbody_basic.c -lm
 *           If COMPUTE_ENERGY is defined, the program will print 
 *              total potential energy, total kinetic energy and total
 *              energy of the system at each time step.
 *           To turn off output except for timing results, define NO_OUTPUT
 *           To get verbose output, define DEBUG
 *           Needs timer.h
 * Run:      ./nbody_basic <number of particles> <number of timesteps>  
 *              <size of timestep> <output frequency> <g|i>
 *              'g': generate initial conditions using a random number
 *                   generator
 *              'i': read initial conditions from stdin
 *           A timestep of 0.01 seems to work reasonably well for
 *           the automatically generated data.
 *
 * Input:    If 'g' is specified on the command line, none.  
 *           If 'i', mass, initial position and initial velocity of 
 *              each particle
 * Output:   If the output frequency is k, then position and velocity of 
 *              each particle at every kth timestep
 *
 * Algorithm: Slightly modified version of algorithm in James Demmel, 
 *    "CS 267, Applications of Parallel Computers:  Hierarchical 
 *    Methods for the N-Body Problem",
 *    www.cs.berkeley.edu/~demmel/cs267_Spr09, April 20, 2009.
 *
 *    for each timestep t {
 *       for each particle i
 *          compute f(i), the force on i
 *       for each particle i
 *          update position and velocity of i using F = ma
 *       if (output step) Output new positions and velocities
 *    }
 *
 * Force:    The force on particle i due to particle k is given by
 *
 *    -G m_i m_k (s_i - s_k)/|s_i - s_k|^3
 *
 * Here, m_j is the mass of particle j, s_j is its position vector
 * (at time t), and G is the gravitational constant (see below).  
 *
 * Integration:  We use Euler's method:
 *
 *    v_i(t+1) = v_i(t) + h v'_i(t)
 *    s_i(t+1) = s_i(t) + h v_i(t)
 *
 * Here, v_i(u) is the velocity of the ith particle at time u and
 * s_i(u) is its position.
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "timer.h"

#define DIM 2  /* Two-dimensional system */
#define X 0    /* x-coordinate subscript */
#define Y 1    /* y-coordinate subscript */

const double G = 6.673e-11;  /* Gravitational constant. */
                             /* Units are m^3/(kg*s^2)  */
// const double G = 0.1;  /* Gravitational constant. */
                       /* Units are m^3/(kg*s^2)  */

typedef double vect_t[DIM];  /* Vector type for position, etc. */

struct particle_s {
   double m;  /* Mass     */
   vect_t s;  /* Position */
   vect_t v;  /* Velocity */
};

void Usage(char* prog_name);
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p);
void Get_init_cond(struct particle_s curr[], int n);
void Gen_init_cond(struct particle_s curr[], int n);
void Output_state(double time, struct particle_s curr[], int n);
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n);
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t);
void Compute_energy(struct particle_s curr[], int n, double* kin_en_p,
      double* pot_en_p);

/*--------------------------------------------------------------------*/
int main(int argc, char* argv[]) {
   int n;                      /* Number of particles        */
   int n_steps;                /* Number of timesteps        */
   int step;                   /* Current step               */
   int part;                   /* Current particle           */
   int output_freq;            /* Frequency of output        */
   double delta_t;             /* Size of timestep           */
   double t;                   /* Current Time               */
   struct particle_s* curr;    /* Current state of system    */
   vect_t* forces;             /* Forces on each particle    */
   char g_i;                   /*_G_en or _i_nput init conds */
#  ifdef COMPUTE_ENERGY
   double kinetic_energy, potential_energy;
#  endif
   double start, finish;       /* For timings                */

   Get_args(argc, argv, &n, &n_steps, &delta_t, &output_freq, &g_i);
   curr = malloc(n*sizeof(struct particle_s));
   forces = malloc(n*sizeof(vect_t));
   if (g_i == 'i')
      Get_init_cond(curr, n);
   else
      Gen_init_cond(curr, n);

   GET_TIME(start);
#  ifdef COMPUTE_ENERGY
   Compute_energy(curr, n, &kinetic_energy, &potential_energy);
   printf("   PE = %e, KE = %e, Total Energy = %e\n",
         potential_energy, kinetic_energy, kinetic_energy+potential_energy);
#  endif
#  ifndef NO_OUTPUT
   Output_state(0, curr, n);
#  endif
   for (step = 1; step <= n_steps; step++) {
      t = step*delta_t;
//    memset(forces, 0, n*sizeof(vect_t));
      for (part = 0; part < n; part++)
         Compute_force(part, forces, curr, n);
      for (part = 0; part < n; part++)
         Update_part(part, forces, curr, n, delta_t);
#     ifdef COMPUTE_ENERGY
      Compute_energy(curr, n, &kinetic_energy, &potential_energy);
      printf("   PE = %e, KE = %e, Total Energy = %e\n",
            potential_energy, kinetic_energy, kinetic_energy+potential_energy);
#     endif
#     ifndef NO_OUTPUT
      if (step % output_freq == 0)
         Output_state(t, curr, n);
#     endif
   }
   
   GET_TIME(finish);
   printf("Elapsed time = %e seconds\n", finish-start);

   free(curr);
   free(forces);
   return 0;
}  /* main */

/*---------------------------------------------------------------------
 * Function: Usage
 * Purpose:  Print instructions for command-line and exit
 * In arg:   
 *    prog_name:  the name of the program as typed on the command-line
 */
void Usage(char* prog_name) {
   fprintf(stderr, "usage: %s <number of particles> <number of timesteps>\n",
         prog_name);
   fprintf(stderr, "   <size of timestep> <output frequency>\n");
   fprintf(stderr, "   <g|i>\n");
   fprintf(stderr, "   'g': program should generate init conds\n");
   fprintf(stderr, "   'i': program should get init conds from stdin\n");
    
   exit(0);
}  /* Usage */

/*---------------------------------------------------------------------
 * Function:  Get_args
 * Purpose:   Get command line args
 * In args:
 *    argc:            number of command line args
 *    argv:            command line args
 * Out args:
 *    n_p:             pointer to n, the number of particles
 *    n_steps_p:       pointer to n_steps, the number of timesteps
 *    delta_t_p:       pointer to delta_t, the size of each timestep
 *    output_freq_p:   pointer to output_freq, which is the number of
 *                     timesteps between steps whose output is printed
 *    g_i_p:           pointer to char which is 'g' if the init conds
 *                     should be generated by the program and 'i' if
 *                     they should be read from stdin
 */
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p) {
   if (argc != 6) Usage(argv[0]);
   *n_p = strtol(argv[1], NULL, 10);
   *n_steps_p = strtol(argv[2], NULL, 10);
   *delta_t_p = strtod(argv[3], NULL);
   *output_freq_p = strtol(argv[4], NULL, 10);
   *g_i_p = argv[5][0];

   if (*n_p <= 0 || *n_steps_p < 0 || *delta_t_p <= 0) Usage(argv[0]);
   if (*g_i_p != 'g' && *g_i_p != 'i') Usage(argv[0]);

#  ifdef DEBUG
   printf("n = %d\n", *n_p);
   printf("n_steps = %d\n", *n_steps_p);
   printf("delta_t = %e\n", *delta_t_p);
   printf("output_freq = %d\n", *output_freq_p);
   printf("g_i = %c\n", *g_i_p);
#  endif
}  /* Get_args */

/*---------------------------------------------------------------------
 * Function:  Get_init_cond
 * Purpose:   Read in initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 */
void Get_init_cond(struct particle_s curr[], int n) {
   int part;

   printf("For each particle, enter (in order):\n");
   printf("   its mass, its x-coord, its y-coord, ");
   printf("its x-velocity, its y-velocity\n");
   for (part = 0; part < n; part++) {
      scanf("%lf", &curr[part].m);
      scanf("%lf", &curr[part].s[X]);
      scanf("%lf", &curr[part].s[Y]);
      scanf("%lf", &curr[part].v[X]);
      scanf("%lf", &curr[part].v[Y]);
   }
}  /* Get_init_cond */

/*---------------------------------------------------------------------
 * Function:  Gen_init_cond
 * Purpose:   Generate initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 *
 * Note:      The initial conditions place all particles at
 *            equal intervals on the nonnegative x-axis with 
 *            identical masses, and identical initial speeds
 *            parallel to the y-axis.  However, some of the
 *            velocities are in the positive y-direction and
 *            some are negative.
 */
void Gen_init_cond(struct particle_s curr[], int n) {
   int part;
   double mass = 5.0e24;
   double gap = 1.0e5;
   double speed = 3.0e4;

   srandom(1);
   for (part = 0; part < n; part++) {
      curr[part].m = mass;
      curr[part].s[X] = part*gap;
      curr[part].s[Y] = 0.0;
      curr[part].v[X] = 0.0;
//    if (random()/((double) RAND_MAX) >= 0.5)
      if (part % 2 == 0)
         curr[part].v[Y] = speed;
      else
         curr[part].v[Y] = -speed;
   }
}  /* Gen_init_cond */

/*---------------------------------------------------------------------
 * Function:  Output_state
 * Purpose:   Print the current state of the system
 * In args:
 *    curr:   array with n elements, curr[i] stores the state (mass,
 *            position and velocity) of the ith particle
 *    n:      number of particles
 */
void Output_state(double time, struct particle_s curr[], int n) {
   int part;
   printf("%.2f\n", time);
   for (part = 0; part < n; part++) {
//    printf("%.3f ", curr[part].m);
      printf("%3d %10.3e ", part, curr[part].s[X]);
      printf("  %10.3e ", curr[part].s[Y]);
      printf("  %10.3e ", curr[part].v[X]);
      printf("  %10.3e\n", curr[part].v[Y]);
   }
   printf("\n");
}  /* Output_state */

/*---------------------------------------------------------------------
 * Function:  Compute_force
 * Purpose:   Compute the total force on particle part.  Exploit
 *            the symmetry (force on particle i due to particle k) 
 *            = -(force on particle k due to particle i) to also
 *            calculate partial forces on other particles.
 * In args:   
 *    part:   the particle on which we're computing the total force
 *    curr:   current state of the system:  curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out arg:
 *    forces: force[i] stores the total force on the ith particle
 *
 * Note: This function uses the force due to gravitation.  So 
 * the force on particle i due to particle k is given by
 *
 *    m_i m_k (s_k - s_i)/|s_k - s_i|^2
 *
 * Here, m_j is the mass of particle j and s_k is its position vector
 * (at time t). 
 */
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n) {
   int k;
   double mg; 
   vect_t f_part_k;
   double len, len_3, fact;

#  ifdef DEBUG
   printf("Current total force on particle %d = (%.3e, %.3e)\n",
         part, forces[part][X], forces[part][Y]);
#  endif
   forces[part][X] = forces[part][Y] = 0.0;
   for (k = 0; k < n; k++) {
      if (k != part) {
      /* Compute force on part due to k */
         f_part_k[X] = curr[part].s[X] - curr[k].s[X];
         f_part_k[Y] = curr[part].s[Y] - curr[k].s[Y];
         len = sqrt(f_part_k[X]*f_part_k[X] + f_part_k[Y]*f_part_k[Y]);
         len_3 = len*len*len;
         mg = -G*curr[part].m*curr[k].m;
         fact = mg/len_3;
         f_part_k[X] *= fact;
         f_part_k[Y] *= fact;
   #     ifdef DEBUG
         printf("Force on particle %d due to particle %d = (%.3e, %.3e)\n",
               part, k, f_part_k[X], f_part_k[Y]);
   #     endif
   
         /* Add force in to total forces */
         forces[part][X] += f_part_k[X];
         forces[part][Y] += f_part_k[Y];
      }
   }
}  /* Compute_force */

/*---------------------------------------------------------------------
 * Function:  Update_part
 * Purpose:   Update the velocity and position for particle part
 * In args:
 *    part:    the particle we're updating
 *    forces:  forces[i] stores the total force on the ith particle
 *    n:       number of particles
 *
 * In/out arg:
 *    curr:    curr[i] stores the mass, position and velocity of the
 *             ith particle
 *
 * Note:  This version uses Euler's method to update both the velocity
 *    and the position.
 */
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t) {
   double fact = delta_t/curr[part].m;

#  ifdef DEBUG
   printf("Before update of %d:\n", part);
   printf("   Position  = (%.3e, %.3e)\n", curr[part].s[X], curr[part].s[Y]);
   printf("   Velocity  = (%.3e, %.3e)\n", curr[part].v[X], curr[part].v[Y]);
   printf("   Net force = (%.3e, %.3e)\n", forces[part][X], forces[part][Y]);
#  endif
   curr[part].s[X] += delta_t * curr[part].v[X];
   curr[part].s[Y] += delta_t * curr[part].v[Y];
   curr[part].v[X] += fact * forces[part][X];
   curr[part].v[Y] += fact * forces[part][Y];
#  ifdef DEBUG
   printf("Position of %d = (%.3e, %.3e), Velocity = (%.3e,%.3e)\n",
         part, curr[part].s[X], curr[part].s[Y],
               curr[part].v[X], curr[part].v[Y]);
#  endif
// curr[part].s[X] += delta_t * curr[part].v[X];
// curr[part].s[Y] += delta_t * curr[part].v[Y];
}  /* Update_part */

/*---------------------------------------------------------------------
 * Function:  Compute_energy
 * Purpose:   Compute the kinetic and potential energy in the system
 * In args:
 *    curr:   current state of the system, curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out args:
 *    kin_en_p: pointer to kinetic energy of system
 *    pot_en_p: pointer to potential energy of system
 */
void Compute_energy(struct particle_s curr[], int n, double* kin_en_p,
      double* pot_en_p) {
   int i, j;
   vect_t diff;
   double pe = 0.0, ke = 0.0;
   double dist, speed_sqr;

   for (i = 0; i < n; i++) {
      speed_sqr = curr[i].v[X]*curr[i].v[X] + curr[i].v[Y]*curr[i].v[Y];
      ke += curr[i].m*speed_sqr;
   }
   ke *= 0.5;

   for (i = 0; i < n-1; i++) {
      for (j = i+1; j < n; j++) {
         diff[X] = curr[i].s[X] - curr[j].s[X];
         diff[Y] = curr[i].s[Y] - curr[j].s[Y];
         dist = sqrt(diff[X]*diff[X] + diff[Y]*diff[Y]);
         pe += -G*curr[i].m*curr[j].m/dist;
      }
   }

   *kin_en_p = ke;
   *pot_en_p = pe;
}  /* Compute_energy */

~~~
nbody_basic.c
{:.figure}

### nbody_red.c

~~~c
/* File:     nbody_red.c
 * Purpose:  Implement a 2-dimensional n-body solver that uses the 
 *           reduced algorithm.  So when the force on particle
 *           q due to particle k (q < k) is computed, the force
 *           on k due to q is also computed
 *
 * Compile:  gcc -g -Wall -o nbody_red nbody_red.c -lm
 *           If COMPUTE_ENERGY is defined, the program will print 
 *              total potential energy, total kinetic energy and total
 *              energy of the system at each time step.
 *           To turn off all output except for timing results, define NO_OUTPUT
 *           To get verbose output, define DEBUG
 *           Needs timer.h
 *
 * Run:      ./nbody_red <number of particles> <number of timesteps>  
 *              <size of timestep> <output frequency> <g|i>
 *              'g': generate initial conditions using a random number
 *                   generator
 *              'i': read initial conditions from stdin
 *           A timestep of 0.01 seems to work reasonably well for
 *           the automatically generated data.
 *
 * Input:    If 'g' is specified on the command line, none.  
 *           If 'i', mass, initial position and initial velocity of 
 *              each particle
 * Output:   If the output frequency is k, then position and velocity of 
 *              each particle at every kth timestep
 *
 * Algorithm: Slightly modified version of algorithm in James Demmel, 
 *    "CS 267, Applications of Parallel Computers:  Hierarchical 
 *    Methods for the N-Body Problem",
 *    www.cs.berkeley.edu/~demmel/cs267_Spr09, April 20, 2009.
 *
 *    for each timestep t {
 *       for each particle i
 *          compute f(i), the force on i
 *       for each particle i
 *          update position and velocity of i using F = ma
 *       if (output step) Output new positions and velocities
 *    }
 *
 * Force:    The force on particle i due to particle k is given by
 *
 *    -G m_i m_k (s_i - s_k)/|s_i - s_k|^3
 *
 * Here, m_j is the mass of particle j, s_j is its position vector
 * (at time t), and G is the gravitational constant (see below).  
 *
 * Note that the force on particle k due to particle i is 
 * -(force on i due to k).  So we can approximately halve the number 
 * of force computations.
 *
 * Integration:  We use Euler's method:
 *
 *    v_i(t+1) = v_i(t) + h v'_i(t)
 *    s_i(t+1) = s_i(t) + h v_i(t)
 *
 * Here, v_i(u) is the velocity of the ith particle at time u and
 * s_i(u) is its position.
 *
 * IPP:  Section 6.1.2 (pp. 273 and ff.)
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "timer.h"

#define DIM 2  /* Two-dimensional system */
#define X 0    /* x-coordinate subscript */
#define Y 1    /* y-coordinate subscript */

const double G = 6.673e-11;  /* Gravitational constant. */
                             /* Units are m^3/(kg*s^2)  */
// const double G = 0.1;  /* Gravitational constant. */
                          /* Units are m^3/(kg*s^2)  */

typedef double vect_t[DIM];  /* Vector type for position, etc. */

struct particle_s {
   double m;  /* Mass     */
   vect_t s;  /* Position */
   vect_t v;  /* Velocity */
};

void Usage(char* prog_name);
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p);
void Get_init_cond(struct particle_s curr[], int n);
void Gen_init_cond(struct particle_s curr[], int n);
void Output_state(double time, struct particle_s curr[], int n);
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n);
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t);
void Compute_energy(struct particle_s curr[], int n, double* kin_en_p,
      double* pot_en_p);

/*--------------------------------------------------------------------*/
int main(int argc, char* argv[]) {
   int n;                      /* Number of particles        */
   int n_steps;                /* Number of timesteps        */
   int step;                   /* Current step               */
   int part;                   /* Current particle           */
   int output_freq;            /* Frequency of output        */
   double delta_t;             /* Size of timestep           */
   double t;                   /* Current Time               */
   struct particle_s* curr;    /* Current state of system    */
   vect_t* forces;             /* Forces on each particle    */
   char g_i;                   /*_G_en or _i_nput init conds */
#  ifdef COMPUTE_ENERGY
   double kinetic_energy, potential_energy;
#  endif
   double start, finish;       /* For timings                */

   Get_args(argc, argv, &n, &n_steps, &delta_t, &output_freq, &g_i);
   curr = malloc(n*sizeof(struct particle_s));
   forces = malloc(n*sizeof(vect_t));
   if (g_i == 'i')
      Get_init_cond(curr, n);
   else
      Gen_init_cond(curr, n);

   GET_TIME(start);
#  ifdef COMPUTE_ENERGY
   Compute_energy(curr, n, &kinetic_energy, &potential_energy);
   printf("   PE = %e, KE = %e, Total Energy = %e\n",
         potential_energy, kinetic_energy, kinetic_energy+potential_energy);
#  endif
#  ifndef NO_OUTPUT
   Output_state(0, curr, n);
#  endif
   for (step = 1; step <= n_steps; step++) {
      t = step*delta_t;
      /* Particle n-1 will have all forces computed after call to
       * Compute_force(n-2, . . .) */
      memset(forces, 0, n*sizeof(vect_t));
      for (part = 0; part < n-1; part++)
         Compute_force(part, forces, curr, n);
      for (part = 0; part < n; part++)
         Update_part(part, forces, curr, n, delta_t);
#     ifdef COMPUTE_ENERGY
      Compute_energy(curr, n, &kinetic_energy, &potential_energy);
      printf("   PE = %e, KE = %e, Total Energy = %e\n",
            potential_energy, kinetic_energy, kinetic_energy+potential_energy);
#     endif
#     ifndef NO_OUTPUT
      if (step % output_freq == 0)
         Output_state(t, curr, n);
#     endif
   }
   
   GET_TIME(finish);
   printf("Elapsed time = %e seconds\n", finish-start);

   free(curr);
   free(forces);
   return 0;
}  /* main */

/*---------------------------------------------------------------------
 * Function: Usage
 * Purpose:  Print instructions for command-line and exit
 * In arg:   
 *    prog_name:  the name of the program as typed on the command-line
 */
void Usage(char* prog_name) {
   fprintf(stderr, "usage: %s <number of particles> <number of timesteps>\n",
         prog_name);
   fprintf(stderr, "   <size of timestep> <output frequency>\n");
   fprintf(stderr, "   <g|i>\n");
   fprintf(stderr, "   'g': program should generate init conds\n");
   fprintf(stderr, "   'i': program should get init conds from stdin\n");
    
   exit(0);
}  /* Usage */

/*---------------------------------------------------------------------
 * Function:  Get_args
 * Purpose:   Get command line args
 * In args:
 *    argc:            number of command line args
 *    argv:            command line args
 * Out args:
 *    n_p:             pointer to n, the number of particles
 *    n_steps_p:       pointer to n_steps, the number of timesteps
 *    delta_t_p:       pointer to delta_t, the size of each timestep
 *    output_freq_p:   pointer to output_freq, which is the number of
 *                     timesteps between steps whose output is printed
 *    g_i_p:           pointer to char which is 'g' if the init conds
 *                     should be generated by the program and 'i' if
 *                     they should be read from stdin
 */
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p) {
   if (argc != 6) Usage(argv[0]);
   *n_p = strtol(argv[1], NULL, 10);
   *n_steps_p = strtol(argv[2], NULL, 10);
   *delta_t_p = strtod(argv[3], NULL);
   *output_freq_p = strtol(argv[4], NULL, 10);
   *g_i_p = argv[5][0];

   if (*n_p <= 0 || *n_steps_p < 0 || *delta_t_p <= 0) Usage(argv[0]);
   if (*g_i_p != 'g' && *g_i_p != 'i') Usage(argv[0]);

#  ifdef DEBUG
   printf("n = %d\n", *n_p);
   printf("n_steps = %d\n", *n_steps_p);
   printf("delta_t = %e\n", *delta_t_p);
   printf("output_freq = %d\n", *output_freq_p);
   printf("g_i = %c\n", *g_i_p);
#  endif
}  /* Get_args */

/*---------------------------------------------------------------------
 * Function:  Get_init_cond
 * Purpose:   Read in initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 */
void Get_init_cond(struct particle_s curr[], int n) {
   int part;

   printf("For each particle, enter (in order):\n");
   printf("   its mass, its x-coord, its y-coord, ");
   printf("its x-velocity, its y-velocity\n");
   for (part = 0; part < n; part++) {
      scanf("%lf", &curr[part].m);
      scanf("%lf", &curr[part].s[X]);
      scanf("%lf", &curr[part].s[Y]);
      scanf("%lf", &curr[part].v[X]);
      scanf("%lf", &curr[part].v[Y]);
   }
}  /* Get_init_cond */

/*---------------------------------------------------------------------
 * Function:  Gen_init_cond
 * Purpose:   Generate initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 *
 * Note:      The initial conditions place all particles at
 *            equal intervals on the nonnegative x-axis with 
 *            identical masses, and identical initial speeds
 *            parallel to the y-axis.  However, some of the
 *            velocities are in the positive y-direction and
 *            some are negative.
 */
void Gen_init_cond(struct particle_s curr[], int n) {
   int part;
   double mass = 5.0e24;
   double gap = 1.0e5;
   double speed = 3.0e4;

   srandom(1);
   for (part = 0; part < n; part++) {
      curr[part].m = mass;
      curr[part].s[X] = part*gap;
      curr[part].s[Y] = 0.0;
      curr[part].v[X] = 0.0;
//    if (random()/((double) RAND_MAX) >= 0.5)
      if (part % 2 == 0)
         curr[part].v[Y] = speed;
      else
         curr[part].v[Y] = -speed;
   }
}  /* Gen_init_cond */

/*---------------------------------------------------------------------
 * Function:  Output_state
 * Purpose:   Print the current state of the system
 * In args:
 *    curr:   array with n elements, curr[i] stores the state (mass,
 *            position and velocity) of the ith particle
 *    n:      number of particles
 */
void Output_state(double time, struct particle_s curr[], int n) {
   int part;
   printf("%.2f\n", time);
   for (part = 0; part < n; part++) {
//    printf("%.3f ", curr[part].m);
      printf("%3d %10.3e ", part, curr[part].s[X]);
      printf("  %10.3e ", curr[part].s[Y]);
      printf("  %10.3e ", curr[part].v[X]);
      printf("  %10.3e\n", curr[part].v[Y]);
   }
   printf("\n");
}  /* Output_state */

/*---------------------------------------------------------------------
 * Function:  Compute_force
 * Purpose:   Compute the total force on particle part.  Exploit
 *            the symmetry (force on particle i due to particle k) 
 *            = -(force on particle k due to particle i) to also
 *            calculate partial forces on other particles.
 * In args:   
 *    part:   the particle on which we're computing the total force
 *    curr:   current state of the system:  curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out arg:
 *    forces: force[i] stores the total force on the ith particle
 *
 * Note: This function uses the force due to gravitation.  So 
 * the force on particle i due to particle k is given by
 *
 *    m_i m_k (s_k - s_i)/|s_k - s_i|^2
 *
 * Here, m_j is the mass of particle j and s_k is its position vector
 * (at time t). 
 */
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n) {
   int k;
   double mg; 
   vect_t f_part_k;
   double len, len_3, fact;

#  ifdef DEBUG
   printf("Current total force on particle %d = (%.3e, %.3e)\n",
         part, forces[part][X], forces[part][Y]);
#  endif
   for (k = part+1; k < n; k++) {
      /* Compute force on part due to k */
      f_part_k[X] = curr[part].s[X] - curr[k].s[X];
      f_part_k[Y] = curr[part].s[Y] - curr[k].s[Y];
      len = sqrt(f_part_k[X]*f_part_k[X] + f_part_k[Y]*f_part_k[Y]);
      len_3 = len*len*len;
      mg = -G*curr[part].m*curr[k].m;
      fact = mg/len_3;
      f_part_k[X] *= fact;
      f_part_k[Y] *= fact;
#     ifdef DEBUG
      printf("Force on particle %d due to particle %d = (%.3e, %.3e)\n",
            part, k, f_part_k[X], f_part_k[Y]);
#     endif

      /* Add force in to total forces */
      forces[part][X] += f_part_k[X];
      forces[part][Y] += f_part_k[Y];
      forces[k][X] -= f_part_k[X];
      forces[k][Y] -= f_part_k[Y];
   }
}  /* Compute_force */

/*---------------------------------------------------------------------
 * Function:  Update_part
 * Purpose:   Update the velocity and position for particle part
 * In args:
 *    part:    the particle we're updating
 *    forces:  forces[i] stores the total force on the ith particle
 *    n:       number of particles
 *
 * In/out arg:
 *    curr:    curr[i] stores the mass, position and velocity of the
 *             ith particle
 *
 * Note:  This version uses Euler's method to update both the velocity
 *    and the position.
 */
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t) {
   double fact = delta_t/curr[part].m;

#  ifdef DEBUG
   printf("Before update of %d:\n", part);
   printf("   Position  = (%.3e, %.3e)\n", curr[part].s[X], curr[part].s[Y]);
   printf("   Velocity  = (%.3e, %.3e)\n", curr[part].v[X], curr[part].v[Y]);
   printf("   Net force = (%.3e, %.3e)\n", forces[part][X], forces[part][Y]);
#  endif
   curr[part].s[X] += delta_t * curr[part].v[X];
   curr[part].s[Y] += delta_t * curr[part].v[Y];
   curr[part].v[X] += fact * forces[part][X];
   curr[part].v[Y] += fact * forces[part][Y];
#  ifdef DEBUG
   printf("Position of %d = (%.3e, %.3e), Velocity = (%.3e,%.3e)\n",
         part, curr[part].s[X], curr[part].s[Y],
               curr[part].v[X], curr[part].v[Y]);
#  endif
// curr[part].s[X] += delta_t * curr[part].v[X];
// curr[part].s[Y] += delta_t * curr[part].v[Y];
}  /* Update_part */

/*---------------------------------------------------------------------
 * Function:  Compute_energy
 * Purpose:   Compute the kinetic and potential energy in the system
 * In args:
 *    curr:   current state of the system, curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out args:
 *    kin_en_p: pointer to kinetic energy of system
 *    pot_en_p: pointer to potential energy of system
 */
void Compute_energy(struct particle_s curr[], int n, double* kin_en_p,
      double* pot_en_p) {
   int i, j;
   vect_t diff;
   double pe = 0.0, ke = 0.0;
   double dist, speed_sqr;

   for (i = 0; i < n; i++) {
      speed_sqr = curr[i].v[X]*curr[i].v[X] + curr[i].v[Y]*curr[i].v[Y];
      ke += curr[i].m*speed_sqr;
   }
   ke *= 0.5;

   for (i = 0; i < n-1; i++) {
      for (j = i+1; j < n; j++) {
         diff[X] = curr[i].s[X] - curr[j].s[X];
         diff[Y] = curr[i].s[Y] - curr[j].s[Y];
         dist = sqrt(diff[X]*diff[X] + diff[Y]*diff[Y]);
         pe += -G*curr[i].m*curr[j].m/dist;
      }
   }

   *kin_en_p = ke;
   *pot_en_p = pe;
}  /* Compute_energy */

~~~
nbody_red.c
{:.figure}

### omp_nbody_basic.c

~~~c
/* File:     omp_nbody_basic.c
 * Purpose:  Implement a 2-dimensional n-body solver that uses the 
 *           basic algorithm.  So this version directly computes 
 *           all the forces.
 *
 * Compile:  gcc -g -Wall -fopenmp -o omp_nbody_basic omp_nbody_basic.c -lm
 *           To turn off output except for timing results, define NO_OUTPUT
 *           To get verbose output, define DEBUG
 *
 * Run:      ./omp_nbody_basic <number of threads> <number of particles>
 *              <number of timesteps>  <size of timestep> 
 *              <output frequency> <g|i>
 *              'g': generate initial conditions using a random number
 *                   generator
 *              'i': read initial conditions from stdin
 *           A timestep of 0.01 seems to work reasonably well for
 *           the automatically generated data.
 *
 * Input:    If 'g' is specified on the command line, none.  
 *           If 'i', mass, initial position and initial velocity of 
 *              each particle
 * Output:   If the output frequency is k, then position and velocity of 
 *              each particle at every kth timestep
 *
 * Algorithm: Slightly modified version of algorithm in James Demmel, 
 *    "CS 267, Applications of Parallel Computers:  Hierarchical 
 *    Methods for the N-Body Problem",
 *    www.cs.berkeley.edu/~demmel/cs267_Spr09, April 20, 2009.
 *
 *    for each timestep t {
 *       for each particle i
 *          compute f(i), the force on i
 *       for each particle i
 *          update position and velocity of i using F = ma
 *       if (output step) Output new positions and velocities
 *    }
 *
 * Force:    The force on particle i due to particle k is given by
 *
 *    -G m_i m_k (s_i - s_k)/|s_i - s_k|^3
 *
 * Here, m_j is the mass of particle j, s_j is its position vector
 * (at time t), and G is the gravitational constant (see below).  
 *
 * Integration:  We use Euler's method:
 *
 *    v_i(t+1) = v_i(t) + h v'_i(t)
 *    s_i(t+1) = s_i(t) + h v_i(t)
 *
 * Here, v_i(u) is the velocity of the ith particle at time u and
 * s_i(u) is its position.
 *
 * IPP:   Section 6.1.5 (pp. 281 and ff.)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <omp.h>

#define DIM 2  /* Two-dimensional system */
#define X 0    /* x-coordinate subscript */
#define Y 1    /* y-coordinate subscript */

const double G = 6.673e-11;  /* Gravitational constant. */
                             /* Units are m^3/(kg*s^2)  */
// const double G = 0.1;  /* Gravitational constant. */
                       /* Units are m^3/(kg*s^2)  */

typedef double vect_t[DIM];  /* Vector type for position, etc. */

struct particle_s {
   double m;  /* Mass     */
   vect_t s;  /* Position */
   vect_t v;  /* Velocity */
};

void Usage(char* prog_name);
void Get_args(int argc, char* argv[], int* thread_count_p, int* n_p, 
      int* n_steps_p, double* delta_t_p, int* output_freq_p, char* g_i_p);
void Get_init_cond(struct particle_s curr[], int n);
void Gen_init_cond(struct particle_s curr[], int n);
void Output_state(double time, struct particle_s curr[], int n);
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n);
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t);

/*--------------------------------------------------------------------*/
int main(int argc, char* argv[]) {
   int n;                      /* Number of particles        */
   int n_steps;                /* Number of timesteps        */
   int step;                   /* Current step               */
   int part;                   /* Current particle           */
   int output_freq;            /* Frequency of output        */
   double delta_t;             /* Size of timestep           */
   double t;                   /* Current Time               */
   struct particle_s* curr;    /* Current state of system    */
   vect_t* forces;             /* Forces on each particle    */
   int thread_count;           /* Number of threads          */
   char g_i;                   /*_G_en or _i_nput init conds */
   double start, finish;       /* For timings                */

   Get_args(argc, argv, &thread_count, &n, &n_steps, &delta_t, 
         &output_freq, &g_i);
   curr = malloc(n*sizeof(struct particle_s));
   forces = malloc(n*sizeof(vect_t));
   if (g_i == 'i')
      Get_init_cond(curr, n);
   else
      Gen_init_cond(curr, n);

   start = omp_get_wtime();
#  ifndef NO_OUTPUT
   Output_state(0, curr, n);
#  endif
#  pragma omp parallel num_threads(thread_count) default(none) \
      shared(curr, forces, thread_count, delta_t, n, n_steps, output_freq) \
      private(step, part, t)
   for (step = 1; step <= n_steps; step++) {
      t = step*delta_t;
//    memset(forces, 0, n*sizeof(vect_t));
#     pragma omp for
      for (part = 0; part < n; part++)
         Compute_force(part, forces, curr, n);
#     pragma omp for
      for (part = 0; part < n; part++)
         Update_part(part, forces, curr, n, delta_t);
#     ifndef NO_OUTPUT
#     pragma omp single
      if (step % output_freq == 0)
         Output_state(t, curr, n);
#     endif
   }
   
   finish = omp_get_wtime();
   printf("Elapsed time = %e seconds\n", finish-start);

   free(curr);
   free(forces);
   return 0;
}  /* main */

/*---------------------------------------------------------------------
 * Function: Usage
 * Purpose:  Print instructions for command-line and exit
 * In arg:   
 *    prog_name:  the name of the program as typed on the command-line
 */
void Usage(char* prog_name) {
   fprintf(stderr, "usage: %s <number of threads> <number of particles>\n",
         prog_name);
   fprintf(stderr, "   <number of timesteps> <size of timestep>\n"); 
   fprintf(stderr, "   <output frequency> <g|i>\n");
   fprintf(stderr, "   'g': program should generate init conds\n");
   fprintf(stderr, "   'i': program should get init conds from stdin\n");
    
   exit(0);
}  /* Usage */

/*---------------------------------------------------------------------
 * Function:  Get_args
 * Purpose:   Get command line args
 * In args:
 *    argc:            number of command line args
 *    argv:            command line args
 * Out args:
 *    thread_count_p:  pointer to thread_count, the number of threads
 *    n_p:             pointer to n, the number of particles
 *    n_steps_p:       pointer to n_steps, the number of timesteps
 *    delta_t_p:       pointer to delta_t, the size of each timestep
 *    output_freq_p:   pointer to output_freq, which is the number of
 *                     timesteps between steps whose output is printed
 *    g_i_p:           pointer to char which is 'g' if the init conds
 *                     should be generated by the program and 'i' if
 *                     they should be read from stdin
 */
void Get_args(int argc, char* argv[], int* thread_count_p, int* n_p, 
      int* n_steps_p, double* delta_t_p, int* output_freq_p, char* g_i_p) {
   if (argc != 7) Usage(argv[0]);
   *thread_count_p = strtol(argv[1], NULL, 10);
   *n_p = strtol(argv[2], NULL, 10);
   *n_steps_p = strtol(argv[3], NULL, 10);
   *delta_t_p = strtod(argv[4], NULL);
   *output_freq_p = strtol(argv[5], NULL, 10);
   *g_i_p = argv[6][0];

   if (*thread_count_p < 0 || *n_p <= 0 || *n_steps_p < 0 || *delta_t_p <= 0) 
      Usage(argv[0]);
   if (*g_i_p != 'g' && *g_i_p != 'i') Usage(argv[0]);

#  ifdef DEBUG
   printf("thread_count = %d\n", *thread_count_p);
   printf("n = %d\n", *n_p);
   printf("n_steps = %d\n", *n_steps_p);
   printf("delta_t = %e\n", *delta_t_p);
   printf("output_freq = %d\n", *output_freq_p);
   printf("g_i = %c\n", *g_i_p);
#  endif
}  /* Get_args */

/*---------------------------------------------------------------------
 * Function:  Get_init_cond
 * Purpose:   Read in initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 */
void Get_init_cond(struct particle_s curr[], int n) {
   int part;

   printf("For each particle, enter (in order):\n");
   printf("   its mass, its x-coord, its y-coord, ");
   printf("its x-velocity, its y-velocity\n");
   for (part = 0; part < n; part++) {
      scanf("%lf", &curr[part].m);
      scanf("%lf", &curr[part].s[X]);
      scanf("%lf", &curr[part].s[Y]);
      scanf("%lf", &curr[part].v[X]);
      scanf("%lf", &curr[part].v[Y]);
   }
}  /* Get_init_cond */

/*---------------------------------------------------------------------
 * Function:  Gen_init_cond
 * Purpose:   Generate initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 *
 * Note:      The initial conditions place all particles at
 *            equal intervals on the nonnegative x-axis with 
 *            identical masses, and identical initial speeds
 *            parallel to the y-axis.  However, some of the
 *            velocities are in the positive y-direction and
 *            some are negative.
 */
void Gen_init_cond(struct particle_s curr[], int n) {
   int part;
   double mass = 5.0e24;
   double gap = 1.0e5;
   double speed = 3.0e4;

   srandom(1);
   for (part = 0; part < n; part++) {
      curr[part].m = mass;
      curr[part].s[X] = part*gap;
      curr[part].s[Y] = 0.0;
      curr[part].v[X] = 0.0;
//    if (random()/((double) RAND_MAX) >= 0.5)
      if (part % 2 == 0)
         curr[part].v[Y] = speed;
      else
         curr[part].v[Y] = -speed;
   }
}  /* Gen_init_cond */

/*---------------------------------------------------------------------
 * Function:  Output_state
 * Purpose:   Print the current state of the system
 * In args:
 *    curr:   array with n elements, curr[i] stores the state (mass,
 *            position and velocity) of the ith particle
 *    n:      number of particles
 */
void Output_state(double time, struct particle_s curr[], int n) {
   int part;
   printf("%.2f\n", time);
   for (part = 0; part < n; part++) {
//    printf("%.3f ", curr[part].m);
      printf("%3d %10.3e ", part, curr[part].s[X]);
      printf("  %10.3e ", curr[part].s[Y]);
      printf("  %10.3e ", curr[part].v[X]);
      printf("  %10.3e\n", curr[part].v[Y]);
   }
   printf("\n");
}  /* Output_state */

/*---------------------------------------------------------------------
 * Function:  Compute_force
 * Purpose:   Compute the total force on particle part.  
 * In args:   
 *    part:   the particle on which we're computing the total force
 *    curr:   current state of the system:  curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out arg:
 *    forces: force[i] stores the total force on the ith particle
 *
 * Note: This function uses the force due to gravitation.  So 
 * the force on particle i due to particle k is given by
 *
 *    m_i m_k (s_k - s_i)/|s_k - s_i|^2
 *
 * Here, m_j is the mass of particle j and s_k is its position vector
 * (at time t). 
 */
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n) {
   int k;
   double mg; 
   vect_t f_part_k;
   double len, len_3, fact;

#  ifdef DEBUG
   printf("Current total force on particle %d = (%.3e, %.3e)\n",
         part, forces[part][X], forces[part][Y]);
#  endif
   forces[part][X] = forces[part][Y] = 0.0;
   for (k = 0; k < n; k++) {
      if (k != part) {
      /* Compute force on part due to k */
         f_part_k[X] = curr[part].s[X] - curr[k].s[X];
         f_part_k[Y] = curr[part].s[Y] - curr[k].s[Y];
         len = sqrt(f_part_k[X]*f_part_k[X] + f_part_k[Y]*f_part_k[Y]);
         len_3 = len*len*len;
         mg = -G*curr[part].m*curr[k].m;
         fact = mg/len_3;
         f_part_k[X] *= fact;
         f_part_k[Y] *= fact;
   #     ifdef DEBUG
         printf("Force on particle %d due to particle %d = (%.3e, %.3e)\n",
               part, k, f_part_k[X], f_part_k[Y]);
   #     endif
   
         /* Add force in to total forces */
         forces[part][X] += f_part_k[X];
         forces[part][Y] += f_part_k[Y];
      }
   }
}  /* Compute_force */

/*---------------------------------------------------------------------
 * Function:  Update_part
 * Purpose:   Update the velocity and position for particle part
 * In args:
 *    part:    the particle we're updating
 *    forces:  forces[i] stores the total force on the ith particle
 *    n:       number of particles
 *
 * In/out arg:
 *    curr:    curr[i] stores the mass, position and velocity of the
 *             ith particle
 *
 * Note:  This version uses Euler's method to update both the velocity
 *    and the position.
 */
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t) {
   double fact = delta_t/curr[part].m;

#  ifdef DEBUG
   printf("Before update of %d:\n", part);
   printf("   Position  = (%.3e, %.3e)\n", curr[part].s[X], curr[part].s[Y]);
   printf("   Velocity  = (%.3e, %.3e)\n", curr[part].v[X], curr[part].v[Y]);
   printf("   Net force = (%.3e, %.3e)\n", forces[part][X], forces[part][Y]);
#  endif
   curr[part].s[X] += delta_t * curr[part].v[X];
   curr[part].s[Y] += delta_t * curr[part].v[Y];
   curr[part].v[X] += fact * forces[part][X];
   curr[part].v[Y] += fact * forces[part][Y];
#  ifdef DEBUG
   printf("Position of %d = (%.3e, %.3e), Velocity = (%.3e,%.3e)\n",
         part, curr[part].s[X], curr[part].s[Y],
               curr[part].v[X], curr[part].v[Y]);
#  endif
// curr[part].s[X] += delta_t * curr[part].v[X];
// curr[part].s[Y] += delta_t * curr[part].v[Y];
}  /* Update_part */

/*---------------------------------------------------------------------
 * Function:  Compute_energy
 * Purpose:   Compute the kinetic and potential energy in the system
 * In args:
 *    curr:   current state of the system, curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out args:
 *    kin_en_p: pointer to kinetic energy of system
 *    pot_en_p: pointer to potential energy of system
 */
void Compute_energy(struct particle_s curr[], int n, double* kin_en_p,
      double* pot_en_p) {
   int i, j;
   vect_t diff;
   double pe = 0.0, ke = 0.0;
   double dist, speed_sqr;

   for (i = 0; i < n; i++) {
      speed_sqr = curr[i].v[X]*curr[i].v[X] + curr[i].v[Y]*curr[i].v[Y];
      ke += curr[i].m*speed_sqr;
   }
   ke *= 0.5;

   for (i = 0; i < n-1; i++) {
      for (j = i+1; j < n; j++) {
         diff[X] = curr[i].s[X] - curr[j].s[X];
         diff[Y] = curr[i].s[Y] - curr[j].s[Y];
         dist = sqrt(diff[X]*diff[X] + diff[Y]*diff[Y]);
         pe += -G*curr[i].m*curr[j].m/dist;
      }
   }

   *kin_en_p = ke;
   *pot_en_p = pe;
}  /* Compute_energy */
~~~
omp_nbody_basic.c
{:.figure}

### omp_nbody_red.c

~~~c
/* File:     omp_nbody_red.c
 *
 * Purpose:  Use OpenMP to parallelize a 2-dimensional n-body solver 
 *           that uses the reduced algorithm.  This version uses one 
 *           array per thread to store locally computed forces.
 *           These forces are then added into a shared array.  It
 *           uses a block schedule for each of the parallel for
 *           except the loop that computes forces, which uses
 *           a cyclic distribution.
 *
 * Compile:  gcc -g -Wall -fopenmp -o omp_nbody_red omp_nbody_red.c -lm
 *           To turn off output (e.g., when timing), define NO_OUTPUT
 *           To get verbose output, define DEBUG
 *
 * Run:      ./omp_nbody_red <number of threads> <number of particles>
 *              <number of timesteps>  <size of timestep> 
 *              <output frequency> <g|i>
 *              'g': generate initial conditions using a random number
 *                   generator
 *              'i': read initial conditions from stdin
 *            0.01 seems to work well as a timestep for the automatically
 *            generated data.
 *
 * Input:    If 'g' is specified on the command line, none.  
 *           If 'i', mass, initial position and initial velocity of 
 *              each particle
 * Output:   If the output frequency is k, then position and velocity of 
 *              each particle at every kth timestep
 *
 * Force:    The force on particle i due to particle k is given by
 *
 *    -G m_i m_k (s_i - s_k)/|s_i - s_k|^3
 *
 * Here, m_j is the mass of particle j, s_j is its position vector
 * (at time t), and G is the gravitational constant (see below).  
 *
 * Note that the force on particle k due to particle i is 
 * -(force on i due to k).  So we can approximately halve the number 
 * of force computations.
 *
 * Integration:  We use Euler's method:
 *
 *    v_i(t+1) = v_i(t) + h v'_i(t)
 *    s_i(t+1) = s_i(t) + h v_i(t)
 *
 * Here, v_i(u) is the velocity of the ith particle at time u and
 * s_i(u) is its position.
 *
 * IPP:  Section 6.1.6 (pp. 284 and ff.)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <omp.h>

#define DIM 2  /* Two-dimensional system */
#define X 0    /* x-coordinate subscript */
#define Y 1    /* y-coordinate subscript */

const double G = 6.673e-11;  /* Gravitational constant. */
                             /* Units are m^3/(kg*s^2)  */

typedef double vect_t[DIM];  /* Vector type for position, etc. */

struct particle_s {
   double m;  /* Mass     */
   vect_t s;  /* Position */
   vect_t v;  /* Velocity */
};

void Usage(char* prog_name);
void Get_args(int argc, char* argv[], int* thread_count_p, int* n_p, 
      int* n_steps_p, double* delta_t_p, int* output_freq_p, char* g_i_p);
void Get_init_cond(struct particle_s curr[], int n);
void Gen_init_cond(struct particle_s curr[], int n);
void Output_state(double time, struct particle_s curr[], int n);
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n);
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t);

/*--------------------------------------------------------------------*/
int main(int argc, char* argv[]) {
   int n;                      /* Number of particles              */
   int n_steps;                /* Number of timesteps              */
   int step;                   /* Current step                     */
   int part;                   /* Current particle                 */
   int output_freq;            /* Frequency of output              */
   double delta_t;             /* Size of timestep                 */
   double t;                   /* Current Time                     */
   struct particle_s* curr;    /* Current state of system          */
   vect_t* forces;             /* Forces on each particle          */
   int thread_count;           /* Number of threads                */
   char g_i;                   /* _G_enerate or _i_nput init conds */
   double start, finish;       /* For timing                       */
   vect_t* loc_forces;         /* Forces computed by each thread   */

   Get_args(argc, argv, &thread_count, &n, &n_steps, &delta_t, 
         &output_freq, &g_i);
   curr = malloc(n*sizeof(struct particle_s));
   forces = malloc(n*sizeof(vect_t));
   loc_forces = malloc(thread_count*n*sizeof(vect_t));
   if (g_i == 'i')
      Get_init_cond(curr, n);
   else
      Gen_init_cond(curr, n);

   start = omp_get_wtime();
#  ifndef NO_OUTPUT
   Output_state(0, curr, n);
#  endif
#  pragma omp parallel num_threads(thread_count) default(none) \
      shared(curr,forces,thread_count,delta_t,n,n_steps, \
            output_freq,loc_forces) \
      private(step, part, t)
   {
      int my_rank = omp_get_thread_num();
      int thread;

      for (step = 1; step <= n_steps; step++) {
         t = step*delta_t;
//       memset(loc_forces + my_rank*n, 0, n*sizeof(vect_t));
#        pragma omp for
         for (part = 0; part < thread_count*n; part++)
            loc_forces[part][X] = loc_forces[part][Y] = 0.0;
#        ifdef DEBUG
#        pragma omp single
         {
            printf("Step %d, after memset loc_forces = \n", step);
            for (part = 0; part < thread_count*n; part++)
               printf("%d %e %e\n", part, loc_forces[part][X], 
                  loc_forces[part][Y]);
            printf("\n");
         }
#        endif
         /* Particle n-1 will have all forces computed after call to
          * Compute_force(n-2, . . .) */
#        pragma omp for schedule(static,1)
         for (part = 0; part < n-1; part++)
            Compute_force(part, loc_forces + my_rank*n, curr, n);
#        pragma omp for 
         for (part = 0; part < n; part++) {
            forces[part][X] = forces[part][Y] = 0.0;
            for (thread = 0; thread < thread_count; thread++) {
               forces[part][X] += loc_forces[thread*n + part][X];
               forces[part][Y] += loc_forces[thread*n + part][Y];
            }
         }
#        pragma omp for
         for (part = 0; part < n; part++)
            Update_part(part, forces, curr, n, delta_t);
#        ifndef NO_OUTPUT
         if (step % output_freq == 0) {
#           pragma omp single
            Output_state(t, curr, n);
         }
#        endif
      }  /* for step */
   }  /* pragma omp parallel */
   finish = omp_get_wtime();
   printf("Elapsed time = %e seconds\n", finish-start);

   free(curr);
   free(forces);
   free(loc_forces);
   return 0;
}  /* main */

/*---------------------------------------------------------------------
 * Function: Usage
 * Purpose:  Print instructions for command-line and exit
 * In arg:   
 *    prog_name:  the name of the program as typed on the command-line
 */
void Usage(char* prog_name) {
   fprintf(stderr, "usage: %s <number of threads> <number of particles>\n",
         prog_name);
   fprintf(stderr, "   <number of timesteps>  <size of timestep>\n");
   fprintf(stderr, "   <output frequency> <g|i>\n");
   fprintf(stderr, "   'g': program should generate init conds\n");
   fprintf(stderr, "   'i': program should get init conds from stdin\n");
    
   exit(0);
}  /* Usage */

/*---------------------------------------------------------------------
 * Function:  Get_args
 * Purpose:   Get command line args
 * In args:
 *    argc:            number of command line args
 *    argv:            command line args
 * Out args:
 *    thread_count_p:  pointer to thread_count
 *    n_p:             pointer to n, the number of particles
 *    n_steps_p:       pointer to n_steps, the number of timesteps
 *    delta_t_p:       pointer to delta_t, the size of each timestep
 *    output_freq_p:   pointer to output_freq, which is the number of
 *                     timesteps between steps whose output is printed
 *    g_i_p:           pointer to char which is 'g' if the init conds
 *                     should be generated by the program and 'i' if
 *                     they should be read from stdin
 */
void Get_args(int argc, char* argv[], int* thread_count_p, int* n_p, 
      int* n_steps_p, double* delta_t_p, int* output_freq_p, 
      char* g_i_p) {
   if (argc != 7) Usage(argv[0]);
   *thread_count_p = strtol(argv[1], NULL, 10);
   *n_p = strtol(argv[2], NULL, 10);
   *n_steps_p = strtol(argv[3], NULL, 10);
   *delta_t_p = strtod(argv[4], NULL);
   *output_freq_p = strtol(argv[5], NULL, 10);
   *g_i_p = argv[6][0];

   if (*thread_count_p <= 0 || *n_p <= 0 || *n_steps_p < 0 ||
       *delta_t_p <= 0) Usage(argv[0]);
   if (*g_i_p != 'g' && *g_i_p != 'i') Usage(argv[0]);

#  ifdef DEBUG
   printf("thread_count = %d\n", *thread_count_p);
   printf("n = %d\n", *n_p);
   printf("n_steps = %d\n", *n_steps_p);
   printf("delta_t = %e\n", *delta_t_p);
   printf("output_freq = %d\n", *output_freq_p);
   printf("g_i = %c\n", *g_i_p);
#  endif
}  /* Get_args */

/*---------------------------------------------------------------------
 * Function:  Get_init_cond
 * Purpose:   Read in initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 */
void Get_init_cond(struct particle_s curr[], int n) {
   int part;

   printf("For each particle, enter (in order):\n");
   printf("   its mass, its x-coord, its y-coord, ");
   printf("its x-velocity, its y-velocity\n");
   for (part = 0; part < n; part++) {
      scanf("%lf", &curr[part].m);
      scanf("%lf", &curr[part].s[X]);
      scanf("%lf", &curr[part].s[Y]);
      scanf("%lf", &curr[part].v[X]);
      scanf("%lf", &curr[part].v[Y]);
   }
}  /* Get_init_cond */

/*---------------------------------------------------------------------
 * Function:  Gen_init_cond
 * Purpose:   Generate initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:      number of particles
 * Out args:
 *    curr:   array of n structs, each struct stores the mass (scalar),
 *            position (vector), and velocity (vector) of a particle
 *
 * Note:      The initial conditions place all particles at
 *            equal intervals on the nonnegative x-axis with 
 *            identical masses, and identical initial speeds
 *            parallel to the y-axis.  However, some of the
 *            velocities are in the positive y-direction and
 *            some are negative.
 */
void Gen_init_cond(struct particle_s curr[], int n) {
   int part;
   double mass = 5.0e24;
   double gap = 1.0e5;
   double speed = 3.0e4;

   srandom(1);
   for (part = 0; part < n; part++) {
      curr[part].m = mass;
      curr[part].s[X] = part*gap;
      curr[part].s[Y] = 0.0;
      curr[part].v[X] = 0.0;
//    if (random()/((double) RAND_MAX) >= 0.5)
      if (part % 2 == 0)
         curr[part].v[Y] = speed;
      else
         curr[part].v[Y] = -speed;
   }
}  /* Gen_init_cond */

/*---------------------------------------------------------------------
 * Function:  Output_state
 * Purpose:   Print the current state of the system
 * In args:
 *    curr:   array with n elements, curr[i] stores the state (mass,
 *            position and velocity) of the ith particle
 *    n:      number of particles
 */
void Output_state(double time, struct particle_s curr[], int n) {
   int part;
   printf("%.2f\n", time);
   for (part = 0; part < n; part++) {
//    printf("%.3e ", curr[part].m);
      printf("%3d %10.3e ", part, curr[part].s[X]);
      printf("  %10.3e ", curr[part].s[Y]);
      printf("  %10.3e ", curr[part].v[X]);
      printf("  %10.3e\n", curr[part].v[Y]);
   }
   printf("\n");
}  /* Output_state */

/*---------------------------------------------------------------------
 * Function:  Compute_force
 * Purpose:   Compute the total force on particle part.  Exploit
 *            the symmetry (force on particle i due to particle k) 
 *            = -(force on particle k due to particle i) to also
 *            calculate partial forces on other particles.
 * In args:   
 *    part:   the particle on which we're computing the total force
 *    curr:   current state of the system:  curr[i] stores the mass,
 *            position and velocity of the ith particle
 *    n:      number of particles
 * Out arg:
 *    forces: force[i] stores the total force on the ith particle
 *
 * Note: This function uses the force due to gravitation.  So 
 * the force on particle i due to particle k is given by
 *
 *    m_i m_k (s_k - s_i)/|s_k - s_i|^2
 *
 * Here, m_j is the mass of particle j and s_k is its position vector
 * (at time t). 
 */
void Compute_force(int part, vect_t forces[], struct particle_s curr[], 
      int n) {
   int k;
   double mg; 
   vect_t f_part_k;
   double len, len_3, fact;

#  ifdef DEBUG
   printf("Current total force on particle %d = (%.3e, %.3e)\n",
         part, forces[part][X], forces[part][Y]);
#  endif
   for (k = part+1; k < n; k++) {
      /* Compute force on part due to k */
      f_part_k[X] = curr[part].s[X] - curr[k].s[X];
      f_part_k[Y] = curr[part].s[Y] - curr[k].s[Y];
      len = sqrt(f_part_k[X]*f_part_k[X] + f_part_k[Y]*f_part_k[Y]);
      len_3 = len*len*len;
      mg = -G*curr[part].m*curr[k].m;
      fact = mg/len_3;
      f_part_k[X] *= fact;
      f_part_k[Y] *= fact;
#     ifdef DEBUG
      printf("Force on particle %d due to particle %d = (%.3e, %.3e)\n",
            part, k, f_part_k[X], f_part_k[Y]);
#     endif

      /* Add force into total forces */
      forces[part][X] += f_part_k[X];
      forces[part][Y] += f_part_k[Y];
      forces[k][X] -= f_part_k[X];
      forces[k][Y] -= f_part_k[Y];
   }
}  /* Compute_force */

/*---------------------------------------------------------------------
 * Function:  Update_part
 * Purpose:   Update the velocity and position for particle part
 * In args:
 *    part:    the particle we're updating
 *    forces:  forces[i] stores the total force on the ith particle
 *    n:       number of particles
 *
 * In/out arg:
 *    curr:    curr[i] stores the mass, position and velocity of the
 *             ith particle
 *
 * Note:  This version uses Euler's method to update both the velocity
 *    and the position.
 */
void Update_part(int part, vect_t forces[], struct particle_s curr[], 
      int n, double delta_t) {
   double fact = delta_t/curr[part].m;

#  ifdef DEBUG
   printf("Before update of %d:\n", part);
   printf("   Position  = (%.3e, %.3e)\n", curr[part].s[X], curr[part].s[Y]);
   printf("   Velocity  = (%.3e, %.3e)\n", curr[part].v[X], curr[part].v[Y]);
   printf("   Net force = (%.3e, %.3e)\n", forces[part][X], forces[part][Y]);
#  endif
   curr[part].s[X] += delta_t * curr[part].v[X];
   curr[part].s[Y] += delta_t * curr[part].v[Y];
   curr[part].v[X] += fact * forces[part][X];
   curr[part].v[Y] += fact * forces[part][Y];
#  ifdef DEBUG
   printf("Position of %d = (%.3e, %.3e), Velocity = (%.3e,%.3e)\n",
         part, curr[part].s[X], curr[part].s[Y],
               curr[part].v[X], curr[part].v[Y]);
#  endif
// curr[part].s[X] += delta_t * curr[part].v[X];
// curr[part].s[Y] += delta_t * curr[part].v[Y];
}  /* Update_part */
~~~
omp_nbody_red.c
{:.figure}

### mpi_nbody_basic.c

~~~c
/* File:     mpi_nbody_basic.c
 * Purpose:  Implement a 2-dimensional n-body solver that uses the 
 *           basic algorithm.  This version uses an in-place Allgather
 *
 * Compile:  mpicc -g -Wall -o mpi_nbody_basic mpi_nbody_basic.c -lm
 *           To turn off output (e.g., when timing), define NO_OUTPUT
 *           To get verbose output, define DEBUG
 *
 * Run:      mpiexec -n <number of processes> ./mpi_nbody_basic
 *              <number of particles> <number of timesteps>  <size of timestep> 
 *              <output frequency> <g|i>
 *              'g': generate initial conditions using a random number
 *                   generator
 *              'i': read initial conditions from stdin
 *              number of particles should be evenly divisible by the number
 *                 of MPI processes
 *           A stepsize of 0.01 seems to work well with automatically
 *           generated data.
 *
 * Input:    If 'g' is specified on the command line, none.  
 *           If 'i', mass, initial position and initial velocity of 
 *              each particle
 * Output:   If the output frequency is k, then position and velocity of 
 *              each particle at every kth timestep.  This value is
 *              ignored (but still necessary) if NO_OUTPUT is defined
 *
 *    for each timestep t {
 *       for each particle i I own
 *          compute F(i), the total force on i
 *       for each particle i I own
 *          update position and velocity of i using F(i) = ma
 *       Allgather positions
 *       if (output step) {
 *          Allgather velocities
 *          Output new positions and velocities
 *       }
 *    }
 *
 * Force:    The force on particle i due to particle k is given by
 *
 *    -G m_i m_k (s_i - s_k)/|s_i - s_k|^3
 *
 * Here, m_j is the mass of particle j, s_j is its position vector
 * (at time t), and G is the gravitational constant (see below).  
 *
 * Note that the force on particle k due to particle i is 
 * -(force on i due to k).  So we could approximately halve the number 
 * of force computations.  This version of the program does not
 * exploit this.
 *
 * Integration:  We use Euler's method:
 *
 *    v_i(t+1) = v_i(t) + h v'_i(t)
 *    s_i(t+1) = s_i(t) + h v_i(t)
 *
 * Here, v_i(u) is the velocity of the ith particle at time u and
 * s_i(u) is its position.
 *
 * Notes:
 * 1.  Each process stores the masses of all the particles:  the
 *     masses array has dimension n = number of particles.
 *
 * IPP:  Section 6.1.9 (pp. 290 and ff.)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <mpi.h>

#define DIM 2  /* Two-dimensional system */
#define X 0    /* x-coordinate subscript */
#define Y 1    /* y-coordinate subscript */

typedef double vect_t[DIM];  /* Vector type for position, etc. */

/* Global variables.  Except or vel all are unchanged after being set */
const double G = 6.673e-11;  /* Gravitational constant. */
                             /* Units are m^3/(kg*s^2)  */
int my_rank, comm_sz;
MPI_Comm comm;
MPI_Datatype vect_mpi_t;

/* Scratch array used by process 0 for global velocity I/O */
vect_t *vel = NULL;

void Usage(char* prog_name);
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p);
void Get_init_cond(double masses[], vect_t pos[], 
      vect_t loc_vel[], int n, int loc_n);
void Gen_init_cond(double masses[], vect_t pos[], 
      vect_t loc_vel[], int n, int loc_n);
void Output_state(double time, double masses[], vect_t pos[],
      vect_t loc_vel[], int n, int loc_n);
void Compute_force(int loc_part, double masses[], vect_t loc_forces[], 
      vect_t pos[], int n, int loc_n);
void Update_part(int loc_part, double masses[], vect_t loc_forces[], 
      vect_t loc_pos[], vect_t loc_vel[], int n, int loc_n, double delta_t);

/*--------------------------------------------------------------------*/
int main(int argc, char* argv[]) {
   int n;                      /* Total number of particles  */
   int loc_n;                  /* Number of my particles     */
   int n_steps;                /* Number of timesteps        */
   int step;                   /* Current step               */
   int loc_part;               /* Current local particle     */
   int output_freq;            /* Frequency of output        */
   double delta_t;             /* Size of timestep           */
   double t;                   /* Current Time               */
   double* masses;             /* All the masses             */
   vect_t* loc_pos;            /* Positions of my particles  */
   vect_t* pos;                /* Positions of all particles */
   vect_t* loc_vel;            /* Velocities of my particles */
   vect_t* loc_forces;         /* Forces on my particles     */

   char g_i;                   /*_G_en or _i_nput init conds */
   double start, finish;       /* For timings                */

   MPI_Init(&argc, &argv);
   comm = MPI_COMM_WORLD;
   MPI_Comm_size(comm, &comm_sz);
   MPI_Comm_rank(comm, &my_rank);

   Get_args(argc, argv, &n, &n_steps, &delta_t, &output_freq, &g_i);
   loc_n = n/comm_sz;  /* n should be evenly divisible by comm_sz */
   masses = malloc(n*sizeof(double));
   pos = malloc(n*sizeof(vect_t));
   loc_forces = malloc(loc_n*sizeof(vect_t));
   loc_pos = pos + my_rank*loc_n;
   loc_vel = malloc(loc_n*sizeof(vect_t));
   if (my_rank == 0) vel = malloc(n*sizeof(vect_t));
   MPI_Type_contiguous(DIM, MPI_DOUBLE, &vect_mpi_t);
   MPI_Type_commit(&vect_mpi_t);

   if (g_i == 'i')
      Get_init_cond(masses, pos, loc_vel, n, loc_n);
   else
      Gen_init_cond(masses, pos, loc_vel, n, loc_n);

   start = MPI_Wtime();
#  ifndef NO_OUTPUT
   Output_state(0.0, masses, pos, loc_vel, n, loc_n);
#  endif
   for (step = 1; step <= n_steps; step++) {
      t = step*delta_t;
      for (loc_part = 0; loc_part < loc_n; loc_part++)
         Compute_force(loc_part, masses, loc_forces, pos, n, loc_n);
      for (loc_part = 0; loc_part < loc_n; loc_part++)
         Update_part(loc_part, masses, loc_forces, loc_pos, loc_vel, 
               n, loc_n, delta_t);
      MPI_Allgather(MPI_IN_PLACE, loc_n, vect_mpi_t, 
                    pos, loc_n, vect_mpi_t, comm);
#     ifndef NO_OUTPUT
      if (step % output_freq == 0)
         Output_state(t, masses, pos, loc_vel, n, loc_n);
#     endif
   }
   
   finish = MPI_Wtime();
   if (my_rank == 0)
      printf("Elapsed time = %e seconds\n", finish-start);

   MPI_Type_free(&vect_mpi_t);
   free(masses);
   free(pos);
   free(loc_forces);
   free(loc_vel);
   if (my_rank == 0) free(vel);

   MPI_Finalize();

   return 0;
}  /* main */

/*---------------------------------------------------------------------
 * Function: Usage
 * Purpose:  Print instructions for command-line and exit
 * In arg:   
 *    prog_name:  the name of the program as typed on the command-line
 */
void Usage(char* prog_name) {
   
   fprintf(stderr, "usage: mpiexec -n <number of processes> %s\n", prog_name);
   fprintf(stderr, "   <number of particles> <number of timesteps>\n");
   fprintf(stderr, "   <size of timestep> <output frequency>\n");
   fprintf(stderr, "   <g|i>\n");
   fprintf(stderr, "   'g': program should generate init conds\n");
   fprintf(stderr, "   'i': program should get init conds from stdin\n");
    
   exit(0);
}  /* Usage */

/*---------------------------------------------------------------------
 * Function:  Get_args
 * Purpose:   Get command line args
 * In args:
 *    argc:            number of command line args
 *    argv:            command line args
 * Out args:
 *    n_p:             pointer to n, the number of particles
 *    n_steps_p:       pointer to n_steps, the number of timesteps
 *    delta_t_p:       pointer to delta_t, the size of each timestep
 *    output_freq_p:   pointer to output_freq, which is the number of
 *                     timesteps between steps whose output is printed
 *    g_i_p:           pointer to char which is 'g' if the init conds
 *                     should be generated by the program and 'i' if
 *                     they should be read from stdin
 */
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p) {
   if (my_rank == 0) {
      if (argc != 6) Usage(argv[0]);
      *n_p = strtol(argv[1], NULL, 10);
      *n_steps_p = strtol(argv[2], NULL, 10);
      *delta_t_p = strtod(argv[3], NULL);
      *output_freq_p = strtol(argv[4], NULL, 10);
      *g_i_p = argv[5][0];
   }
   MPI_Bcast(n_p, 1, MPI_INT, 0, comm);
   MPI_Bcast(n_steps_p, 1, MPI_INT, 0, comm);
   MPI_Bcast(delta_t_p, 1, MPI_DOUBLE, 0, comm);
   MPI_Bcast(output_freq_p, 1, MPI_INT, 0, comm);
   MPI_Bcast(g_i_p, 1, MPI_CHAR, 0, comm);

   if (*n_p <= 0 || *n_steps_p < 0 || *delta_t_p <= 0) {
      if (my_rank == 0) Usage(argv[0]);
      MPI_Finalize();
      exit(0);
   }
   if (*g_i_p != 'g' && *g_i_p != 'i') {
      if (my_rank == 0) Usage(argv[0]);
      MPI_Finalize();
      exit(0);
   }
#  ifdef DEBUG
   if (my_rank == 0) {
      printf("n = %d\n", *n_p);
      printf("n_steps = %d\n", *n_steps_p);
      printf("delta_t = %e\n", *delta_t_p);
      printf("output_freq = %d\n", *output_freq_p);
      printf("g_i = %c\n", *g_i_p);
   }
#  endif
}  /* Get_args */

/*---------------------------------------------------------------------
 * Function:   Get_init_cond
 * Purpose:    Read in initial conditions:  mass, position and velocity
 *             for each particle
 * In args:  
 *    n:       total number of particles
 *    loc_n:   number of particles assigned to this process
 * Out args:
 *    masses:  global array of the masses of the particles
 *    pos:     global array of positions
 *    loc_vel: local array of velocities assigned to this process.
 *
 * Global var:
 *    vel:     Scratch.  Used by process 0 for global velocities
 */
void Get_init_cond(double masses[], vect_t pos[], 
     vect_t loc_vel[], int n, int loc_n) {
   int part;

   if (my_rank == 0) {
      printf("For each particle, enter (in order):\n");
      printf("   its mass, its x-coord, its y-coord, ");
      printf("its x-velocity, its y-velocity\n");
      for (part = 0; part < n; part++) {
         scanf("%lf", &masses[part]);
         scanf("%lf", &pos[part][X]);
         scanf("%lf", &pos[part][Y]);
         scanf("%lf", &vel[part][X]);
         scanf("%lf", &vel[part][Y]);
      }
   }
   MPI_Bcast(masses, n, MPI_DOUBLE, 0, comm);
   MPI_Bcast(pos, n, vect_mpi_t, 0, comm);
   MPI_Scatter(vel, loc_n, vect_mpi_t, 
         loc_vel, loc_n, vect_mpi_t, 0, comm);
}  /* Get_init_cond */

/*---------------------------------------------------------------------
 * Function:  Gen_init_cond
 * Purpose:   Generate initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:       total number of particles
 *    loc_n:   number of particles assigned to this process
 * Out args:
 *    masses:  global array of the masses of the particles
 *    pos:     global array of positions
 *    loc_vel: local array of velocities assigned to this process.
 * Global var:
 *    vel:     Scratch.  Used by process 0 for global velocities
 *
 * Note:      The initial conditions place all particles at
 *            equal intervals on the nonnegative x-axis with 
 *            identical masses, and identical initial speeds
 *            parallel to the y-axis.  However, some of the
 *            velocities are in the positive y-direction and
 *            some are negative.
 */
void Gen_init_cond(double masses[], vect_t pos[], 
      vect_t loc_vel[], int n, int loc_n) {
   int part;
   double mass = 5.0e24;
   double gap = 1.0e5;
   double speed = 3.0e4;

   if (my_rank == 0) {
//    srandom(1);
      for (part = 0; part < n; part++) {
         masses[part] = mass;
         pos[part][X] = part*gap;
         pos[part][Y] = 0.0;
         vel[part][X] = 0.0;
//       if (random()/((double) RAND_MAX) >= 0.5)
         if (part % 2 == 0)
            vel[part][Y] = speed;
         else
            vel[part][Y] = -speed;
      }
   }

   MPI_Bcast(masses, n, MPI_DOUBLE, 0, comm);
   MPI_Bcast(pos, n, vect_mpi_t, 0, comm);
   MPI_Scatter(vel, loc_n, vect_mpi_t, 
         loc_vel, loc_n, vect_mpi_t, 0, comm);
}  /* Gen_init_cond */

/*---------------------------------------------------------------------
 * Function:   Output_state
 * Purpose:    Print the current state of the system
 * In args:
 *    time:    current time
 *    masses:  global array of particle masses
 *    pos:     global array of particle positions
 *    loc_vel: local array of my particle velocities
 *    n:       total number of particles
 *    loc_n:   number of my particles
 */
void Output_state(double time, double masses[], vect_t pos[],
      vect_t loc_vel[], int n, int loc_n) {
   int part;

   MPI_Gather(loc_vel, loc_n, vect_mpi_t, vel, loc_n, vect_mpi_t, 
         0, comm);
   if (my_rank == 0) {
      printf("%.2f\n", time);
      for (part = 0; part < n; part++) {
//       printf("%.3f ", masses[part]);
         printf("%3d %10.3e ", part, pos[part][X]);
         printf("  %10.3e ", pos[part][Y]);
         printf("  %10.3e ", vel[part][X]);
         printf("  %10.3e\n", vel[part][Y]);
      }
      printf("\n");
   }
}  /* Output_state */

/*---------------------------------------------------------------------
 * Function:       Compute_force
 * Purpose:        Compute the total force on particle loc_part.  Don't 
 *                 exploit the symmetry (force on particle i due to 
 *                 particle k) = -(force on particle k due to particle i) 
 * In args:   
 *    loc_part:    the particle (local index) on which we're computing 
 *                 the total force
 *    masses:      global array of particle masses
 *    pos:         global array of particle positions
 *    n:           total number of particles
 *    loc_n:       number of my particles
 * Out arg:
 *    loc_forces:  array of total forces acting on my particles
 *
 * Note: This function uses the force due to gravitation.  So 
 * the force on particle i due to particle k is given by
 *
 *    m_i m_k (s_k - s_i)/|s_k - s_i|^2
 *
 * Here, m_k is the mass of particle k and s_k is its position vector
 * (at time t). 
 */
void Compute_force(int loc_part, double masses[], vect_t loc_forces[], 
      vect_t pos[], int n, int loc_n) {
   int k, part;
   double mg; 
   vect_t f_part_k;
   double len, len_3, fact;

   /* Global index corresponding to loc_part */
   part = my_rank*loc_n + loc_part;
   loc_forces[loc_part][X] = loc_forces[loc_part][Y] = 0.0;
#  ifdef DEBUG
   printf("Proc %d > Current total force on part %d = (%.3e, %.3e)\n",
         my_rank, part, loc_forces[loc_part][X], 
         loc_forces[loc_part][Y]);
#  endif
   for (k = 0; k < n; k++) {
      if (k != part) {
         /* Compute force on part due to k */
         f_part_k[X] = pos[part][X] - pos[k][X];
         f_part_k[Y] = pos[part][Y] - pos[k][Y];
         len = sqrt(f_part_k[X]*f_part_k[X] + f_part_k[Y]*f_part_k[Y]);
         len_3 = len*len*len;
         mg = -G*masses[part]*masses[k];
         fact = mg/len_3;
         f_part_k[X] *= fact;
         f_part_k[Y] *= fact;
#        ifdef DEBUG
         printf("Proc %d > Force on part %d due to part %d = (%.3e, %.3e)\n",
               my_rank, part, k, f_part_k[X], f_part_k[Y]);
#        endif
   
         /* Add force in to total forces */
         loc_forces[loc_part][X] += f_part_k[X];
         loc_forces[loc_part][Y] += f_part_k[Y];
      }
   }
}  /* Compute_force */

/*---------------------------------------------------------------------
 * Function:  Update_part
 * Purpose:   Update the velocity and position for particle loc_part
 * In args:
 *    loc_part:    local index of the particle we're updating
 *    masses:      global array of particle masses
 *    loc_forces:  local array of total forces
 *    n:           total number of particles
 *    loc_n:       number of particles assigned to this process
 *    delta_t:     step size
 *
 * In/out args:
 *    loc_pos:     local array of positions
 *    loc_vel:     local array of velocities
 *
 * Note:  This version uses Euler's method to update both the velocity
 *    and the position.
 */
void Update_part(int loc_part, double masses[], vect_t loc_forces[], 
      vect_t loc_pos[], vect_t loc_vel[], int n, int loc_n, 
      double delta_t) {
   int part;
   double fact;

   part = my_rank*loc_n + loc_part;
   fact = delta_t/masses[part];
#  ifdef DEBUG
   printf("Proc %d > Before update of %d:\n", my_rank, part);
   printf("   Position  = (%.3e, %.3e)\n", 
         loc_pos[loc_part][X], loc_pos[loc_part][Y]);
   printf("   Velocity  = (%.3e, %.3e)\n", 
         loc_vel[loc_part][X], loc_vel[loc_part][Y]);
   printf("   Net force = (%.3e, %.3e)\n", 
         loc_forces[loc_part][X], loc_forces[loc_part][Y]);
#  endif
   loc_pos[loc_part][X] += delta_t * loc_vel[loc_part][X];
   loc_pos[loc_part][Y] += delta_t * loc_vel[loc_part][Y];
   loc_vel[loc_part][X] += fact * loc_forces[loc_part][X];
   loc_vel[loc_part][Y] += fact * loc_forces[loc_part][Y];
#  ifdef DEBUG
   printf("Proc %d > Position of %d = (%.3e, %.3e), Velocity = (%.3e,%.3e)\n",
         my_rank, part, loc_pos[loc_part][X], loc_pos[loc_part][Y],
               loc_vel[loc_part][X], loc_vel[loc_part][Y]);
#  endif
}  /* Update_part */
~~~
mpi_nbody_basic.c
{:.figure}

### mpi_nbody_red.c

~~~c
/* File:     mpi_nbody_red.c
 * Purpose:  Implement a 2-dimensional n-body solver that uses the 
 *           reduced algorithm.  In this version, we reduce storage 
 *           and communication over the original MPI version 
 *           and we slightly improve the organization of the loops 
 *           in Compute_proc_forces
 *
 * Compile:  mpicc -g -Wall -o mpi_nbody_red mpi_nbody_red.c -lm
 *           To turn off output (e.g., when timing), define NO_OUTPUT
 *           To get verbose output, define DEBUG
 *
 * Run:      mpiexec -n <number of processes> ./mpi_nbody_red
 *              <number of particles> <number of timesteps>  <size of timestep> 
 *              <output frequency> <g|i>
 *              'g': generate initial conditions using a random number
 *                   generator
 *              'i': read initial conditions from stdin
 *              number of particles should be evenly divisible by the number
 *                 of MPI processes
 *           A stepsize of 0.01 seems to work well with the automatically
 *           generated input.
 *
 * Input:    If 'g' is specified on the command line, none.  
 *           If 'i', mass, initial position and initial velocity of 
 *              each particle
 * Output:   If the output frequency is k, then position and velocity of 
 *              each particle at every kth timestep.  This value is
 *              ignored (but still necessary) if NO_OUTPUT is defined
 *
 *    for each timestep t {
 *       for each particle i I own
 *          compute F(i), the total force on i
 *       for each particle i I own
 *          update position and velocity of i using F(i) = ma
 *       Allgather positions
 *       if (output step) {
 *          Allgather velocities
 *          Output new positions and velocities
 *       }
 *    }
 *
 * Force:    The force on particle i due to particle k is given by
 *
 *    -G m_i m_k (s_i - s_k)/|s_i - s_k|^3
 *
 * Here, m_j is the mass of particle j, s_j is its position vector
 * (at time t), and G is the gravitational constant (see below).  
 *
 * Note that the force on particle k due to particle i is 
 * -(force on i due to k).  So we can approximately halve the number 
 * of force computations.  This version of the program attempts to
 * exploit this.
 *
 * Integration:  We use Euler's method:
 *
 *    v_i(t+1) = v_i(t) + h v'_i(t)
 *    s_i(t+1) = s_i(t) + h v_i(t)
 *
 * Here, v_i(u) is the velocity of the ith particle at time u and
 * s_i(u) is its position.
 *
 * Notes:
 * 1.  Each process stores the masses of all the particles:  the
 *     masses array had dimension n = number of particles.  This
 *     can be easily modified so that each process stores only
 *     n/p. 
 * 2.  This version uses a cyclic distribution of the particles.
 *
 * IPP:  Section 6.1.10 (pp. 292 and ff.)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <mpi.h>

#define DIM 2  /* Two-dimensional system */
#define X 0    /* x-coordinate subscript */
#define Y 1    /* y-coordinate subscript */

typedef double vect_t[DIM];  /* Vector type for position, etc. */

/* Global variables.  Except for vel all are unchanged after being set */
const double G = 6.673e-11;  /* Gravitational constant. */
                             /* Units are m^3/(kg*s^2)  */
int my_rank, comm_sz;
MPI_Comm comm;
MPI_Datatype vect_mpi_t;
MPI_Datatype cyclic_mpi_t;

/* Scratch arrays used by process 0 for I/O */
vect_t *vel = NULL;
vect_t *pos = NULL;

void Usage(char* prog_name);
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p);
void Build_cyclic_mpi_type(int loc_n);
void Get_init_cond(double masses[], vect_t loc_pos[], 
      vect_t loc_vel[], int n, int loc_n);
void Gen_init_cond(double masses[], vect_t loc_pos[], 
      vect_t loc_vel[], int n, int loc_n);
void Output_state(double time, double masses[], vect_t loc_pos[],
      vect_t loc_vel[], int n, int loc_n);
void Compute_forces(double masses[], vect_t tmp_data[], 
      vect_t loc_forces[], vect_t loc_pos[], int n, int loc_n);
void Compute_proc_forces(double masses[], vect_t tmp_data[], 
      vect_t loc_forces[], vect_t pos1[], int loc_n1, int rk1, 
      int loc_n2, int rk2, int n, int p);
int Local_to_global(int loc_part, int proc_rk, int proc_count);
int Global_to_local(int gbl_part, int proc_rk, int proc_count);
int First_index(int gbl1, int proc_rk1, int proc_rk2, int proc_count);
void Compute_force_pair(double m1, double m2, vect_t pos1, vect_t pos2,
      vect_t force1, vect_t force2);
void Update_part(int loc_part, double masses[], vect_t loc_forces[], 
      vect_t loc_pos[], vect_t loc_vel[], int n, int loc_n, double delta_t);

/*--------------------------------------------------------------------*/
int main(int argc, char* argv[]) {
   int n;                      /* Total number of particles     */
   int loc_n;                  /* Number of my particles        */
   int n_steps;                /* Number of timesteps           */
   int step;                   /* Current step                  */
   int output_freq;            /* Frequency of output           */
   double delta_t;             /* Size of timestep              */
   double t;                   /* Current Time                  */
   double* masses;             /* All the masses                */
   vect_t* loc_pos;            /* Positions of my particles     */
   vect_t* tmp_data;           /* Received positions and forces */
   vect_t* loc_vel;            /* Velocities of my particles    */
   vect_t* loc_forces;         /* Forces on my particles        */
   int loc_part;

   char g_i;                   /*_G_en or _i_nput init conds */
   double start, finish;       /* For timings                */

   MPI_Init(&argc, &argv);
   comm = MPI_COMM_WORLD;
   MPI_Comm_size(comm, &comm_sz);
   MPI_Comm_rank(comm, &my_rank);

   Get_args(argc, argv, &n, &n_steps, &delta_t, &output_freq, &g_i);
   loc_n = n/comm_sz;  /* n should be evenly divisible by comm_sz */
   masses = malloc(n*sizeof(double));
   tmp_data = malloc(2*loc_n*sizeof(vect_t));
   loc_forces = malloc(loc_n*sizeof(vect_t));
   loc_pos = malloc(loc_n*sizeof(vect_t));
   loc_vel = malloc(loc_n*sizeof(vect_t));
   if (my_rank == 0) {
      pos = malloc(n*sizeof(vect_t));
      vel = malloc(n*sizeof(vect_t));
   }
   MPI_Type_contiguous(DIM, MPI_DOUBLE, &vect_mpi_t);
   MPI_Type_commit(&vect_mpi_t);
   Build_cyclic_mpi_type(loc_n);

   if (g_i == 'i')
      Get_init_cond(masses, loc_pos, loc_vel, n, loc_n);
   else
      Gen_init_cond(masses, loc_pos, loc_vel, n, loc_n);

   start = MPI_Wtime();
#  ifndef NO_OUTPUT
   Output_state(0.0, masses, loc_pos, loc_vel, n, loc_n);
#  endif
   for (step = 1; step <= n_steps; step++) {
      t = step*delta_t;
      Compute_forces(masses, tmp_data, loc_forces, loc_pos, 
            n, loc_n);
      for (loc_part = 0; loc_part < loc_n; loc_part++)
         Update_part(loc_part, masses, loc_forces, loc_pos, loc_vel, 
               n, loc_n, delta_t);
#     ifndef NO_OUTPUT
      if (step % output_freq == 0)
         Output_state(t, masses, loc_pos, loc_vel, n, loc_n);
#     endif
   }
   
   finish = MPI_Wtime();
   if (my_rank == 0)
      printf("Elapsed time = %e seconds\n", finish-start);

   MPI_Type_free(&vect_mpi_t);
   MPI_Type_free(&cyclic_mpi_t);
   free(masses);
   free(tmp_data);
   free(loc_forces);
   free(loc_pos);
   free(loc_vel);
   if (my_rank == 0) {
      free(pos);
      free(vel);
   }

   MPI_Finalize();

   return 0;
}  /* main */

/*---------------------------------------------------------------------
 * Function: Usage
 * Purpose:  Print instructions for command-line and exit
 * In arg:   
 *    prog_name:  the name of the program as typed on the command-line
 */
void Usage(char* prog_name) {
   
   fprintf(stderr, "usage: mpiexec -n <number of processes> %s\n", prog_name);
   fprintf(stderr, "   <number of particles> <number of timesteps>\n");
   fprintf(stderr, "   <size of timestep> <output frequency>\n");
   fprintf(stderr, "   <g|i>\n");
   fprintf(stderr, "   'g': program should generate init conds\n");
   fprintf(stderr, "   'i': program should get init conds from stdin\n");
    
}  /* Usage */

/*---------------------------------------------------------------------
 * Function:  Get_args
 * Purpose:   Get command line args
 * In args:
 *    argc:            number of command line args
 *    argv:            command line args
 * Out args:
 *    n_p:             pointer to n, the number of particles
 *    n_steps_p:       pointer to n_steps, the number of timesteps
 *    delta_t_p:       pointer to delta_t, the size of each timestep
 *    output_freq_p:   pointer to output_freq, which is the number of
 *                     timesteps between steps whose output is printed
 *    g_i_p:           pointer to char which is 'g' if the init conds
 *                     should be generated by the program and 'i' if
 *                     they should be read from stdin
 */
void Get_args(int argc, char* argv[], int* n_p, int* n_steps_p, 
      double* delta_t_p, int* output_freq_p, char* g_i_p) {
   if (my_rank == 0) {
      if (argc != 6) {
         Usage(argv[0]);
         *n_p = *n_steps_p = *output_freq_p = 0;
         *delta_t_p = 0.0;
         *g_i_p = 'g';
      } else {
         *n_p = strtol(argv[1], NULL, 10);
         *n_steps_p = strtol(argv[2], NULL, 10);
         *delta_t_p = strtod(argv[3], NULL);
         *output_freq_p = strtol(argv[4], NULL, 10);
         *g_i_p = argv[5][0];
      }
   }
   MPI_Bcast(n_p, 1, MPI_INT, 0, comm);
   MPI_Bcast(n_steps_p, 1, MPI_INT, 0, comm);
   MPI_Bcast(delta_t_p, 1, MPI_DOUBLE, 0, comm);
   MPI_Bcast(output_freq_p, 1, MPI_INT, 0, comm);
   MPI_Bcast(g_i_p, 1, MPI_CHAR, 0, comm);

   if (*n_p <= 0 || *n_steps_p < 0 || *delta_t_p <= 0) {
      if (my_rank == 0 && argc > 6) Usage(argv[0]);
      MPI_Finalize();
      exit(0);
   }
   if (*g_i_p != 'g' && *g_i_p != 'i') {
      if (my_rank == 0) Usage(argv[0]);
      MPI_Finalize();
      exit(0);
   }
#  ifdef DEBUG
   if (my_rank == 0) {
      printf("n = %d\n", *n_p);
      printf("n_steps = %d\n", *n_steps_p);
      printf("delta_t = %e\n", *delta_t_p);
      printf("output_freq = %d\n", *output_freq_p);
      printf("g_i = %c\n", *g_i_p);
   }
#  endif
}  /* Get_args */

/*---------------------------------------------------------------------
 * Function:         Build_cyclic_mpi_type
 * Purpose:          Build an MPI derived datatype that can be used with
 *                   cyclically distributed data.
 * In arg:
 *    loc_n:         The number of elements assigned to each process
 * Global out:
 *    cyclic_mpi_t:  An MPI datatype that can be used with cyclically
 *                   distributed data
 */
void Build_cyclic_mpi_type(int loc_n) {
   MPI_Datatype temp_mpi_t;
   MPI_Aint lb, extent;

   MPI_Type_vector(loc_n, 1, comm_sz, vect_mpi_t, &temp_mpi_t);
   MPI_Type_get_extent(vect_mpi_t, &lb, &extent);
   MPI_Type_create_resized(temp_mpi_t, lb, extent, &cyclic_mpi_t);
   MPI_Type_commit(&cyclic_mpi_t);

}  /* Build_cyclic_mpi_type */

/*---------------------------------------------------------------------
 * Function:   Get_init_cond
 * Purpose:    Read in initial conditions:  mass, position and velocity
 *             for each particle
 * In args:  
 *    n:       total number of particles
 *    loc_n:   number of particles assigned to this process
 * Out args:
 *    masses:  global array of the masses of the particles
 *    loc_pos: local array of the positions of the particles assigned
 *             to this process
 *    loc_vel: local array of velocities assigned to this process.
 *
 * Global var:
 *    pos:     Scratch.  Used by process 0 for global positions
 *    vel:     Scratch.  Used by process 0 for global velocities
 */
void Get_init_cond(double masses[], vect_t loc_pos[],
     vect_t loc_vel[], int n, int loc_n) {
   int part;

   if (my_rank == 0) {
      printf("For each particle, enter (in order):\n");
      printf("   its mass, its x-coord, its y-coord, ");
      printf("its x-velocity, its y-velocity\n");
      for (part = 0; part < n; part++) {
         scanf("%lf", &masses[part]);
         scanf("%lf", &pos[part][X]);
         scanf("%lf", &pos[part][Y]);
         scanf("%lf", &vel[part][X]);
         scanf("%lf", &vel[part][Y]);
      }
   }
   MPI_Bcast(masses, n, MPI_DOUBLE, 0, comm);
   MPI_Scatter(pos, 1, cyclic_mpi_t, 
         loc_pos, loc_n, vect_mpi_t, 0, comm);
   MPI_Scatter(vel, 1, cyclic_mpi_t, 
         loc_vel, loc_n, vect_mpi_t, 0, comm);
}  /* Get_init_cond */

/*---------------------------------------------------------------------
 * Function:  Gen_init_cond
 * Purpose:   Generate initial conditions:  mass, position and velocity
 *            for each particle
 * In args:  
 *    n:       total number of particles
 *    loc_n:   number of particles assigned to this process
 * Out args:
 *    masses:  global array of the masses of the particles
 *    pos:     global array of positions
 *    loc_pos: local array of the positions of the particles assigned
 *             to this process
 *    loc_vel: local array of velocities assigned to this process.
 * Global vars:
 *    pos:     Scratch.  Used by process 0 for global positions
 *    vel:     Scratch.  Used by process 0 for global velocities
 *
 * Note:      The initial conditions place all particles at
 *            equal intervals on the nonnegative x-axis with 
 *            identical masses, and identical initial speeds
 *            parallel to the y-axis.  However, some of the
 *            velocities are in the positive y-direction and
 *            some are negative.
 */
void Gen_init_cond(double masses[], vect_t loc_pos[], 
      vect_t loc_vel[], int n, int loc_n) {
   int part;
   double mass = 5.0e24;
   double gap = 1.0e5;
   double speed = 3.0e4;

   if (my_rank == 0) {
//    srandom(1);
      for (part = 0; part < n; part++) {
         masses[part] = mass;
         pos[part][X] = part*gap;
         pos[part][Y] = 0.0;
         vel[part][X] = 0.0;
//       if (random()/((double) RAND_MAX) >= 0.5)
         if (part % 2 == 0)
            vel[part][Y] = speed;
         else
            vel[part][Y] = -speed;
      }
   }

   MPI_Bcast(masses, n, MPI_DOUBLE, 0, comm);
   MPI_Scatter(pos, 1, cyclic_mpi_t, 
         loc_pos, loc_n, vect_mpi_t, 0, comm);
   MPI_Scatter(vel, 1, cyclic_mpi_t, 
         loc_vel, loc_n, vect_mpi_t, 0, comm);
}  /* Gen_init_cond */

/*---------------------------------------------------------------------
 * Function:   Output_state
 * Purpose:    Print the current state of the system
 * In args:
 *    time:    current time
 *    masses:  global array of particle masses
 *    loc_pos: local array of particle positions
 *    loc_vel: local array of my particle velocities
 *    n:       total number of particles
 *    loc_n:   number of my particles
 * Global vars:
 *    pos:     Scratch.  Used by proc 0 for global positions
 *    vel:     Scratch.  Used by proc 0 for global velocities
 */
void Output_state(double time, double masses[], vect_t loc_pos[],
      vect_t loc_vel[], int n, int loc_n) {
   int part;

   MPI_Gather(loc_pos, loc_n, vect_mpi_t, pos, 1, cyclic_mpi_t, 
         0, comm);
   MPI_Gather(loc_vel, loc_n, vect_mpi_t, vel, 1, cyclic_mpi_t, 
         0, comm);
   if (my_rank == 0) {
      printf("%.2f\n", time);
      for (part = 0; part < n; part++) {
//       printf("%.3f ", masses[part]);
         printf("%3d %10.3e ", part, pos[part][X]);
         printf("  %10.3e ", pos[part][Y]);
         printf("  %10.3e ", vel[part][X]);
         printf("  %10.3e\n", vel[part][Y]);
      }
      printf("\n");
   }
}  /* Output_state */

/*---------------------------------------------------------------------
 * Function:       Compute_forces
 * Purpose:        Compute the total force on each local particle.
 *                 Exploit the symmetry (force on particle i due to 
 *                 particle k) = -(force on particle k due to particle i) 
 * In args:   
 *    masses:      global array of particle masses (dimension n)
 *    loc_pos:     local array of positions of my particles (dim loc_n)
 *    n:           total number of particles
 *    loc_n:       number of my particles
 * Scratch:
 *    tmp_data:    Stores received positions (subscripts 0 - loc_n-1)
 *                 and forces computed thus far on particles corresp
 *                 onding to received positions (subscripts 
 *                 loc_n - 2*loc_n-1).  (dimension 2*loc_n)
 * Out arg:
 *    loc_forces:  array of total forces acting on my particles
 */
void Compute_forces(double masses[], vect_t tmp_data[], 
      vect_t loc_forces[], vect_t loc_pos[], int n, int loc_n) {
   int src, dest;  /* Source and dest processes for particle pos */
   int i, other_proc, loc_part;
   MPI_Status status;

   src = (my_rank + 1) % comm_sz;
   dest = (my_rank - 1 + comm_sz) % comm_sz;
   memcpy(tmp_data, loc_pos, loc_n*sizeof(vect_t));
   memset(tmp_data + loc_n, 0, loc_n*sizeof(vect_t));
   memset(loc_forces, 0, loc_n*sizeof(vect_t));

   /* First compute the forces resulting from my particles' interactions 
    * with themselves */
   Compute_proc_forces(masses, tmp_data, loc_forces, loc_pos, loc_n, 
         my_rank, loc_n, my_rank, n, comm_sz);
   /* Now compute forces resulting from my particles' interactions with
    * other processes' particles */
   for (i = 1; i < comm_sz; i++) {
      other_proc = (my_rank + i) % comm_sz;
      MPI_Sendrecv_replace(tmp_data, 2*loc_n, vect_mpi_t, dest, 0, src, 0,
            comm, &status);
      Compute_proc_forces(masses, tmp_data, loc_forces, loc_pos, loc_n, 
            my_rank, loc_n, other_proc, n, comm_sz);
   }
   MPI_Sendrecv_replace(tmp_data, 2*loc_n, vect_mpi_t, dest, 0, src, 0,
         comm, &status);
   for (loc_part = 0; loc_part < loc_n; loc_part++) {
      loc_forces[loc_part][X] += tmp_data[loc_n+loc_part][X];
      loc_forces[loc_part][Y] += tmp_data[loc_n+loc_part][Y];
   }

}  /* Compute_forces */

/*---------------------------------------------------------------------
 * Function:       Compute_proc_forces
 * Purpose:        Compute the forces on particles owned by process
 *                 rk1 due to interaction with particles owned by
 *                 procss rk2.  Exploit the symmetry (force on particle 
 *                 i due to particle k) = -(force on particle k due 
 *                 to particle i) 
 * In args:   
 *    masses:      global array of particle masses (dim n)
 *    pos1:        local array of particle positions (dim loc_n1)
 *    loc_n1:      number of my particles in pos1
 *    rk1:         process owning particles in pos1
 *    loc_n2:      number of particles contributed by second process
 *    rk2:         process owning contributed particles 
 *    n:           total number of particles
 *    p:           number of processes in communicator containing
 *                 processes rk1 and rk2
 * In/out args:
 *    tmp_data:    positions of rk2 particles (in only, loc_n2 positions)
 *                 followed by forces computed thus far corresp to
 *                    rk2 particles (in and out, loc_n2 positions)
 *    loc_forces:  forces computed thus far on my particles (loc_n1)
 */
void Compute_proc_forces(double masses[], vect_t tmp_data[], 
      vect_t loc_forces[], vect_t pos1[], int loc_n1, int rk1, 
      int loc_n2, int rk2, int n, int p) {
   int loc_part1, loc_part2;
   int gbl_part1, gbl_part2;

   for (gbl_part1 = rk1, loc_part1 = 0;
        loc_part1 < loc_n1; 
        loc_part1++, gbl_part1 += p) {
      for(gbl_part2 = First_index(gbl_part1, rk1, rk2, p),
          loc_part2 = Global_to_local(gbl_part2, rk2, p); 
          loc_part2 < loc_n2; 
          loc_part2++, gbl_part2 += p) {
#        ifdef DEBUG
         printf("Proc %d > Current total force on part %d = (%.3e, %.3e)\n",
               my_rank, gbl_part1, loc_forces[loc_part1][X], 
               loc_forces[loc_part1][Y]);
         printf("Proc %d > Current total force on part %d = (%.3e, %.3e)\n",
               my_rank, gbl_part2, 
               tmp_data[loc_n2+loc_part2][X], 
               tmp_data[loc_n2+loc_part2][Y]);
#        endif
         Compute_force_pair(masses[gbl_part1], masses[gbl_part2], 
               pos1[loc_part1], tmp_data[loc_part2],
               loc_forces[loc_part1], tmp_data[loc_n2+loc_part2]);
#        ifdef DEBUG
         printf("Proc %d > Current total force on part %d = (%.3e, %.3e)\n",
               my_rank, gbl_part1, loc_forces[loc_part1][X], 
               loc_forces[loc_part1][Y]);
         printf("Proc %d > Current total force on part %d = (%.3e, %.3e)\n",
               my_rank, gbl_part2, 
               tmp_data[loc_n2+loc_part2][X], 
               tmp_data[loc_n2+loc_part2][Y]);
#        endif
      } /* for gbl_part2 */
   } /* for gbl_part1 */
}  /* Compute_proc_forces */

/*---------------------------------------------------------------------
 * Function:    Local_to_global
 * Purpose:     Convert a local particle index to a global particle
 *              index
 * In args: 
 *    loc_part:  local particle index
 *    proc_rk:   process rank
 *    loc_n:     number of particles assigned to the process
 *    n:         total number of particles
 *    proc_count:  number of processes in the communicator
 * Ret val:
 *    global particle index
 *
 * Notes:
 * 1.  This version assumes a cyclic distribution of the particles
 * 2.  It also assumes loc_n = n/proc_count, and n is evenly divisible
 *     by proc_count
 */
int Local_to_global(int loc_part, int proc_rk, int proc_count) {
   return loc_part*proc_count + proc_rk;
}  /*  Local_to_global */

/*---------------------------------------------------------------------
 * Function:    Global_to_local
 * Purpose:     Convert a global particle index to a global permuted
 *              index
 * In args:
 *    gbl_part:    The global particle index
 *    proc_rk:     The rank of the owning process
 *    proc_count:  The number of processes
 *    
 * Notes:
 * 1.  This version assumes a cyclic distribution of the particles
 * 2.  It also assumes loc_n = n/proc_count, and n is evenly divisible
 *     by proc_count
 */
int Global_to_local(int gbl_part, int proc_rk, int proc_count) {
   return (gbl_part - proc_rk)/proc_count;
}  /* Global_to_local */

/*---------------------------------------------------------------------
 * Function:           First_index
 * Purpose:            Given a global index glb1 assigned to process
 *                     rk1, find the next higher global index assigned
 *                     to process rk2
 * In args:
 *    gbl1:            global particle index of particle assigned to
 *                     process rk1
 *    rk1:             rank of process owning gbl1
 *    rk2:             rank of process owning particle with computed index
 *    proc_count:      number of processes
 * Return val:         next higher global particle index of particle assigned
 *                     to process rk2
 * Note:               If there is no particle assigned to rk2 with index
 *                     greater than rk1, the function will return a value
 *                     larger than n, the total number of particles.
 */
int First_index(int gbl1, int rk1, int rk2, int proc_count) {
   if (rk1 < rk2)
      return gbl1 + (rk2 - rk1);
   else 
      return gbl1 + (rk2 - rk1) + proc_count;
}  /* First_index */

/*---------------------------------------------------------------------
 * Function:           Compute_force_pair
 * Purpose:            Compute the force resulting from the interaction of
 *                     of two particles.  Exploit the fact that f_kq = -f_qk
 * In args:
 *    m1, m2:          Masses of the two particles
 *    pos1, pos2:      Positions of the two particles
 * In/out args:
 *    force1, force2:  The total forces on the two particles as thus far
 *                     computed 
 */
void Compute_force_pair(double m1, double m2, vect_t pos1, vect_t pos2,
      vect_t force1, vect_t force2) {
   double mg; 
   vect_t f_part_k;
   double len, len_3, fact;

   f_part_k[X] = pos1[X] - pos2[X];
   f_part_k[Y] = pos1[Y] - pos2[Y];
   len = sqrt(f_part_k[X]*f_part_k[X] + f_part_k[Y]*f_part_k[Y]);
   len_3 = len*len*len;
   mg = -G*m1*m2;
   fact = mg/len_3;
   f_part_k[X] *= fact;
   f_part_k[Y] *= fact;
   
   /* Add force in to total forces */
   force1[X] += f_part_k[X];
   force1[Y] += f_part_k[Y];
   force2[X] -= f_part_k[X];
   force2[Y] -= f_part_k[Y];
}  /* Compute_force_pair */

/*---------------------------------------------------------------------
 * Function:  Update_part
 * Purpose:   Update the velocity and position for particle loc_part
 * In args:
 *    loc_part:    local index of the particle we're updating
 *    masses:      global array of particle masses
 *    loc_forces:  local array of total forces
 *    n:           total number of particles
 *    loc_n:       number of particles assigned to this process
 *    delta_t:     step size
 *
 * In/out args:
 *    loc_pos:     local array of positions
 *    loc_vel:     local array of velocities
 *
 * Note:  This version uses Euler's method to update both the velocity
 *    and the position.
 */
void Update_part(int loc_part, double masses[], vect_t loc_forces[], 
      vect_t loc_pos[], vect_t loc_vel[], int n, int loc_n, 
      double delta_t) {
   int part;
   double fact;

   part = my_rank*loc_n + loc_part;
   fact = delta_t/masses[part];
#  ifdef DEBUG
   printf("Proc %d > Before update of %d:\n", my_rank, part);
   printf("   Position  = (%.3e, %.3e)\n", 
         loc_pos[loc_part][X], loc_pos[loc_part][Y]);
   printf("   Velocity  = (%.3e, %.3e)\n", 
         loc_vel[loc_part][X], loc_vel[loc_part][Y]);
   printf("   Net force = (%.3e, %.3e)\n", 
         loc_forces[loc_part][X], loc_forces[loc_part][Y]);
#  endif
   loc_pos[loc_part][X] += delta_t * loc_vel[loc_part][X];
   loc_pos[loc_part][Y] += delta_t * loc_vel[loc_part][Y];
   loc_vel[loc_part][X] += fact * loc_forces[loc_part][X];
   loc_vel[loc_part][Y] += fact * loc_forces[loc_part][Y];
#  ifdef DEBUG
   printf("Proc %d > Position of %d = (%.3e, %.3e), Velocity = (%.3e,%.3e)\n",
         my_rank, part, loc_pos[loc_part][X], loc_pos[loc_part][Y],
               loc_vel[loc_part][X], loc_vel[loc_part][Y]);
#  endif
}  /* Update_part */
~~~
mpi_nbody_red.c
{:.figure}
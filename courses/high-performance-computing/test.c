#include <stdio.h>
#include <stdlib.h>

int main(){
    double* a;
    a = malloc(1024*8 +8); // niz 1024 double vrednosti
    printf("%p\n", a);
    if((size_t)a %8 != 0){ // detektovano neporavnanje
        a = (double*)((((size_t)a >>3) << 3));
    }
    printf("%p\n", a);
    free(a);
}
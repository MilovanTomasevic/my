{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Hibridno programiranje](#hp)
- [Primer](#primer)
- [Prednosti](#prednosti)
- [Arhitekture](#arhitekture)
- [Gradivni elementi](#gradivni)
- [Klasifikacija](#klasifikacija)
- [Zadaci](#zadaci)

---
name: hp
class: center, middle

# Hibridno programiranje

---
layout: true

.section[[Hibridno programiranje](#sadrzaj)]

---
## Hibridno programiranje

- Podrazumeva kombinovano korišćenje više različitih programskih modela.
- U ovom slučaju to su OpenMP i OpenMPI kako bi se iskoristila dva različita nivoa paralelizma.

---

## Ciljna arhitektura

![](img/hibrid.png)

.footer.medium[
  [Detaljnije](http://pages.tacc.utexas.edu/~eijkhout/pcse/html/mpi-functional.html)

] 

---


## Kompajliranje hibridnih OpenMP-OpenMPI programa

- Pozicionirati se u direktorijum u kojem se nalazi izvorni kod hibridnog programa i pokrenuti:

```console
mpicc <izvorna_datoteka> -fopenmp
```

- Pokretanje:

```console
OMP_NUM_THREADS=<Nmp> \ mpiexec [-np <Nmpi>] <izvrsna_datoteka>
```

- `-np <Nmpi>` - opcija za zadavanje broja procesa OpenMPI procesa.
- `OMP_NUM_THREADS = <Nmp>` - maksimalan broj OpenMP niti po MPI procesu

---
layout: false
name: primer
class: center, middle

# Primer

---
layout: true

.section[[Primer](#sadrzaj)]

---


## Primer 1: Hello World!

```c
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
```

---

## MPI taksonimija interoperabilnosti niti
- Nivoi interoperabilnosti po standardu MPI 3.1:
	- `MPI_THREAD_SINGLE` - Samo jedna nit u MPI procesu.
	- `MPI_THREAD_FUNNELED` - MPI proces može imati više niti, ali MPI pozive može izvršavati samo glavna nit.
	- `MPI_THREAD_SERIALIZED` - MPI proces može imati više niti i sve niti mogu izvršavati MPI pozive, ali pozivi ne mogu biti izvršavani konkurentno iz dve različite niti, nego se serijalizuju.
	- `MPI_THREAD_MULTIPLE` - MPI proces može imati više niti, niti mogu izvršavati MPI pozive bez ograničenja.

- **Direktna razmena poruka podržana samo između procesa - ne može se eksplicitno adresirati nit.**

---

## MPI taksonimija interoperabilnosti niti

![](img/hibrid2.png)

---


## MPI taksonimija interoperabilnosti niti

Nemaju sve MPI implementacije isti nivo podrške za rad sa više niti. `MPI_init_thread`.ref[2] umesto `MPI_Init`..ref[1]
```c
int MPI_Init_thread(int *argc, char ***argv, int required, int *provided)
```
- (ulazni parametar)
```c
required := MPI_THREAD_SINGLE | MPI_THREAD_FUNNELED | MPI_THREAD_SERIALIZED | MPI_THREAD_MULTIPLE
```
- (izlazni parametar)
```c
provided := MPI_THREAD_SINGLE | MPI_THREAD_FUNNELED | MPI_THREAD_SERIALIZED | MPI_THREAD_MULTIPLE
```

.footer.medium[
<a target="_blank" rel="noopener noreferrer" href="https://www.open-mpi.org/doc/v3.1/man3/MPI_Init.3.php">1. MPI_Init</a><br>
<a target="_blank" rel="noopener noreferrer" href="https://www.open-mpi.org/doc/v3.1/man3/MPI_Init_thread.3.php">2. MPI_Init_thread</a>
] 

---

## Performanse hibridnog rešenja

<br><br><br><br>
> "Consider going hybrid only if pure MPI scalability is not satisfactory." .ref[*]


  
.footer[
\* Preuzeto iz knjige "Introduction to High Performance Computing for Scientists and Engineers" 
]

---

## Performanse hibridnog rešenja

<br><br><br>
- ... veoma zavise od broja procesa, broja niti u okviru procesa, MPI i MP implementacije, arhitekture na kojoj se hibridni program pokreće, same implementacije rešenja, itd. ...

---

## Prednosti i mane hibridnih rešenja


.lcol[

- Bolje iskorišćenje keša.
- Eksploatisanje dodatnih nivoa paralelizma u odnosu na čisto MPI rešenje.
- Smanjenje vremena izvršavanja preklapanjem komunikacije i računanja.
- ...
]

.rcol[

- MNOGO zahtevnije za pisanje više posla oko osmišljavanja rešenja, pisanja koda bez štetnog preplitanja, mnogo više potencijalnih mesta za pravljenje neefikasnog rešenja usled korišćenja dva različita programska modela.
- Često je nemoguće inkrementalno napraviti hibridno rešenje od nehibridnog rešenja - zahteva pisanje rešenja od početka.
- ...
]


---

## Alternativne tehnologije

- MPI za komunikaciju između čvorova, MPI 3.0 model za deljenu memoriju
- MPI za komunikaciju između čvorova, pthreads model za deljenu memoriju
- ...

---

layout: false
name: zadaci
class: center, middle

# Zadaci

---
layout: true

.section[[Zadaci](#sadrzaj)]

---

## Zadatak 1: Računanje broja π

- Implementirati čisto OpenMPI i hibridno OpenMP-OpenMPI rešenje za računanje broja π računanjem vrednosti integrala

![:scale 15%](img/integral.png)

- Sekvencijalna i OpenMP verzija programa su date u direktorijumu resenja.
	- Porediti vreme izvršavanja hibridnog rešenja sa vremenom izvršavanja OpenMP ubrzanog rešenja.
	- Meriti vreme izvršavanja hibridnog rešenja za različite kombinacije broja OpenMPI procesa i OpenMP niti.

.attention[
**Preporuka**: Implementirati OpenMPI verziju programa na osnovu sekvencijalnog rešenja, pa je proširiti OpenMP direktivama.
]


---

## Zadatak 2: Pretraga niza brojeva

- Implementirati sekvencijalno i hibridno OpenMPI-OpenMP rešenje za pretragu niza celih brojeva minimalne dužine milion elemenata.
- Elemente niza generisati nasumično iz intervala [-100, 100].
	- Meriti vreme izvršavanja hibridnog rešenja za različite kombinacije broja OpenMPI procesa i OpenMP niti.
	- Opciono implementirati čisto OpenMPI i čisto OpenMP rešenje i porediti performanse ovih rešenja porediti sa performnsama hibridnog rešenja

.attention[
**Preporuka**: Implementirati OpenMPI verziju programa na osnovu sekvencijalnog rešenja, pa je proširiti OpenMP direktivama.
]

---

## Zadatak 3: Množenje matrica - domaći

- Implementirati hibridno OpenMP-OpenMPI rešenje u C programskom jeziku za množenje dve kvadratne matrice na osnovu OpenMPI i OpenMP rešenja zadataka sa prethodnih vežbi.
- Pretpostaviti da jedan MPI proces distribuira delove matrice preostalim procesima. Kostur rešenja koji je potrebno popuniti se nalazi u direktrijumu MatrixMultiplicationHybrid.
	- Rezultujuću matricu sačuvati u h5 formatu u datoteci pod nazivom result<nxn>.h5, gde se <nxn> menja dimenzijama matrice koja predstavlja rešenje.
	- Meriti vreme izvršavanja hibridnog, OpenMP i OpenMPI rešenja i zabeležiti ih u priloženu datoteku statistika.csv.

---

## Zadatak 3: Množenje matrica - domaći

- Meriti vreme izvršavanja hibridnog rešenja za različite kombinacije broja MPI procesa i OpenMP niti. U slučaju da se rešenje isprobava na računaru sa soketom i više jezgara, probati sledeće kombinacije:
	- Po jedan MPI proces za svako logičko jezgro
	- Po jedan MPI proces za svako fizičko jezgro i po jedna nit za svako logičko jezgro.
	- Jedan MPI proces i po jedna nit za svako logičko jezgro.

- Po želji dodati još različitih konfiguracija i rezultate upisati u statistika.csv. Analizirati dobijene rezultate.
- Pri analizi performansi rešenja može pomoći poglavlje 11 knjige "Introduction to high performance computing for Scientists and Engineers."


---

layout: false

## Materijali

Georg Hager, Gerhard Wellein, "Introduction to High Performance Computing for Scientists and Engineers"
[MPI 3.1 standard, poglavlje 12.4](https://www.mpi-forum.org/docs/mpi-3.1/mpi31-report.pdf)
[OpenMP dokumentacija](https://www.open-mpi.org/doc/)
[OpenMP SC13 Tutorial: Hybrid MPI and OpenMP Parallel Programming](https://www.openmp.org/press-release/sc13-tutorial-hybrid-mpi-openmp-parallel-programming/)


{% endblock %}
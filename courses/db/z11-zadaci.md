{% extends "base_slides.md" %}
{% block slides %}

name: danas 
class: center, middle
layout: false

# Zadaci za danas

---
layout: true

.section[[Zadaci za danas](#sadrzaj)]

---

## Prvi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 1: 
    - Za sve studente čije ime počinje na slovo P i rođeni su između februara i jula, izdvojiti podatke o položenim ispitima. 
    - Izdvojiti indeks, ime i prezime studenta, naziv predmeta, dobijenu ocenu i kategoriju položenog predmeta. Položen predmet spada u kategoriju:
      - obavezan, ako je obavezan predmet na smeru koji student studira
      - izborni, ako nije obavezan predmet na smeru koji student studira.
- Primer 2: 
    - Napisati okidač koji sprečava brisanje studenata čiji status nije ispisan.
]
]
            



---

## Drugi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 3: 
    - Napraviti okidač koji dozvoljava ažuriranje broja bodova predmetima samo za jedan bod. 
    - Ako je nova vrednost bodova veća od postojeće, broj bodova se povećava za 1, a ako je manja smajuje se za 1.
- Primer 4: 
    - Napraviti tabelu broj_predmeta koja ima jednu kolonu broj (tipa smallint) i u nju uneti jedan entitet koji predstavlja broj predmeta u tabeli predmet. 
    - Napisati okidač koji ažurira tabelu broj_predmeta tako što povećava vrednosti u koloni broj za 1 kada se unese novi predmet u tabelu predmet. 
    - Napisati okidač koji ažurira tabelu broj_predmeta tako što smanjuje vrednost u koloni broj za 1 kada se obriše predmet iz tabelepredmet.
]
]



---

## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 5: 
    - Napisati naredbu na SQL-u koja:
      - pravi tabelu predmet_student koja čuva podatke koliko studenata je položilo koji predmet. Tabela ima kolone: id_predmeta (tipa integer) i student (tipa smallint).
      - unosi u tabelu predmet_student podatke o obaveznim predmetima na smeru Informatika na osnovnim akademskim studijama (može se uzeti da je id_smera 201). Za svaki predmet uneti podatak da ga je položilo 5 studenata.
      - napisati naredbu koja ažurira tabelu predmet_student, tako što predmetima o kojima postoji evidencija ažurira broj studenata koji su ga položili, a za predmete o kojima ne postoji evidencija unosi podatke.
]
]


---
## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 6: 
    - Napisati naredbu na SQL-u koja:
      - pravi tabelu student_podaci sa kolonama: indeks (tipa integer), broj _predmeta (tipa smallint), prosek (tipa float) i dat_rodjenja (tipa date).
      - u tabelu student_podaci unosi indeks, broj položenih predmeta i prosek za studente koji imaju prosek iznad 8 i za studente koji su diplomirali. Za studente koji su diplomirali kao broj predmeta uneti vrednost 10, a kao prosek vrednost 10.
      - ažurira tabelu student_podaci tako što studentima o kojima u tabeli postoje podaci i koji su:
      - -diplomirali ažurira datum rođenja
      - -trenutno na budžetu ažurira broj položenih predmeta i prosek.
    - Naredba podatke o studentima koji su se ispisali briše iz tabele, a unosi podatke o studentima koji se nisu ispisali i o njima ne postoje podaci u tabeli student_podaci. Za studente o kojima nema podataka uneti indeks, broj položenih predmeta i prosek.
]
]





---
## Peti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 7: 
    - Napisati naredbu SQL-a koja:
      - kreira korisnički definisan tip prosek nad tipom float
      - kreira tabelu prosek koja od kolona ima indeks (tipa integer) i prosek (tipa prosek). Kolona indeks je primarni ključ i postoji strani ključ koji se sastoji od kolone indeks i koji referiše na tabelu dosije, a akcija pri brisanju iz bazne tabele je CASCADE.
      - definiše funkciju prosek koja za studenta čiji se broj indeksa prosleđuje računa trenutni prosek.
      - unosi u tabelu prosek podatke o svim studentima.
      - briše iz tabele prosek podatke o studentima koji nisu upisali nijednu školsku godinu.
      - kreir okidač novi_ispit koji se aktivira nakon unošenja novog ispita. Ako je uneti ispit položen, za studenta koji je položio ispit okidač ažurira prosek u tabeli prosek.
      - za studenta sa indeksom 208/2007 unosi podatke o položenom ispitu sa identifikatorom 635. Student je predmet upisao u školskoj godini 2007/2008 u prvom semestru, ispit je prijavljen automatski za januarski ispitni rok 2007. godine, dana 2.2.2007. Ispit je održan 15.2.2007, i student je dobio 85 bodova i ocenu 9.
]
]



---

layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu


{% endblock %}
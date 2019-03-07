{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Uvod](#uvod)
- [Rešiti na relacionom računu](#rel)
- [Rešiti na relacionoj algebri i relacionom računu](#relal)
- [Zadaci za vežbu](#vezba)

---
name: uvod 
class: center, middle, inverse

# Uvod

---
layout: true

.section[[Uvod](#sadrzaj)]

---

## Uvod 

- Rešiti na relacionom računu
- Rešiti na relacionoj algebri i relacionom računu

---
name: rel 
class: center, middle, inverse
layout: false

# Zadaci za danas
#### Rešiti na relacionom računu

---
layout: true

.section[[Rešiti na relacionom računu](#sadrzaj)]

---

## Prvi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 1: 
    - Prikazati šifru i naziv predmeta.
- Primer 2: 
    - Prikazati podatke o predmetima koji imaju po 6 kredita.
- Primer 3: 
    - Izdvojiti ime i prezime studenta sa indeksom 25/2010.
- Primer 4: 
    - Za svakog studenta izdvojiti predmete koje je polagao. 
    - Izdvojiti indeks studenta, naziv predmeta i ocenu koju je dobio.
- Primer 5: 
    - Izdvojiti parove predmeta koji imaju isti broj kredita. 
    - Izdvojiti šifre i nazive predmeta.
]
]

---

## Drugi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 6: 
    - Izdvojiti šifre i nazive predmeta koje je položio student sa indeksom 26/2010.
- Primer 7: 
    - Izdvojiti indekse studenata koji su polagali sve predmete.
- Primer 8: 
    - Pronaci nazive predmeta koji imaju po 6 kredita i koje je polagao student sa prezimenom Vukovic.
- Primer 9: 
    - Pronaci indekse studenata koji su položili bar sve predmete koje je položio student sa indeksom 25/2010.
- Primer 10: 
    - Pronaci indeks, ime i prezime studenta koji je položio samo Programiranje 1.

]
]

---

name: relal 
class: center, middle, inverse
layout: false

# Zadaci za danas
#### Rešiti na relacionoj algebri i relacionom računu

---
layout: true

.section[[Rešiti na relacionoj algebri i relacionom računu](#sadrzaj)]

---

## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 11: 
    - Pronaci predmet sa najvecim brojem kredita. 
    - Izdvojiti naziv i broj kredita predmeta.
- Primer 12: 
    - Pronaci studente koji su položili neki predmet sa 6 kredita. 
    - Izdvojiti indeks, ime, prezime i naziv predmeta.
- Primer 13: 
    - Pronaci studenta koji je u jednoj godini položio sve predmete. 
    - Izdvojiti godinu i indeks.
- Primer 14: 
    - Pronaci studente koji su predmet sa identifikatorom 4002 polagali tacno dva puta.

]
]

---
## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 15: 
    - Pronaci predmete koje su položili dva studenta rodjena iste godine. 
    - Izdvojiti godinu i naziv predmeta.
- Primer 16 : 
    - Pronaci studenta koji:
        - je položio sve predmete od 6 kredita
        - je položio neki predmet od 6 kredita ali ne i sve predmete od 6 kredita
        - nije položio sve predmete od 6 kredita.
]
]

---

name: relal 
class: center, middle, inverse
layout: false

# Zadaci za vežbu

---
layout: true

.section[[Zadaci za vežbu](#sadrzaj)]

---

## Zadaci

.message.is-info[
.message-header[
Zadatak
]
.message-body[
1. Izdvojiti nazive predmetima čiji je broj kredita izmeĎu 5 i 10.
1. Izdvojiti indeks i naziv predmeta, takve da je student polagao predmet i da je dobio ocenu koja je jednaka broju kredita predmeta.
1. Pronaći studente koji su u januarskom ispitnom roku 2010. godine dobili ocenu 9 ili 10. Izdvojiti indeks, ime i prezime studenta, naziv predmeta i ocenu.
1. Pronaći indekse studenata koji nisu polagali Analizu 2.
1. Izdvojiti nazive predmeta koje su položili svi studenti koji su upisali fakultet 2010. godine.
1. Izdvojiti nazive predmeta koje su studenti roĎeni u Čačku položili u aprilu 2010.
]
]

---

layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu

---

class: center, middle, theend
layout: false
background-image: url(/../theend.gif)

{% endblock %}
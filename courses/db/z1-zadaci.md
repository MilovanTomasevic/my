{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Uvod](#uvod)
- [Zadaci za danas](#danas)
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

- <a target="_blank" rel="noopener noreferrer" href="../db/sema.html"> ☛ `Šema baze podataka`</a>

---
name: danas 
class: center, middle, inverse
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
    - Prikazati šifru i naziv predmeta.
- Primer 2: 
    - Prikazati podatke o predmetima koji imaju po 6 kredita.
- Primer 3: 
    - Izdvojiti ime i prezime studenta sa indeksom 25/2010.
- Primer 4: 
    - Izdvojiti nazive rokova koji su održani posle 2009. godine.
- Primer 5: 
    - Izdvojiti indekse studenata koji imaju:
        - ocenu 10 ili 9
        - ocenu 10 i 9
        - samo ocene 10.
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
    - Pronaći studente koji su rođeni u godini kada je održan neki ispitni rok.
    - Izdvojiti indeks, godinu rođenja i naziv roka.
- Primer 7: 
    - Za svakog studenta izdvojiti predmete koje je polagao. 
    - Izdvojiti indeks studenta, naziv predmeta i ocenu koju je dobio.
- Primer 8: 
    - Izdvojiti indekse studenata koji su polagali sve predmete.
- Primer 9: 
    - Izdvojiti parove predmeta koji imaju isti broj kredita. Izdvojiti šifre i nazive predmeta.
- Primer 10: 
    - Izdvojiti indekse studenata koji su položili predmet Geometrija.
]
]

---

## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[

- Primer 11: 
    - Izdvojiti podatke o studentima koji su polagali u januarsokm ispitnom roku 2011.
- Primer 12: 
    - Izdvojiti podatke o predmetima koje je položio bar jedan student rodjen 1992. godine.
- Primer 13: 
    - Izdvojiti podatke o studentima koji nisu polagali ispite u januarskom ispitnom roku.
- Primer 14: 
    - Za svaki predmet prikazati njegove podatke i koliko košta njegovo upisivanje za samofinansirajuće studente. Jedan kredit košta 1500 din.
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
    - Za svaku godinu izračunati koliko studenata je rođeno te godine.
- Primer 16 : 
    - Za svakog studenta i godinu u kojoj su održani ispitni rokovi prikazati koliko predmeta je položio i prosečnu ocenu.
- Primer 17: 
    - Pronaći ispitni rok u kome su bar jedan ispit polagali svi studenti.
- Primer 18: 
    - Pronaći studente koji su polozili neki predmet od 6 kredita. 
    - Izdvojiti indeks, ime, prezime i naziv predmeta.
]
]

---

layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu

--

class: center, middle, theend, hide-text
layout: false
background-image: url(../theend.gif)

{% endblock %}
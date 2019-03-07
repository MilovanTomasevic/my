{% extends "base_slides.md" %}
{% block slides %}

name: danas 
class: center, middle , inverse
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
    - Za svakog studenta izdvojiti predmete koje je položio. 
    - Prikazati indeks, ime i prezime studenta, naziv predmeta i ocenu.
- Primer 2: 
    - Izdvojiti podatke o studentima i ispitnim rokovima za koje važi da je student rođen godine kada je održan ispitni rok.
- Primer 3: 
    - Prikazati podatke o ispitima čiji je datum nepoznat.
- Primer 4: 
    - Prikazati parove predmeta koji imaju isti broj bodova.
- Primer 5: 
    - Izdvojiti podatke o predmetima koje je položio neki student sa ocenom 10 u nekom ispitnom roku održanom u toku 2011. godini
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
    - Za svaki predmet izdvojiti godinu i oznaku ispitnog roka u kojem je predmet polagao neki student. 
    - Izdvojiti naziv ispitnog roka, godinu i oznaku ispitnog roka.
- Primer 7: 
    - Za svaki ispitni rok izdvojiti naziv roka i ocene koje su dobijene u tom roku. 
    - Rezultat urediti prema nazivu ispitnog roka.
- Primer 8: 
    - Izdvojiti parove student-ispitni rok takve da je student rođen u godini kada je održan ispitni rok. 
    - Izdvojiti indeks i godinu rođenja studenta, naziv i godinu ispitnog roka. 
    - Prikazati i studente i ispitne rokove koji nemaju odgovarajuće podatke.
]
]

---

## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 9: 
    - Izdvojiti nazive predmeta koje je polagao student sa indeksom 22/2010.
- Primer 10: 
    - Izdvojiti indekse studenata koji su položili bar jedan predmet koji nije položio student sa indeksom 22/2010.
- Primer 11: 
    - Izdvojiti nazive predmeta koje je položio student sa indeksom 22/2010.
- Primer 12: 
    - Pronaći naziv predmeta koji su polagali svi studenti.
]
]

---
## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 13: 
    - Izdvojiti indekse studenata koji su polagali sve predmete od 8 bodova.
- Primer 14: 
    - Pronaći studente koji su polagali u svim ispitnim rokovima.
- Primer 15: 
    - Pronaći predmete sa najvećim brojem bodova.
- Primer 16 : 
    - Izdvojiti sve studente osim najstarijih.
- Primer 17: 
    - Izdvojiti studente čije prezime sadrži slovo a na 4. poziciji i završava na c i koji imaju ocene 6, 8 ili 10 iz predmeta čija je šifra u intervalu [M105, P103].
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
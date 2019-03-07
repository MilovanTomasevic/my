{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Uvod](#uvod)
- [Zadaci za danas](#danas)

---
name: uvod 
class: center, middle

# Uvod

---
layout: true

.section[[Uvod](#sadrzaj)]

---

## Uvod 

.message.is-warning[
.message-header[
Info
]
.message-body[
- <a target="_blank" rel="noopener noreferrer" href="../db/sema.html"> ☛ `Šema baze podataka`</a>
- <a target="_blank" rel="noopener noreferrer" href="../db-mySQL.sql"> ☛ `Skripta`</a>

]
]

---
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
    - Prikazati podatke o svim predmetima.
- Primer 2: 
    - Prikazati podatke o svim studentima rođenim u Beogradu.
- Primer 3: 
    - Izdvojiti gradove u kojima su rođeni studenti.
- Primer 4: 
    - Izdvojiti nazive predmeta koji imaju više od 6 bodova.
- Primer 5: 
    - Izdvojiti šifre i nazive predmeta koji imaju između 8 i 15 bodova.
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
    - Izdvojiti imena i prezimena studenata koji su rođeni 1989, 1992 ili 1988 godine.
- Primer 7: 
    - Izdvojiti imena i prezimena studenata koji nisu rođeni 1989, 1992 ili 1988 godine.
- Primer 8: 
    - Izdvojiti nazive predmeta i njihovu cenu za samofinansirajuće studente izraženu u dinarima. Jedan bod košta 1500 dinara.
- Primer 9: 
    - Izdvojiti nazive predmeta i njihovu cenu za samofinansirajuće studente izraženu u dinarima. Jedan bod košta 1500 dinara. Između kolone naziv i kolone cena dodati kolonu u kojoj će za svaku vrstu biti ispisanoCena u dinarima.
]
]

---

## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 10: 
    - Prikazati podatke o studentima koji su rođeni u mestu čiji naziv
      - sadrži malo slovo o;
      - sadrži o kao drugo slovo;
      - se završava sa e;
      - počinje sa N a završava sa d.
- Primer 11: 
    - Prikazati podatke o predmetima. Rezultat urediti po bodovima
      - u rastućem poretku;
      - u opadajućem poretku;
      - u rastućem poretku i po nazivu u opadajućem poretku.
- Primer 12: 
    - Prikazati ime, prezime i godinu rođenja studenata koji su rođeni između 1987. i 1992. godine i urediti rezultat prema prezimenu studenta.

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
    - Prikazati naziv ispitnog roka koji je održan između 2008. i 2011. godine i koji u oznaci sadrži slovo p. 
    - Rezultat urediti prema nazivu u opadajućem poretku.
- Primer 14: 
    - Prikazati podatke o ispitima čiji je datum nepoznat.
- Primer 15: 
    - Prikazati podatke o studentima i ispitima.
- Primer 16 : 
    - Prikazati podatke o studentima i njihovim ispitima koji su održani 4.3.2011. Izdvojiti indeks, ime i prezime studenta, id predmeta i ocenu.
]
]

---

## Peti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 17: 
    - Prikazati nazive predmeta koje je polagao neki student u januarskom ispitnom roku 2011. godine.
- Primer 18: 
    - Za svakog studenta izdvojiti predmete koje je položio. Prikazati indeks, ime i prezime studenta, naziv predmeta i ocenu.
- Primer 19: 
    - Izdvojiti podatke o studentima i ispitnim rokovima za koje važi da je student rođen godine kada je održan ispitni rok.
]
]

---

layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu

{% endblock %}
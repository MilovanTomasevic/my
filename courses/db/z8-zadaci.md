{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Zadaci za danas](#danas)
- [Zadaci za vežbu](#vezba)

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
    - Napraviti tabelu `polozeni_predmeti` u kojoj ce se nalaziti podaci o položenim predmetima studenata. 
    - Tabela ima iste kolone kao i tabela ispit.
- Primer 2: 
    - Iz tabele `polozeni_predmeti` ukloniti kolonu `datum_ispita` i dodati uslov da se u tabeli mogu nalaziti samo podaci o studentima koji su fakultet upisali 2010. godine i da je podrazumevana ocena 6.
- Primer 3: 
    -  Ukloniti tabelu `polozeni_predmeti`.
]
]
            

---

## Drugi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 4: 
    - Napraviti tabelu student_ispiti koja od kolona ima:
      - indeks – indeks studenta
      - polozeni_ispiti – broj položenih ispita
      - prosek – prosek studenta
    - Definisati primarni ključ i strani ključ na tabelu dosije.
- Primer 5: 
    - Tabeli `student_ispiti` dodati kolonu `broj_ispita` koja predstavlja broj polaganih ispita. 
    - Dodati i ograničenje da broj polaganih ispita mora biti veći ili jednak od broja položenih ispita.
- Primer 6: 
    - U tabelu `student_ispiti` uneti podatke na osnovu podataka u tabeli `ispit`.
]
]

---
## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 7: 
    - Napraviti indeks nad tabelom `student_ispit` nad kolonama `indeks` i `prosek`.
- Primer 8: 
    - Napraviti pogled `ispitnirok_predmeti` koji prikazuje u kom ispitnom roku koji predmet je polagalo koliko studenata. 
    - Izdvojiti naziv ispitnog roka, naziv predmeta i broj polaganih ispita.
- Primer 9: 
  - Za svakog studenta izdvojiti: indeks, broj različitih predmeta koje je polagao, broj različitih ocena koje je dobio, broj ispita koje je polagao, broj ispita koje je položio, najveću ocenu koju je dobio i prosek. 
  - Rezultat urediti prema broju ispita.
]
]

---

## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 10: 
  -  Za svakog studenta koji je položio izmedu 15 i 25 kredita (bodova) i čije ime sadrži slovo o ili a izdvojiti indeks, ime, prezime, broj predmeta koje je polagao, broj predmeta koje je položio i prosečnu ocenu. 
  -  Rezultat urediti prema indeksu.
- Primer 11: 
  - Pronaći poslednji položeni ispit za svakog studenta koji ima prosek iznad 7 i koji ima između 20 i 25 godina.
- Primer 12: 
  - Pronaći studenta koji ima najviše položenih bodova.
]
]

---

## Peti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 13: 
    - Ako godišnje položi 60 bodova, koliko godina je potrebno studentu sa indeksom 27/2010 da položi predmete koje još nije položio. 
    - Rezultat zaokružti na ceo broj.
- Primer 14: 
    - Pronaći studenta koji je je u aprilsom roku 2011. godine dobio samo ocene 9.
- Primer 15: 
    - Izdvojiti naziv ispitnog roka u kome su polagali svi studenti rođeni 1992. godine.

]
]

---

name: vezba 
class: center, middle, inverse
layout: false

# Zadaci za vežbu

---
layout: true

.section[[Zadaci za vežbu](#sadrzaj)]

---

## Prvi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 1: 
    - Za svakog studenta izdvojiti kog dana u nedelji je polagao poslednji ispit i koliko ispita je položio. 
    - Za studente koji nisu polagali ispite umesto dana u nedelji ispisati nije polagao, a kao broj ispita 0.
- Primer 2: 
    - Za svaki ispitni rok koji u svom nazivu sadrži slovo n i u kome je polagalo više od 5 studenata, izdvojiti naziv ispitnog roka, najmanju ocenu dobijenu u tom ispitnom roku, najveću ocenu dobijenu u tom ispitnom roku, i broj studenata koji su polagali u tom ispitnom roku.
- Primer 3: 
  - Izdvojiti predmet sa najmanjim brojem bodova koji je položio student sa indeksom 22/2010. 
  - Izdvojiti naziv predmeta, ocenu koju je dobio student sa indeksom 22/2010 iz tog predmeta i datum kada je položen.

]
]

---

## Drugi deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 4: 
    - Za svakog studenta rođenog u Beogradu ili Valjevu i koji ima prosek između 6 i 9, izračunati koliko je dana prošlo od poslednjeg položenog ispita. 
    - Izdvojiti indeks studenta i broj dana od poslednjeg položenog ispita.
- Primer 5: 
    - Izdvojiti parove predmeta koje je položio student sa indeksom 25/2010 u istom ispitnom roku. 
    - Izdvojiti nazive predmeta, datume kada su položeni i ocene koje je student dobio iz tih predmeta.
]
]

---
## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 6: 
    - Za svaki ispit izračunati koliko je vremena prošlo od njegovog održavanja. 
    - Posebno izračunati koliko je prošlo:
      - godina
      - meseci
      - dana
      - godina, meseci, dana u obliku ggggmmdd
      - ukupno meseci
      - ukupno dana.
- Primer 7: 
    - Izdvojiti naziv predmeta koji je polagan u svakom ispitnom roku koji u svom nazivu sadrži slovo p.
]
]

---
## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 8: 
    - Izdvojiti parove predmeta koji imaju po 6 bodova i koje nije položio student sa indeksom 25/2010.
- Primer 9: 
  - Za svakog studenta koji je položio više od tri ispita, izdvojiti najmanju ocenu, najveću ocenu, prosečnu ocenu i ukupan broj položenih bodova. 
  - Prosečnu ocenu prikazati sa tri decimalne cifre. 
  - Rezultat urediti prema broju položenih bodova.
- Primer 10: 
  -  Izdvojiti naziv predmeta koji je položio samo jedan student.
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
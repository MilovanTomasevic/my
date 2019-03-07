{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Zadaci za danas](#danas)
- [Zadaci za vežbu](#vezba)

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
    - Izdvojiti indekse studenata koji su
      - rođeni u Beogradu ili imaju ocenu 10. Rezultat urediti u opadajućem poretku.
      - rođeni u Beogradu i imaju ocenu 10. Rezultat urediti u opadajućem poretku.
      - rođeni u Beogradu i nemaju ocenu 10. Rezultat urediti u opadajućem poretku.
- Primer 2: 
    - Za svakog studenta izdvojiti broj ispita koje je polagao. 
    - Izdvojiti indeks studenta i broj ispita koje je polagao.
- Primer 3: 
    -  Za svaki ispit izdvojiti indeks, id_predmeta i dobijenu ocenu. 
    -  Vrednost ocene ispisati i slovima. 
    -  Ako je predmet nepoložen umesto ocene ispisati nepoložen.

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
    - Klasifikovati predmete prema broju bodova na sledeći način:
      - ako predmet ima više od 7 bodova tada pripada I kategoriji
      - ako predmet ima bodova u intervalu [5,7] pripada II kategoriji
      - inače predmet pripada III kategoriji.
    - Izdvojiti naziv predmeta i kategoriju.
- Primer 5: 
    - Prebrojati koliko predmeta pripada svakoj kategoriji iz prethodnog zadatka.
- Primer 6: 
    - Izračunati koliko studenata je položilo više od 10 bodova.
- Primer 7: 
    - Za studenta koji ima ocenu 8 ili 9 izračunati iz koliko ispita je dobio ocenu 8 i iz koliko ispita je dobio ocenu 9. Izdvojiti indeks studenta, broj ispita iz kojih je student dobio ocenu 8, broj ispita iz kojih je student dobio ocenu 9.
]
]

  
---
## Treći deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 8: 
    - U tabelu dosije uneti novog studenta Marka Markovica sa indeksom 27/2010, koji je rođen 1990. godine u Kragujevcu.
- Primer 9: 
  - Uneti u bazu podatke o predmetima:
    - Uvod u arhitekturu računara, koji ima šifru P112, 6 bodova i identifikator 2005;
    - Razvoj softvera, koji ima šifru P116, 6 bodova i identifikator 2006.
- Primer 10: 
  -  Uneti podatke o polaganju ispita iz predmeta Programiranje 2 za studente rođene 1991. godine. 
  -  Studenti su polagali u junskom ispitnom roku i svi dobili ocenu 9.
]
]

---

## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 11: 
  - Iz baze izbrisati studente rođene 1990. godine.
- Primer 12: 
  - Iz baze izbrisati ispite u kojima je polagan predmet Programiranje 2 ili predmet koji ima 15 bodova.
- Primer 13: 
    - Svim predmetima cija šifra počinje sa P povećati broj bodova za 20%.
- Primer 14: 
    - Svim studentima koji su u januaru 2011. godine polagali Analizu 2 promeniti rok u jun 2011. 
    - Kao datum polaganja staviti da je nepoznat.

]
]

---
## Peti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 15: 
    - Predmetima koje su polagali studenti iz Beograda postaviti broj bodova na najveći broj bodova koji postoji u tabeli predmet.
- Primer 16: 
  -  Izdvojiti parove ispitni rok–predmet, takve da je predmet polagan u ispitnom roku. 
  -  Izdvojiti i ispitne rokove i predmete koji nemaju odgovarajućeg para.
- Primer 17: 
    - Za svakog studenta koji je položio izmedu 15 i 25 bodova i čije ime sadrži slovo o ili a izdvojiti indeks, ime, prezime, broj predmeta koje je polagao, broj predmeta koje je položio i prosečnu ocenu. Rezultat urediti prema indeksu.
]
]

---

name: vezba 
class: center, middle
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
    - Izdvojiti ukupan broj studenata i maksimalni broj indeksa studenta iz tabele dosije.
- Primer 2: 
    - Odrediti ukupan broj studenata kojima je poznata godina rođenja i broj različitih vrednosti za godinu rođenja.
- Primer 3: 
  - Prikazati ukupan broj položenih ispita studenta sa brojem indeksa 22/2010.
- Primer 4: 
    - Izdvojiti ukupan broj studena koji su bar jedan ispit položili sa ocenom 8.
- Primer 5: 
    - Za svakog od studenata izdvojiti broj indeksa i ukupan broj sakupljenih bodova.
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
    - Za svakog studenta koji je skupio bar 20 bodova prikazati ukupan broj skupljenih bodova.
- Primer 7: 
    - Za svakog studenta izračunati trenutni prosek ocena.
- Primer 8: 
    - Za svaki od ispitnih rokova i za svaki polagan predmet naći broj položenih ispita.
- Primer 9: 
  - Izdvojiti id predmeta koji ili nose više od 6 bodova ili ih je polagao student čiji broj indeksa je 20100024.
- Primer 10: 
  -  Izdvojiti id predmeta koji su polagani i u januaru 2011 i u februaru 2011.
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
  - Izdvojiti sve identifikatore za predmete koje položio student sa brojem indeksa 20100021, a nije položio student sa indeksom 20100025, sortirane u opadajućem poretku.
- Primer 12: 
  - Izdvojiti brojeve indeksa studenata koji su položili barem 3 ispita i id predmeta koje su položila barem tri studenta. 
  - Sve to uradi u jednom upitu i rezultat urediti u opadajućem poretku broja ispita/studenata.
- Primer 13: 
    - Izdvojiti sve informacije za predmete i uz svaki od njih ispisati `lak` ako predmet nosi manje od 6 bodova, `srednje tezak` ako nosi 6 ili 7 bodova i `tezak` ako nosi bar 8 bodova
]
]

.
---

## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[

- Primer 14: 
    - Izdvojiti sva polaganja predmeta Programiranje 1 i uz svako od njih u zavisnosti od ocena izdvojiti `pao` ako je ocena 5, `provukao se` ako je ocena 6, inače `polozio`.
- Primer 14: 
    - Za svakog studenta koji je položio više od 30 kredita (bodova) i čije prezime ne sadrži slovo o izdvojiti indeks, mesto rođenja, broj predmeta koje je polagao ali pao u koloni `Broj neuspesnih`, broj predmeta koje je položio u koloni `Broj uspesnih` i prosečnu ocenu u koloni `Prosek`. 
    - Rezultat urediti prema proseku opadajuce.

]
]

---

layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu

{% endblock %}
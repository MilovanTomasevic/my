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
            
- Primer 1: 
    - Izdvojiti ukupan broj studenata.
- Primer 2: 
    - Izdvojiti ukupan broj studenata koji bar iz jednog predmeta imaju ocenu 10.
- Primer 3: 
    - Izdvojiti ukupan broj položenih predmeta i položenih bodova za studenta sa indeksom 25/2010.
- Primer 4: 
    - Izlistati ocene dobijene na ispitima i ako je ocena jednaka 5 ispisati NULL
- Primer 5: 
    - Koliko ima različitih ocena dobijenih na ispitu a da ocena nije 5.

---

## Drugi deo

- Primer 6: 
    - Izdvojiti šifre, nazive i bodove predmeta čiji je broj bodova veći od prosečnog broja bodova svih predmeta.
- Primer 7: 
    - Za svaki predmet izračunati koliko studenata ga je položilo.
- Primer 8: 
    - Za svakog studenta rođenog 1992. godine, koji ima bar jedan položen ispit, izdvojiti broj indeksa, prosečnu ocenu, najmanju i najveću ocenu.
- Primer 9: 
  - Za svaku godinu ispitnog roka i predmet pronaći najveću ocenu. 
  - Izdvojiti godinu roka, naziv predmeta i najveću ocenu.
- Primer 10: 
  -  Izdvojiti predmete koje je polagalo više od 5 različitih studenata.
  
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


- Primer 11: 
  - Za svakog studenta izdvojiti broj indeksa i mesec u kome je položio više od dva ispita (nije važno koje godine). 
  - Izdvojiti indeks studenta, ime meseca i broj položenih predmeta. 
  - Rezultat urediti prema broju indeksa i mesecu polaganja.
- Primer 12: 
  - Primer 12: Za svaki rok koji održan 2011. godine i u kome nema neuspešnih polaganja ispita, izdvojiti oznaku roka, broj položenih ispita u tom roku i broj studenata koji su položili ispite u tom roku.

---
## Drugi deo

- Primer 13: 
    - Za svaki ispitni rok izdvojiti naziv ispitnog roka, najveću ocenu dobijenu u tom ispitnom roku i ime i prezime studenta koji je dobio tu ocenu. 
    - Ime i prezime studenta napisati u jednoj koloni. Za ispitne rokove u kojima nije bilo ispita, kao ime i prezime studenta ispisati nema, a kao ocenu 0.
- Primer 14: 
    - Prikazati naziv predmeta koji je položio samo student Milos Peric.
- Primer 15: 
    - Izdvojiti parove studenata čija imena počinju na slovo M i za koje važi da su bar dva ista predmeta položili u istom ispitnom roku.

---

layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu


{% endblock %}
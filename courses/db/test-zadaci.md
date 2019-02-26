{% extends "base_slides.md" %}
{% block slides %}

name: sadrzaj

# Sadržaj

- [Test](#test)
- [Zadaci za vežbu](#vezba)

---
name: test 
class: center, middle

# Test

---
layout: true

.section[[Test](#sadrzaj)]

---

## Zadatak 1

.medium[
- Napisati na SQL-u upit koji:
  - izračunava izveštaj o uspešnosti završavanja kurseva na smeru Informatika u školskoj godini 2006/2007. Smatrati da je kurs završen ako je položen u istoj školskoj godini. Izdvojiti: šifru predmeta, naziv predmeta, semestar u kome je kurs organizovan, broj studenata koji su upisali kurs, broj studenata koji su ga uspešno završili, procenat uspešnosti. Izveštaj urediti po uspešnosti u opadajućem poretku.
  - izdvaja studente sa osnovnih akademskih studija koji su u školskoj 2007/2008. godini ponovo upisali neki obavezan predmet za koji nisu položili sve uslovne predmete. Izdvojiti naziv smera, indeks, ime i prezime studenta, naziv obaveznog predmeta koji su upisali 2007/2008. školske godine, a upisivali su ga i ranije, i naziv uslovnog predmeta za taj obavezan predmet koji student još nije položio. Rezultat urediti prema nazivu smera u opadajućem poretku i indeksu studenta.
]

---

## Zadatak 2

.medium[
- Napisati naredbu SQL-a koja:
  - kreira korisnički definisan tip rsd nad tipom float.
  - definiše funkciju iznosskolarine koja kao parametar dobija broj upisanih bodova i izračunava iznos školarine na osnovu broja upisanih bodova. Svaki upisani bod košta 1200 rsd. Tip vrednosti koju vraća funkcija je rsd.
  - pravi tabelu skolarina sa kolonama: indeks (tipa integer), godina (tipa smallint), bodova (tipa integer), iznos (tipa rsd) i izmireno (tipa rsd). Definisati primarni ključ.
  - koristeći funkciju iznosskolarine u tabelu skolarina unosi podatke o studentima koji su školsku 2010/2011. godinu upisali kao samofinansirajući studenti. Uneti broj indeksa, školsku godinu, broj upisanih bodova i iznos školarine.
  - modifikuje sadržaj tabele skolarina tako da sadrži podatke o studentima koji su upisali više od 40 bodova u nekoj školskoj godini u kojoj su bili na samofinansiranju. Uneti podatke do 2010/2011. školske godine. Za studente i godine o kojima postoje podaci u tabeli skolarina ažurirati vrednost kolone izmireno da bude jednaka vrednosti kolone iznos, a za studente i godine o kojima nema podataka uneti indeks, godinu, bodove i iznos koristeći funkciju iznosskolarine.
]

---

## Zadatak 3


- Napisati rekurzivan SQL upit koji za svaki obavezan predmet na smeru Informatika izdvaja predmete koji moraju da se polože pre polaganja obaveznog predmeta i nose po 6 bodova. 
- Izdvojiti naziv obaveznog predmeta i naziv uslovnog predmeta. Može se koristiti podatak da je identifikator smera Informatika 201.


---
name: vezba 
class: center, middle
layout: false

# Zadaci za vežbu

---
layout: true

.section[[Zadaci za vežbu](#sadrzaj)]


---

## Zadatak 1

- Napisati naredbu SQL-a koja definiše pogled koji prikazuje podatke o svim studentima koji su položili sve upisane predmete u godini u kojoj su bili na samofinansiranju. Izdvojiti indeks, ime i prezime studenta, školsku godinu, broj bodova koje su upisali u toj školskoj godini i iznos školarine. Može da se koristi tabela skolarina.


---

## Zadatak 2

- Napisati naredbu SQL-a koja definiše okidač skolarinabodovi koji pri promeni vrednosti bodava u tabeli skolarina ažurira i vrednost iznosa primenom funkcije iznosskolarine.

---

## Zadatak 3

.medium[
- Napisati upit na SQL-u koji izračunava podatke o uspešnosti studiranja u školskoj godini 2006/2007. 
- Potrebno je izdvojiti broj i procenat studenata (u odnosu na ukupan broj studenata koji su upisali tu šk.god.) koji su položili sve upisane predmete, 
- broj i procenat studenata kojima je ostalo od 1 do 6 nepoloženih ESPB, 
- broj i procenat studenata kojima je ostalo od 7 do 12 nepoloženih ESPB, 
- broj i procenat studenata kojima je ostalo od 13 do 18 nepoloženih ESPB, 
- broj i procenat studenata kojima je ostalo od 19 do 23 nepoloženih ESPB, 
- broj i procenat studenata kojima je ostalo od 24 do 30 nepoloženih ESPB, 
- broj i procenat studenata kojima je ostalo više od 30 nepoloženih ESPB.

]

---
layout: false

## Korišćeni materijal

- Katedra za računarstvo i informatiku, Matematički fakultet, Univerzitet u Beogradu


{% endblock %}
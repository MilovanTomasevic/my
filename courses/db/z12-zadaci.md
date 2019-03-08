{% extends "base_slides.md" %}
{% block slides %}

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
    - Pronaći sve predmete koji moraju da se polože pre polaganja predmeta Razvoj softvera.
- Primer 2: 
  -  Pronaći predmete koji moraju da se polože pre polaganja predmeta koji su uslovni za Razvoj softvera.
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
    - Za sve studente osnovnih studija izdvojiti podatke o količini ispunjenih obaveza. 
    - Izdvojiti broj indeksa, oznaku smera, ukupan broj bodova potrebnih za završetak studija, ukupan broj bodova iz položenih predmeta, procenat položenosti bodova, ukupan broj bodova koje nose obavezni predmeti, ukupan broj bodova koje nose položeni obavezni predmeti, procenat položenosti bodova koje nose položeni predmeti.
    - Izveštaj urediti po procentu položenosti bodova.
]
]

---

## Treći deo
.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 4: 
    - Napisati na SQL-u upit koji izračunava statistiku o polaganju ispita u rokovima održanim od 2005. do 2009. godine po predmetima. 
    - Izdvojiti naziv roka, naziv predmeta, broj studenata koji su prijavili ispit iz tog predmeta u tom roku, koliko studenata ga je položilo, koji je procenat studenata koji ga je položio u odnosu na broj prijavljenih, koliko studenata je poništilo dobijenu ocenu, koji je to procenat u odnosu na broj studenata koji su ga prijavili i prolaznost rangirati prema procentu položenosti (uzimajući u obzir i studente koji su poništili ispit) kao:
      - odlična - ako je prolaznost veća od 70%
      - srednja - ako je prolaznost između 40% i 70%
      - loša - ako je manja od 40%
    - Rezultat ureditii prema rangu.
]
]

---

## Četvrti deo
.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 5: 
    - Napisati upit na SQL-u koji za sve studente koji su položili sve uslovne predmete obaveznih predmeta na njihovom smeru, a još uvek nisu sakupili dovoljno bodova da bi stekli uslov za sticanje zvanja, izdvaja: broj indeksa, ime i prezime studenta, naziv smera, ukupan broj bodova koji se odnosi na još uvek nepoložene obavezne predmete. 
    - Izveštaj urediti u rastućem redosledu po ukupnom broju bodova još uvek nepoloženih obaveznih predmeta.
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
    - Napisati naredbu SQL-a koja:
      - studentima osnovnih akademskih studija koji su upisali 2008/2009. školsku godinu ažurira broj upisanih bodova na ukupan broj bodova upisanih kurseva, a datum upisa je 20. septembar 2008.
      - studentima osnovnih akademskih studija koji su upisali 2008/2009. školsku godinu ažurira broj overenih kredita na broj kredita koji su položili u toj školskoj godini, a datum overe je 5. septembar 2009.
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
    - Napisati naredbu za pravljenje okidača koji se aktivira pre unošenja novih podataka u tabelu ispit. Okidač obezbeđuje da ocena koja se unosi odgovara broju bodova koje je student osvojio na ispitu. Ako je student osvojio broj bodova:
      -  u intervalu (90,101) upisuje se ocena 10
      - u intervalu (80,91) upisuje se ocena 9
      - u intervalu (70,81) upisuje se ocena 8
      - u intervalu (60,71) upisuje se ocena 7
      - u intervalu (51,61) upisuje se ocena 6
      - u intervalu (0,51) upisuje se ocena 5
      - inače se upisuje NULL vrednost u kolonu ocena.
]
]

---
## Šesti deo
.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 8: 
    - Napisati naredbu SQL-a koja:
      - definiše korisnički definisan tip rsd nad tipom float.
      - definiše funkciju iznosskolarine koja kao parametar dobija broj upisanih bodova i izračunava iznos školarine na osnovu broja upisanih bodova. Svaki upisani bod košta 1200 rsd.
      - pravi tabelu skolarina sa kolonama: indeks (tipa integer), godina (tipa smallint), bodova (tipa integer), iznos (tipa rsd), izmireno (tipa rsd). Definisati primarni ključ.
      - koristeći funkciju iznosskolarine u tabelu skolarina unosi podatke o studentima koji su školsku 2008/2009. godinu upisali kao samofinansirajući studenti. Uneti broj indeksa, školsku godinu, broj upisanih kredita i iznos školarine.
      - modifikuje sadržaj tabele skolarina tako da sadrži podatke o studentima koji su upisali više od 40 bodova u nekoj školskoj godini u kojoj su bili na samofinansiranju. Uneti podatke do 2010/2011 školske godine. Za studente i godine o kojima postoje podaci u tabeli skolarina ažurirati vrednosti kolone izmireno da bude jednaka vrednosti kolone iznos, a za studente i godine o kojima nema podataka uneti indeks, godinu, bodove i iznos koristeći funkciju iznosskolarine.
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
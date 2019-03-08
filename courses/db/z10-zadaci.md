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
    - Napraviti korisnički definisani tip INDEKS nad tipom INTEGER.
- Primer 2: 
    - Napraviti tabelu DOSIJE1 koja ima kolone:
      - INDEKS tipa INDEKS
      - ID_SMERA tipa INTEGER
      - STATUS tipa VARCHAR(20)
      - IME tipa VARCHAR(50)
      - PREZIME tipa VARCHAR(50)
      - DAT_UPISA tipa DATE
    - Kolonu INDEKS definisati kao primarni ključ i definisati strani ključ na tabelu SMER.
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
    - Tabelu DOSIJE1 napuniti podacima iz tabele DOSIJE.
- Primer 4: 
    - Sabrati indekse 20060001 i 20060005 iz tabele DOSIJE1.
- Primer 5: 
    - Napraviti funkciju godinaupisa koja izdvaja godinu upisa studenta iz indeksa.
- Primer 6: 
    - Napraviti funkciju brojindeksa koja izdvaja broj indeksa studenta bez godine upisa.
- Primer 7: 
    - Definisati agregatnu funkciju MAX za tip INDEKS.
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
    - Napisati naredbu SQL-a koja:
      - definiše korisnički definisan tip bodovi nad tipom smallint.
      - definiše funkciju obaveznibodovi koja kao parametar dobija id smera, a vraća ukupan broj bodova (tipa bodovi ) obaveznih predmeta na tom smeru.
      - definiše tabelu polozenobodova koja od kolona ima:
        - -indeks, tipa integer
        - -polozenobodova, tipa bodovi
    - Kolona indeks je primaran ključ.
      - u tabelu polozenobodova unosi podatke o studentima koji su položili sve obavezne predmete na smeru na kome studiraju.
      - definiše pogled koji prikazuje broj indeksa, ime i prezime studenta, naziv smera koji student studira, broj položenih bodova iz obaveznih predmeta i ukupan broj bodova svih obaveznih predmeta na smeru koji studira. Koristiti tabelu polozenobodova i funkciju obaveznibodovi.
]
]

---
## Četvrti deo

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Primer 9: 
    - Napisati upit na SQL-u koji za školsku 2006/2007. i svaki smer osnovnih studija izračunava koliki je procenat studenata koji su te godine upisali fakultet, upisan upravo na taj smer, kao i koja je prosečna ocena na smeru za tu generaciju te školske godine. Izdvojiti oznaku i naziv smera, ukupan broj upisanih studenata na fakultet te godine, kao i prosečnu ocenu smera u toj generaciji. Izveštaj urediti po prosečnoj oceni.
- Primer 10: 
    - Napisati naredbu SQL jezika koja:
      - svim studentima smera Informatika koji imaju položenih 180 ili više ESPB ažurira status u "diplomirao".
      - briše podatke iz tabele Ispit koji se odnose na školsku 2008/2009. godinu svim studentima koji imaju status "mirovanje".
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
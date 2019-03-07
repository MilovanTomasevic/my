---
layout: page
title: Z3-Rešenja
description: >
  Baze podataka - rešenje zadataka
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Primer 1

Prikazati podatke o svim predmetima.

```sql
select * from predmet;
```

## Primer 2

Prikazati podatke o svim studentima rođenim u Beogradu.

```sql
select * from dosije where mesto_rodjenja='Beograd';
```

## Primer 3

Izdvojiti gradove u kojima su rođeni studenti.

```sql
select mesto_rodjenja from dosije;

-- Izlistaće i duplikate... Da bismo to izbegli, koristimo distinct.
select distinct mesto_rodjenja from dosije;
```

## Primer 4

Izdvojiti nazive predmeta koji imaju više od 6 bodova.

```sql
select naziv from predmet where bodovi>6;
```

## Primer 5

Izdvojiti šifre i nazive predmeta koji imaju između 8 i 15 bodova.

```sql
select sifra, naziv from predmet where bodovi between 8 and 15;
```

## Primer 6

Izdvojiti imena i prezimena studenata koji su rođeni 1989, 1992 ili 1988 godine.

```sql
select ime, prezime from dosije where god_rodjenja=1989 or god_rodjenja=1992 or god_rodjenja=1998;

-- Ili, korišćenjem predikata IN:
select ime, prezime from dosije where god_rodjenja in (1989, 1992, 1998);

```

## Primer 7

Izdvojiti imena i prezimena studenata koji nisu rođeni 1989, 1992 ili 1988 godine.

```sql
select ime, prezime from dosije where god_rodjenja not in (1989, 1992, 1998);

--Ili
select ime, prezime from dosije where not god_rodjenja in (1989, 1992, 1998);
```

## Primer 8

Izdvojiti nazive predmeta i njihovu cenu za samofinansirajuće studente izraženu u dinarima. 
Jedan bod košta 1500 dinara.

```sql
select naziv, bodovi*1500 CENA from predmet; 

select naziv, bodovi*1500 as CENA from predmet;
```

## Primer 9

Izdvojiti nazive predmeta i njihovu cenu za samofinansirajuće studente izraženu u dinarima. 
Jedan bod košta 1500 dinara. Između kolone naziv i kolone cena dodati kolonu u kojoj će za svaku vrstu biti ispisano Cena u dinarima.

```sql
select naziv, 'Cena u dinarima', bodovi*1500 from predmet;
```

## Primer 10

Prikazati podatke o studentima koji su rođeni u mestu čiji naziv:

```sql
-- sadrži malo slovo o;
select * from dosije where mesto_rodjenja like '%o%';

-- sadrži o kao drugo slovo;
select * from dosije where mesto_rodjenja like '_o%';

-- se završava sa e;
select * from dosije where mesto_rodjenja like '%o';

-- počinje sa N a završava sa d.
select * from dosije where mesto_rodjenja like 'N%d';
```

## Primer 11

Prikazati podatke o predmetima. Rezultat urediti po bodovima

```sql
-- u rastućem poretku;
select * from predmet order by bodovi;
select * from predmet order by bodovi asc;

-- u opadajućem poretku;
select * from predmet order by bodovi desc;

--u rastućem poretku i po nazivu u opadajućem poretku.
select * from predmet order by bodovi asc, naziv desc;
```

## Primer 12

Prikazati ime, prezime i godinu rođenja studenata koji su rođeni između 1987. i 1992. godine i urediti rezultat prema prezimenu studenta.

```sql
select ime, prezime, god_rodjenja from dosije
where god_rodjenja between 1987 and 1992 order by prezime;
```

## Primer 13

Prikazati naziv ispitnog roka koji je održan između 2008. i 2011. godine i koji u oznaci sadrži slovo p. 
Rezultat urediti prema nazivu u opadajućem poretku.

```sql
select naziv
from ispitni_rok
where godina_roka between 2008 and 2011 and oznaka_roka like '%p%' order by naziv desc;
```

## Primer 14

Prikazati podatke o ispitima čiji je datum nepoznat.

```sql
select * from ispit where datum_ispita is null;
```

## Primer 15

Prikazati podatke o studentima i ispitima.

```sql
select * from dosije d join ispit i on d.indeks = i.indeks;
```

## Primer 16

Prikazati podatke o studentima i njihovim ispitima koji su održani 4.3.2011. 
Izdvojiti indeks, ime i prezime studenta, id predmeta i ocenu.

```sql
select i.indeks, ime, prezime, id_predmeta, ocena 
from dosije d join ispit i on d.indeks = i.indeks 
where datum_ispita='04/03/2011';
```

## Primer 17

Prikazati nazive predmeta koje je polagao neki student u januarskom ispitnom roku 2011. godine.

```sql
select naziv
from predmet p join ispit i on i.id_predmeta=p.id_predmeta 
where godina_roka=2011 and oznaka_roka='jan';
```

## Primer 18

Za svakog studenta izdvojiti predmete koje je položio. 
Prikazati indeks, ime i prezime studenta, naziv predmeta i ocenu.

```sql
select i.indeks, ime, prezime, naziv, ocena
from dosije d join ispit i on d.indeks=i.indeks 
join predmet p on p.id_predmeta=i.id_predmeta
where ocena>5;
```

## Primer 19

Izdvojiti podatke o studentima i ispitnim rokovima za koje važi da je student rođen godine kada je održan ispitni rok.

```sql
select *
from dosije d 
join ispitni_rok ir on d.god_rodjenja=ir.godina_roka;
```
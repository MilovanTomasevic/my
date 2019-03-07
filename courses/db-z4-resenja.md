---
layout: page
title: Z4-Rešenja
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

Za svakog studenta izdvojiti predmete koje je položio. 
Prikazati indeks, ime i prezime studenta, naziv predmeta i ocenu.

```sql
select d.indeks, ime, prezime, naziv, ocena
from ispit i 
join predmet p on p.id_predmeta = i.id_predmeta 
join dosije d on d.indeks=i.indeks
where ocena>5;
```

## Primer 2

Izdvojiti podatke o studentima i ispitnim rokovima za koje važi da je student rođen godine kada je održan ispitni rok.

```sql
select *
from ispitni_rok ir 
join dosije d on d.god_rodjenja=ir.godina_roka;
```

## Primer 3

Prikazati podatke o ispitima čiji je datum nepoznat.

```sql
select *
from ispit
where datum_ispita is null;
```

## Primer 4

Prikazati parove predmeta koji imaju isti broj bodova.

```sql
select px.sifra, py.sifra, px.bodovi
from predmet as px, predmet as py
where px. bodovi =py. bodovi and px.id_predmeta<py.id_predmeta;
```

## Primer 5

Izdvojiti podatke o predmetima koje je položio neki student sa ocenom 10 u nekom ispitnom roku održanom u toku 2011. godine.

```sql
select p.*
from predmet p join ispit i on p.id_predmeta=i.id_predmeta 
where ocena=10 and godina_roka=2011;
```

## Primer 6

Za svaki predmet izdvojiti godinu i oznaku ispitnog roka u kojem je predmet polagao neki student. 
Izdvojiti naziv ispitnog roka, godinu i oznaku ispitnog roka.

```sql
-- Napomena: probati i upit:
select p.naziv, i.godina_roka, i.oznaka_roka
from predmet p 
left outer join ispit i on p.id_predmeta=i.id_predmeta;

-- Napomena: probati i upit:
select p.naziv, i.godina_roka, i.oznaka_roka
from ispit i 
right outer join predmet p on p.id_predmeta=i.id_predmeta;
```

## Primer 7

Za svaki ispitni rok izdvojiti naziv roka i ocene koje su dobijene u tom roku.

```sql
select distinct naziv, ocena
from ispitni_rok ir 
left outer join ispit i on ir.godina_roka=i.godina_roka and ir.oznaka_roka=i.oznaka_roka
order by naziv; -- moglo je i order by 1;
```

## Primer 8

Izdvojiti parove student-ispitni rok takve da je student rođen u godini kada je održan ispitni rok. 
Izdvojiti indeks i godinu rođenja studenta, naziv i godinu ispitnog roka. 
Prikazati i studente i ispitne rokove koji nemaju odgovarajuće podatke.

```sql
select indeks, god_rodjenja, naziv, godina_roka
from dosije d 
full outer join ispitni_rok ir on d.god_rodjenja=ir.godina_roka; 

--Napomena: probati i sa left outer join i sa right outer join i uporedite rezultate upita.
```

## Primer 9

Izdvojiti nazive predmeta koje je polagao student sa indeksom 22/2010.

```sql
-- I način :
select naziv
from predmet p 
join ispit i on p.id_predmeta=i.id_predmeta 
where indeks=20100022;

-- II način :
from ispit
where indeks=20100022);

--III način :
select naziv
from predmet
where 20100022 in 
    (select indeks
    from ispit
    where id_predmeta=predmet.id_predmeta);
```

## Primer 10

Izdvojiti indekse studenata koji su položili bar jedan predmet koji nije položio student sa indeksom 22/2010.

```sql
select distinct indeks
from ispit
where ocena>5 and id_predmeta not in (select id_predmeta
    from ispit
    where ocena>5 and indeks=20100022);
```

## Primer 11

Izdvojiti nazive predmeta koje je položio student sa indeksom 22/2010.

```sql
select naziv
from predmet
where exists (select *
    from ispit
    where ispit.id_predmeta=predmet.id_predmeta and ocena>5 and indeks=20100022);

select naziv
from predmet
where id_predmeta in (select id_predmeta
    from ispit
    where ocena>5 and indeks=20100022);
```

## Primer 12

Pronaći naziv predmeta koji su polagali svi studenti.

```sql
select naziv
from predmet p
where not exists (select *
    from dosije d
    where not exists(select *
        from ispit
        where id_predmeta=p.id_predmeta and indeks=d.indeks));

-- Nije pogrešno ni naglasiti da je podatak iz neke tabele (npr. ispit u ovom slučaju...):
select naziv
from predmet p
where not exists (select *
    from dosije d
    where not exists ( select *
        from ispit i
        where i.id_predmeta=p.id_predmeta and d.indeks=i.indeks));

```

## Primer 13

Izdvojiti indekse studenata koji su polagali sve predmete od 8 bodova.

```sql
--IMPLIKACIJA P=>Q je isto kao NOT P OR Q

P: Predmet ID ima 8 bodova
Q: Predmet ID je polagao student S

FORALL ID (P=>Q)
FORALL ID (NOT P OR Q)
NOT EXISTS ID (NOT(NOT P OR Q)) NOT EXISTS ID ( P AND NOT Q)
    select indeks 
    from dosije d
    where not exists (select * from predmet p
        where bodovi = 8 and not exists(select * from ispit i
            where i.indeks=d.indeks and i.id_predmeta=p.id_predmeta)
        );
```

## Primer 14

Pronaći studente koji su polagali u svim ispitnim rokovima.

```sql
select indeks
from dosije d
where not exists ( select *
    from ispitni_rok ir
    where not exists ( select *
        from ispit i
        where i.indeks=d.indeks and i.godina_roka=ir.godina_roka
              and ir.oznaka_roka=i.oznaka_roka));
```

## Primer 15

Pronaći predmete sa najvećim brojem bodova.

```sql
select *
from predmet
where bodovi >= all (select bodovi from predmet);
```

## Primer 16

Izdvojiti sve studente osim najstarijih.

```sql
select *
from dosije
where not god_rodjenja <= all(select god_rodjenja from dosije);

select *
from dosije
where god_rodjenja > any(select god_rodjenja from dosije);
```

## Primer 17

Izdvojiti studente čije prezime sadrži slovo a na 4. poziciji i završava na c i koji imaju ocene 6, 8 ili 10 iz predmeta čija je šifra u intervalu [M105, P103].

```sql
select dosije.*
from dosije 
join ispit on dosije.indeks=ispit.indeks
join predmet on predmet.id_predmeta=ispit.id_predmeta 
where prezime like '___a%c' and ocena in (6, 7, 10) and sifra between 'M105' and 'P103';
```
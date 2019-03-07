---
layout: page
title: Z7-Rešenja
description: >
  Baze podataka - rešenje zadataka
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Zadaci za danas
### Primer 1

```sql
--a
select indeks
from dosije
where mesto_rodjenja='Beograd' union
select indeks
from ispit
where ocena=10
order by indeks desc;

--b
select indeks
from dosije
where mesto_rodjenja='Beograd' intersect
select indeks
from ispit
where ocena=10
order by indeks desc;

--c
select indeks
from dosije
where mesto_rodjenja='Beograd' except
select indeks
from ispit
where ocena=10
order by indeks desc;
```

### Primer 2

```sql
select d.indeks, count(*) br_ispita
from dosije d join ispit i on d.indeks=i.indeks group by d.indeks
union
select indeks, 0
from dosije d
where not exists ( select *
    from ispit i
    where d.indeks=i.indeks);
```

### Primer 3

```sql
select indeks, id_predmeta, ocena, case
    when ocena=10 then 'deset' 
    when ocena=9 then 'devet' 
    when ocena=8 then 'osam' 
    when ocena=7 then 'sedam' 
    when ocena=6 then 'sest' 
    else 'nepolozen'
    end as rezultat_ispita
from ispit;

-- ili
select indeks, id_predmeta, ocena, case ocena
    when 10 then 'deset' 
    when 9 then 'devet' 
    when 8 then 'osam' 
    when 7 then 'sedam' 
    when 6 then 'sest' 
    else 'nepolozen'
    end as rezultat_ispita
from ispit;

```

### Primer 4

```sql
select naziv, case
    when bodovi>7 then 'I kat' 
    when bodovi>4 then 'II kat' 
    else 'III kat'
    end as kategorija 
from predmet;
```

### Primer 5

```sql
select kategorija, count(*) from (select naziv, case
    when bodovi>7 then 'I kat' 
    when bodovi>4 then 'II kat' 
    else 'III kat'
    end as kategorija 
  from predmet) as a
group by kategorija;

-- ili
with predmet_kategorija (predmet, kategorija) as 
  ( select naziv, case
      when bodovi>7 then 'I kat' 
      when bodovi>4 then 'II kat' 
      else 'III kat'
      end as kategorija from predmet)
select kategorija, 
count(*) 
from predmet_kategorija 
group by kategorija;

```

### Primer 6

```sql
with student_bodovi as (
select indeks, sum(bodovi) pol_bodovi
from ispit i join predmet p on i.id_predmeta=p.id_predmeta
where ocena>5
group by indeks)
select count(*) br_studenata 
from student_bodovi
where pol_bodovi>10;
```

### Primer 7

```sql
with student_ocene as (
select indeks, ocena br8, cast(null as smallint) br9 from ispit
where ocena=8
union all
select indeks, cast(null as smallint) br8, ocena br9 
from ispit
where ocena=9)
select indeks, count(br8) broj_8, count(br9) broj_9 
from student_ocene
group by indeks;

-- ili
with student_8 as (
select indeks, count(*) br8
from ispit
where ocena=8
group by indeks
),
student_9 as (
select indeks, count(*) br9
from ispit
where ocena=9
group by indeks
)
select coalesce(s1.indeks, s2.indeks), coalesce(br8,0) broj_8, coalesce(br9, 0) broj_9 
from student_8 s1 
full outer join student_9 s2 on s1.indeks=s2.indeks;

-- ili
select indeks, sum(case when ocena=8 then 1 else 0 end) broj_8, sum(case when ocena=9 then 1 else 0 end) broj_9
from ispit
group by indeks
having sum(case when ocena=8 then 1 else 0 end)>0 or sum(case when ocena=9 then 1 else 0 end)>0;

-- ili 
select indeks, sum(case when ocena=8 then 1 else 0 end) broj_8, sum(case when ocena=9 then 1 else 0 end) broj_9
from ispit
where ocena=8 or ocena=9
group by indeks;
```

### Primer 8

```sql
insert into dosije (indeks, ime, prezime, god_rodjenja, mesto_rodjenja) 
values (20100028, 'Marko', 'Markovic', 1990, 'Kragujevac');
```

### Primer 9

```sql
insert into predmet
values (2005, 'P112', 'Uvod u arhitekturu racunara', 6), (2006, 'P116', 'Razvoj softvera', 6);
```

### Primer 10

```sql
insert into ispit (indeks, id_predmeta, godina_roka, oznaka_roka, ocena) 
select indeks, id_predmeta, 2011, 'jun', 9
from dosije, predmet
where god_rodjenja=1991 and naziv='Programiranje 2';

```

### Primer 11

```sql
delete from dosije
where god_rodjenja=1990;
```

### Primer 12

```sql
delete from ispit
where id_predmeta in ( select id_predmeta
    from predmet
    where naziv='Programiranje 2' or bodovi=15);
```

### Primer 13

```sql
update predmet
set bodovi=bodovi*1.2 
where sifra like 'P%';
```

### Primer 14

```sql
update ispit
set (godina_roka, oznaka_roka, datum_ispita)=(2011, 'jun', null) 
where id_predmeta in (select id_predmeta
    from predmet
    where naziv='Analiza 1') and godina_roka=2011 and oznaka_roka='jan';

```

### Primer 15

```sql
update predmet
set bodovi=(select max(bodovi)
    from predmet) 
where exists ( select *
    from ispit i 
    join dosije d on i.indeks=d.indeks
    where mesto_rodjenja='Beograd' and i.id_predmeta=predmet.id_predmeta);

```

### Primer 16

```sql
select distinct coalesce(ir.naziv, ‘nema odgovarajuceg‘), coalesce(p.naziv, ‘nema odgovarajuceg‘)
from ispitni_rok ir 
left outer join ispit i on ir.godina_roka=i.godina_roka and ir.oznaka_roka=i.oznaka_roka 
full outer join predmet p on p.id_predmeta=i.id_predmeta;
```

### Primer 17

```sql
with pom as (select indeks, count(distinct id_predmeta) br_polozenih, avg(ocena+0.0) prosek
    from ispit i 
    join predmet p on p.id_predmeta=i.id_predmeta 
    where ocena>5
    group by indeks
    having sum(bodovi) between 15 and 25)
select d.indeks, ime, prezime, 
count(distinct id_predmeta) br_polaganih, br_polozenih, prosek
from dosije d 
join pom on d.indeks = pom.indeks 
join ispit i on i.indeks = d.indeks 
group by d.indeks, ime, prezime, br_polozenih,prosek
order by d.indeks
```

## Zadaci za vežbu
### Primer 1

Izdvojiti ukupan broj studenata i maksimalni broj indeksa studenta iz tabele dosije.

```sql
select count(*) ukupno_studenata, max(indeks) maksimalni_indeks 
from dosije
```

### Primer 2

Odrediti ukupan broj studenata kojima je poznata godina rođenja i broj različitih vrednosti za godinu rođenja.

```sql
select count(god_rodjenja) brSaPoznatomGod, count(distinct god_rodjenja) brRazlicitihGod 
from dosije

```

### Primer 3

Prikazati ukupan broj položenih ispita studenta sa brojem indeksa 22/2010.

```sql
select count(*) ukupno
from ispit
where indeks = 20100022 and ocena>5
```

### Primer 4

Izdvojiti ukupan broj studenata koji su bar jedan ispit položili sa ocenom 8.

```sql
select count(distinct indeks) broj_studenata 
from ispit
where ocena = 8
```

### Primer 5

Za svakog studenta izdvojiti broj indeksa i ukupan broj skupljenih bodova.

```sql
select indeks, sum(bodovi) ukupno
from ispit i 
join predmet p on i.id_predmeta = p.id_predmeta 
where ocena>5
group by indeks
```

### Primer 6

Za svakog studenta koji je skupio barem 20 bodova prikazati ukupan broj skupljenih bodova.

```sql
select indeks, sum(bodovi) ukupno 
from ispit i 
join predmet p on i.id_predmeta = p.id_predmeta 
where ocena > 5
group by indeks
having sum(bodovi) >= 20
```

### Primer 7

Za svakog studenta izračunati trenutni prosek ocena.

```sql
select indeks, avg(ocena+0.0) prosek 
from ispit
where ocena>5
group by indeks
```

### Primer 8

Za svaki od ispitnih rokova i za svaki polagan predmet odrediti broj položenih ispita.

```sql
select oznaka_roka, godina_roka, id_predmeta, count(*) ukupno 
from ispit
where ocena>5
group by oznaka_roka, godina_roka, id_predmeta
```

### Primer 9

Izdvojiti id predmeta koji ili nose više od 6 bodova ili ih je polagao student čiji broj indeksa je 20100024.

```sql
(select id_predmeta
from predmet where bodovi>6 union
select id_predmeta
from ispit where indeks = 20100024) except
(select id_predmeta
from predmet where bodovi>6 intersect
select id_predmeta
from ispit where indeks = 20100024)

-- Napomena: Ovo je ako se traži da bude ispunjen tačno jedan od uslova a ne i oba istovremeno. Za drugo tumačenje zadatka (bar jedan od uslova ispunjen) rešenje je:
select id_predmeta
from predmet where bodovi>6
union
select id_predmeta
from ispit where indeks = 20100024
```

### Primer 10

Izdvojiti id predmeta koji su polagani i u januaru 2011 i u februaru 2011.

```sql
select id_predmeta
from ispit
where oznaka_roka=‘jan‘ and godina_roka=2011 intersect
select id_predmeta
from ispit
where oznaka_roka=‘feb‘ and godina_roka=2011;

-- Ili:
select distinct id_predmeta
from ispit
where oznaka_roka=‘jan‘ and godina_roka=2011 and id_predmeta in (select id_predmeta
from ispit
where oznaka_roka=‘feb‘ and godina_roka=2011) 

-- Ili:
select distinct i.id_predmeta
from ispit i
where i.oznaka_roka=‘jan‘ and i.godina_roka=2011 and exists (select * from ispit
where id_predmeta = i.id_predmeta and oznaka_roka=‘feb‘ and godina_roka=2011)

```

### Primer 11

Izdvojiti sve identifikatore za predmete koje položio student sa brojem indeksa 20100021, a nije položio student sa indeksom 20100025, sortirane u opadajućem poretku.

```sql
select i.id_predmeta
from ispit i
where i.indeks = 20100021 and i.ocena>5 except
select i.id_predmeta
from ispit i
where i.indeks = 20100025 and i.ocena>5 order by id_predmeta

-- Ili:
select i.id_predmeta
from ispit i
where i.indeks = 20100021 and i.ocena>5 and not exists (select *
from ispit
where id_predmeta = i.id_predmeta
and indeks = 20100025 and ocena>5)

-- Ili:
select i.id_predmeta
from ispit i
where i.indeks = 20100021 and i.ocena>5 and i.id_predmeta not in (select id_predmeta from ispit
where indeks = 20100025 and ocena>5)
```

### Primer 12

 Izdvojiti brojeve indeksa studenata koji su položili barem 3 ispita i id predmeta koje su položila barem tri studenta. Sve to uradi u jednom upitu i rezultat urediti u opadajućem poretku po broju položenih ispita, odnosno studenata.

```sql
select indeks id, count(*) ukupno from ispit
where ocena > 5
group by indeks
having count(*)>=3
union
select id_predmeta id, count(*) ukupno from ispit
where ocena > 5
group by id_predmeta
having count(*)>=3
order by 2 desc
```

### Primer 13

Izdvojiti sve informacije za predmete i uz svaki od njih ispisati `lak` ako predmet nosi manje od 6 bodova, `srednje tezak` ako nosi 6 ili 7 bodova i `tezak` ako nosi bar 8 bodova.

```sql
select p.*, case
when bodovi<6 then ‘lak’
when bodovi between 6 and 7 then ‘srednje tezak’ else ‘tezak’
end as tezina
from predmet p
```

### Primer 14

Izdvojiti sva polaganja predmeta Programiranje 1 i uz svako od njih u zavisnosti od ocena izdvojiti `pao` ako je ocena 5, `provukao se` ako je ocena 6, inače `polozio`.

```sql
select i.*, case ocena when 5 then 'pao'
when 6 then 'provukao se' else 'polozio'
end as napomena
from ispit i join predmet p
on i.id_predmeta = p.id_predmeta and p.naziv = ’Programiranje 1’
```

### Primer 15

Za svakog studenta koji je položio više od 30 kredita (bodova) i čije prezime ne sadrži slovo o izdvojiti indeks, mesto rođenja, broj predmeta koje je polagao ali pao u koloni “Broj neuspesnih”, broj predmeta koje je položio u koloni “Broj uspesnih” i prosečnu ocenu u koloni “Prosek”. Rezultat urediti prema proseku opadajuce.

```sql
with Pomocna as(select d.indeks, d.mesto_rodjenja, sum(krediti) ukupnoBodova
from dosije d join ispit i on d.indeks=i.indeks join predmet p on i.id_predmeta=p.id_predmeta where d.prezime not like '%o%' and i.ocena > 5
group by d.indeks, d.mesto_rodjenja
having sum(krediti) > 30)

select P.indeks, P.mesto_rodjenja, sum(case when i.ocena<6 then 1 else 0 end) "Broj neuspelih", sum(case when i.ocena>=6 then 1 else 0 end) "Broj uspesnih",
dec(avg(i.ocena*1.0),4,2) Prosek
from Pomocna P join ispit i on P.indeks=i.indeks group by P.indeks, P.mesto_rodjenja
order by Prosek desc;
```
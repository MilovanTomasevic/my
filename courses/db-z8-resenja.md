---
layout: page
title: Z8-Rešenja
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

```sql
create table polozeni_predmeti (
indeks integer not null,
id_predmeta integer not null,
godina_roka smallint not null,
oznaka_roka char(5) not null,
ocena smallint not null,
datum_ispita date,
primary key(indeks, id_predmeta, godina_roka, oznaka_roka),
foreign key (indeks, id_predmeta, godina_roka, oznaka_roka) references ispit, constraint vrednost_ocene check (ocena between 6 and 10)
);

insert into polozeni_predmeti select *
from ispit
where ocena>5;
```

## Primer 2

```sql
alter table polozeni_predmeti 
drop datum_ispita;

reorg table polozeni_predmeti;

alter table polozeni_predmeti
    add constraint godina_upisa check (indeks/10000=2010) 
    alter column ocena set default 6;

```

## Primer 3

```sql
drop table polozeni_predmeti;
```

## Primer 4

```sql
create table student_ispiti (
    indeks integer not null primary key,
    polozeni_ispiti smallint,
    prosek double,
    constraint si_d foreign key (indeks) references dosije
);
```

## Primer 5

```sql
alter table student_ispiti
    add broj_ispita smallint
    add constraint ispiti check(broj_ispita>=polozeni_ispit);
```

## Primer 6

```sql
insert into student_ispiti
select indeks, sum(case when ocena>5 then 1 else 0 end) broj_polozenih,
    avg(case when ocena>5 then ocena*1.0 else null end), count(*) broj_polaganih
from ispit
group by indeks;
```

## Primer 7

```sql
create index student_prosek on student_ispiti (indeks, prosek);
```

## Primer 8

```sql
create view ispitnirok_predmeti (ispitni_rok, predmet, broj_ispita) as 
select ir.naziv, p.naziv, count(*)
from ispitni_rok ir 
join ispit i on ir.godina_roka=i.godina_roka and ir.oznaka_roka=i.oznaka_roka
join predmet p on p.id_predmeta=i.id_predmeta 
group by ir.naziv, p.naziv;
```

## Primer 9

```sql
select indeks,
    count(distinct id_predmeta) broj_polaganih_predmeta, 
    count(distinct ocena) broj_razlicitih_ocena,
    count(*) broj_ispita,
    sum(case when ocena>5 then 1 else 0 end) broj_polozenih_ispita, 
    max(ocena) najveca_ocena,
    avg(case when ocena>5 then ocena*1.0 else null end) prosek
from ispit
group by indeks
order by broj_ispita;
```

## Primer 10

```sql
select d.indeks, ime, prezime, 
    count(distinct i.id_predmeta) br_polagao, br_polozio,
    sum(case when ocena>5 then 1 else 0 end)
    avg(case when ocena>5 then ocena*1.0 else null end) prosek
from dosije d 
join ispit i on d.indeks=i.indeks 
join predmet p on i.id_predmeta=p.id_predmeta
where ime like 'A%' or ime like '%a%' or ime like 'O%' or ime like '%o%' 
group by d.indeks, ime, prezime
having sum(case when ocena>5 then bodovi else 0 end ) between 15 and 25 
order by d.indeks;
```

## Primer 11

```sql
select d.indeks, ime, prezime, max(datum_ispita) poslednji_ispit 
from dosije d 
join ispit i on d.indeks=i.indeks
where ocena>5 and year(current_date)-god_rodjenja between 20 and 25 
group by d.indeks, ime, prezime
having avg(ocena*1.0)>=7
order by 4;
```

## Primer 12

```sql
with student_bodovi (indeks, polozeni_bodovi) as (
select indeks, sum(bodovi)
from ispit i 
join predmet p on i.id_predmeta=p.id_predmeta
where ocena>5
group by indeks )
select d.indeks, ime, prezime, polozeni_bodovi
from student_bodovi sb 
join dosije d on d.indeks=sb.indeks
where polozeni_bodovi=(select max(polozeni_bodovi) 
from student_bodovi);

select d.indeks, ime, prezime, sum(bodovi)
from ispit i join dosije d on i.indeks=d.indeks
join predmet p on p.id_predmeta=i.id_predmeta 
where ocena>5
group by d.indeks, ime, prezime
having sum(bodovi)>= all(select sum(bodovi)
    from ispit i 
    join predmet p on i.id_predmeta=p.id_predmeta
    where ocena>5
    group by indeks);
```

## Primer 13

```sql
select ceil(sum(bodovi)/60.0)
from predmet
where id_predmeta not in (select id_predmeta
    from ispit
    where indeks=20100027 and ocena>5);
```
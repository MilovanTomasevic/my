---
layout: page
title: Z10-Rešenja
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
create distinct type indeks as integer with comparisons;
```

## Primer 2

```sql
create table dosije1 (
    indeks indeks not null , 
    id_smera integer not null , 
    status varchar(20) not null , 
    ime varchar(10) not null , 
    prezime varchar(15) not null , 
    dat_upisa date not null,
primary key (indeks),
    foreign key (id_smera) references smer);
```

## Primer 3

```sql
insert into dosije1
select indeks, id_smera, status, ime, prezime, dat_upisa 
from dosije;
```

## Primer 4

```sql
select d1.indeks + d2.indeks
from dosije1 d1, dosije1 d2
where d1.indeks=20060001 and d2.indeks=20060005;

select integer(d1.indeks) + integer(d2.indeks)
from dosije1 d1, dosije1 d2
where d1.indeks=indeks(20060001) and d2.indeks=indeks(20060005);
```

## Primer 5

```sql
create function godinaupisa(indeks indeks) -- drugo je tip, prvo ulazna promenljiva... 
returns integer
return integer(indeks)/10000;
```

## Primer 6

```sql
create function brojindeksa(indeks indeks) 
returns integer
return mod(integer(indeks),10000);

select godinaupisa(indeks), brojindeksa(indeks) 
from dosije1;
```

## Primer 7

```sql
create function max (indeks) 
returns indeks
source sysibm.max(integer);

select max(indeks)
from dosije1;
```

## Primer 8

```sql
create distinct type bodovi as smallint with comparisons;

create function obaveznibodovi(smer integer) 
returns bodovi
return select sum(bodovi)
from obavezan_predmet op 
join predmet p on p.id_predmeta=op.id_predmeta
where op.id_smera=smer;

create table polozenobodova
(
indeks integer not null, polozenobodova bodovi, primary key (indeks)
);

insert into polozenobodova
select d.indeks, sum(p.bodovi)
from dosije d 
join ispit i2 on d.indeks=i2.indeks
join predmet p on p.id_predmeta=i2.id_predmeta 
where not exists ( select *
    from obavezan_predmet op 
    where op.id_smera=d.id_smera
    and not exists (select * from ispit i
        where i.id_predmeta=op.id_predmeta and d.indeks=i.indeks
        and ocena>5 and status_prijave='o'))
        and ocena>5 and status_prijave='o' 
        group by d.indeks;

create view studpolobav as (
select d.indeks, ime, prezime, s.naziv, polozenobodova, obaveznibodovi(s.id_smera) obavezkred 
from dosije d 
join smer s on d.id_smera=s.id_smera
join polozenobodova pk on pk.indeks=d.indeks; );
```

## Primer 9

```sql
with na_smeru as (
select d.id_smera, count(distinct d.indeks) n, avg(ocena+0.0) ocena 
from dosije d 
join smer s on d.id_smera = s.id_smera 
join nivo_kvalifikacije nk on nk.id = s.id_nivoa and nk.stepen = 'VI' 
left outer join ispit i on d.indeks = i.indeks and status_prijave='o' and ocena>5 and godina = 2006 
where year(dat_upisa) = 2006
group by d.id_smera ), svias(
select sum(n) n
from na_smeru
)

select s.oznaka, s.naziv, svi.n ukupno, us.n nasmer, us.n * 100.0 / svi.n proc, ocena 
from smer s 
join na_smeru us
on us.id_smera = s.id_smera, svi 
order by ocena;
```

## Primer 10

```sql
update dosije
set status='diplomirao'
where id_smera in ( select id_smera
    from smer 
    join nivo_kvalifikacije on id=id_nivoa
    where smer.naziv='Informatika' and stepen='VI')
    and 180 <= ( select sum(p.bodovi) 
        from ispit i 
        join predmet p on i.id_predmeta=p.id_predmeta
        where indeks = dosije.indeks and ocena > 5 and status_prijave='o');

delete from ispit
where godina=2008 and indeks in ( select indeks
    from dosije
    where status='mirovanje');
```
---
layout: page
title: Z9-Rešenja
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
select ime, count(*)n 
from dosije
where pol='m' 
group by ime
order by n;
```

## Primer 2

```sql
select i.indeks, rtrim(d.ime) || ' ' || rtrim(d.prezime), sum(p.bodovi) polozeno 
from dosije d
join upisan_kurs uk
on d.indeks=uk.indeks
join kurs k
on k.id_predmeta=uk.id_predmeta and k.godina=uk.godina
and k.semestar=uk.semestar
join predmet p
on k.id_predmeta=p.id_predmeta
join ispit i
on uk.indeks=i.indeks
and uk.id_predmeta=i.id_predmeta and uk.godina=i.godina
and uk.semestar=i.semestar
where i.status_prijave='o' and i.ocena>5
group by i.indeks, rtrim(d.ime) || ' ' || rtrim(d.prezime) 
order by 3;
```

## Primer 3

```sql
select indeks, max(coalesce(datum_usmenog, datum_pismenog)) poslednji 
from ispit
where ocena > 5 and status_prijave='o'
group by indeks;
```

## Primer 4

```sql
select s.naziv smer, p1.naziv obavezan_predmet, p2.naziv uslovni_predmet 
from nivo_kvalifikacije nk 
join smer s on s.id_nivoa=nk.id
join obavezan_predmet op on op.id_smera=s.id_smera
join predmet p1 on p1.id_predmeta=op.id_predmeta
left outer join uslovni_predmet up on up.id_predmeta=op.id_predmeta 
left outer join predmet p2 on p2.id_predmeta=up.id_uslovnog
where nk.stepen='VI'
order by smer, obavezan_predmet;
```

## Primer 5

```sql
with indeksbodova as (select indeks, sum(p.bodovi) polbodovi 
from ispit i 
join predmet p on i.id_predmeta=p.id_predmeta
where ocena > 5 and status_prijave='o'
group by indeks), maxsmer as (select id_smera, max(polbodovi) maxb
    from dosije d 
    join indeksbodova on d.indeks=indeksbodova.indeks 
    group by id_smera)
select s.naziv, d.indeks, ime, prezime, polbodovi
from dosije d 
join indeksbodova on d.indeks=indeksbodova.indeks
join maxsmer on maxsmer.id_smera=d.id_smera 
join smer s on maxsmer.id_smera=s.id_smera
where polbodovi = maxb;
```

## Primer 6

```sql
select d.indeks, d.ime, d.prezime, p.naziv
from dosije d 
  join smer s on s.id_smera=d.id_smera
  join nivo_kvalifikacije nk on nk.id=s.id_nivoa
  join obavezan_predmet op on d.id_smera=op.id_smera 
  join predmet p on p.id_predmeta=op.id_predmeta
where s.naziv='Informatika' and nk.stepen='VI' and d.indeks between 20070000 and 20079999 and not exists(select *
from ispit i 
where i.indeks=d.indeks and i.id_predmeta=op.id_predmeta and ocena>5 and status_prijave='o');

```

## Primer 7

```sql
with nepolozeni as (select d.indeks, d.ime, d.prezime,p.id_predmeta, p.naziv 
from dosije d 
  join obavezan_predmet op on d.id_smera=op.id_smera
  join predmet p on p.id_predmeta=op.id_predmeta
where d.id_smera=201 and d.indeks/10000=2007 and not exists (select *
from ispit i
where i.indeks= d.indeks and i.id_predmeta=op.id_predmeta and ocena>5 and status_prijave='o'))
select nepolozeni.ime, nepolozeni.prezime, nepolozeni.naziv predmet, p.naziv
from nepolozeni 
  join uslovni_predmet up on nepolozeni.id_predmeta=up.id_predmeta 
  join predmet p on p.id_predmeta=up.id_uslovnog
where up.id_uslovnog not in ( select id_predmeta from ispit i
    where indeks=nepolozeni.indeks and ocena>5 and status_prijave='o')
    order by nepolozeni.prezime, nepolozeni.ime;
```

## Primer 8

```sql
with a as (select id_nivoa, id_predmeta, count(*) n
    from smer s 
    join obavezan_predmet op on s.id_smera=op.id_smera 
    group by id_nivoa, id_predmeta),
b as (select id_nivoa, count(*) n
    from smer
    group by id_nivoa)
    select nk.naziv, p.naziv
    from a join b on a.id_nivoa=b.id_nivoa
    join nivo_kvalifikacije nk on nk.id=a.id_nivoa
    join predmet p on a.id_predmeta=p.id_predmeta where a.n=b.n;

--ili
select distinct kv.naziv, p.naziv
from obavezan_predmet op join smer s1
on op.id_smera=s1.id join nivo_kvalifikacije kv
on kv.id=s1.id_nivoa join predmet p
on op.id_predmeta=p.id_predmeta 
where not exists( select *
    from smer s
    where s.id_nivoa=s1.id_nivoa
    and not exists( select *
        from obavezan_predmet p1
        where op.id_predmeta=p1.id_predmeta and p1.id_smera=s.id_smera));
```

## Primer 9

```sql
with a as (select id_predmeta id, sum(case when ocena>5 then 1 else 0 end) brP, count(distinct indeks) uk 
from ispit
where status_prijave='o'
group by id_predmeta)
select p.naziv, a.brP*100.0/a.uk prolaznost
from predmet p 
join a on p.id_predmeta=a.id
order by prolaznost desc;

```

## Primer 10

```sql
select s.naziv, d1.dat_rodjenja, d1.dat_rodjenja, d1.indeks, d1.ime, d1.prezime, d2.indeks, d2.ime, d2.prezime 
from dosije d1 
join smer s on d1.id_smera=s.id_smera 
join dosije d2 on d1.id_smera=d2.id_smera and d1.dat_rodjenja=d2.dat_rodjenja 
where d1.indeks<d2.indeks;
```
---
layout: page
title: Z12-Rešenja
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
with uslovni(id_predmeta, id_uslovnog) as (
select id_predmeta, id_uslovnog
from uslovni_predmet
where id_predmeta=662
union all
select up.id_predmeta, up.id_uslovnog
from uslovni, uslovni_predmet up
where uslovni.id_uslovnog=up.id_predmeta)
select distinct u.id_predmeta, p1.naziv, id_uslovnog, p2.naziv 
from uslovni u 
join predmet p1 on p1.id_predmeta=u.id_predmeta 
join predmet p2 on p2.id_predmeta=u.id_uslovnog;
```

## Primer 2

```sql
with uslovni(nivo, id_predmeta, id_uslovnog) as (
select 0, id_predmeta, id_uslovnog
from uslovni_predmet
where id_predmeta=662
union all
select uslovni.nivo+1, up.id_predmeta, up.id_uslovnog
from uslovni, uslovni_predmet up
where uslovni.id_uslovnog=up.id_predmeta)
select distinct nivo, u.id_predmeta, p1.naziv, id_uslovnog, p2.naziv 
from uslovni u 
join predmet p1 on p1.id_predmeta=u.id_predmeta 
join predmet p2 on p2.id_predmeta=u.id_uslovnog where nivo>0;
```

## Primer 3

```sql
with sp as (
select s.id_smera, s.oznaka, s.bodovi espbuk, sum(p.bodovi) espbob 
from obavezan_predmet op
join predmet p on p.id_predmeta = op.id_predmeta
right outer join smer s on s.id_smera = op.id_smera

--moze i ovako: 
from smer s
left outer join obavezan_predmet op on s.id = op.id_smera
left outer join predmet p on p.id = op.id_predmeta
group by s.id_smera, s.oznaka, s.bodovi ),
polozeno as ( select d.indeks, d.id_smera, 
    sum(coalesce(p.bodovi,0)) poluk,
    sum(case when op.id_predmeta is not null then p.bodovi else 0 end) polob
    from ispit i
    join predmet p
    on i.id_predmeta = p.id_predmeta and i.ocena>5
    and i.status_prijave='o'
    right outer join dosije d
    on d.indeks = i.indeks
    left outer join obavezan_predmet op on op.id_smera = d.id_smera
    and op.id_predmeta = i.id_predmeta group by d.indeks, d.id_smera
)

select
indeks, oznaka,
espbuk, poluk, poluk*100.0/espbuk procuk,
espbob, polob,
case when espbob>0 then polob*100.0/espbob else 0 end procob
from polozeno p 
join sp on sp.id_smera = p.id_smera 
order by procuk;
```

## Primer 4

```sql
with prolaznost as (
select ir.naziv naziv_roka, p.id_predmeta,
p.naziv naziv_predmeta, 
count(i.indeks) brPrijavili,
sum(case when status_prijave='o' and ocena> 5 then 1 else 0 end) brPolozili, 
sum(case when status_prijave='x' and ocena> 5 then 1 else 0 end) brPonistili
from ispitni_rok ir 
left outer join ispit i on ir.godina=i.godina_roka and ir.oznaka=i.oznaka_roka
left outer join predmet p on p.id_predmeta=i.id_predmeta
where ir.godina between 2005 and 2009
group by ir.godina, ir.naziv, p.id_predmeta, p.naziv) 
select naziv_roka, naziv_predmeta, brPrijavili, brPolozili,
case when brPrijavili>0 then brPolozili*100.0/brPrijavili else 0 end "Procenat polozenih", brPonistili,
case when brPrijavili>0 then brPonistili*100.0/brPrijavili else 0 end "Procenat ponistenih", case
when brPrijavili>0 and (brPolozili+brPonistili)*100.0/brPrijavili > 80 then 'odlicna' when brPrijavili>0 and (brPolozili+brPonistili)*100.0/brPrijavili > 40 then 'srednja'
else 'losa' end as rang
from prolaznost 
order by rang;
```

## Primer 5

```sql
with polozeno as (
select i.indeks, sum(p.bodovi) as polozeno 
from ispit i 
join predmet p on i.id_predmeta = p.id_predmeta 
where i.ocena > 5 and status_prijave = 'o' 
group by i.indeks
)
select d.indeks, d.ime, d.prezime, s.naziv,
(select sum(p.bodovi)
    from predmet p 
    join obavezan_predmet op on p.id_predmeta = op.id_predmeta
    where op.id_smera = d.id_smera and not exists ( select *
    from ispit i
    where i.indeks = d.indeks and i.id_predmeta = p.id_predmeta and ocena > 5 and - status_prijave = 'o' )) as nepolozeno_obaveznih

from dosije d 
join smer s on s.id_smera = d.id_smera
join polozeno p on d.indeks = p.indeks
where not exists ( select *
from uslovni_predmet up 
join obavezan_predmet op on up.id_predmeta = op.id_predmeta
where op.id_smera = d.id_smera and not exists ( select *
from ispit i 
where i.indeks = d.indeks and i.id_predmeta = up.id_uslovnog and
ocena > 5 ))

and s.bodovi > p.polozeno 
order by nepolozeno_obaveznih;
```

## Primer 6

```sql
update upis_godine ug
set upisano_bodova=(select sum(p.bodovi)
    from upisan_kurs uk 
    join predmet p on p.id_predmeta=uk.id_predmeta
    where  uk.indeks=ug.indeks and uk.godina=ug.godina), dat_upisa='09-20-2008'
where ug.godina=2008 and indeks in ( select indeks
    from dosije d 
    join smer s on d.id_smera=s.id_smera
    join nivo_kvalifikacije nk on s.id_nivoa=nk.id
    where nk.stepen='VI');

update upis_godine ug
set overeno_bodova= ( select coalesce(sum(p.bodovi),0)
    from ispit i 
    join predmet p on i.id_predmeta=p.id_predmeta
    where i.indeks=ug.indeks and i.godina=2008 and ocena>5 and status_prijave='o'),

dat_overe='09-05-2009'

where godina=2008 and indeks in ( select indeks
    from dosije d
    join smer s on d.id_smera=s.id_smera
    join nivo_kvalifikacije nk on s.id_nivoa=nk.id
    where nk.stepen='VI')
and upisano_bodova is not null;
```

## Primer 7

```sql
--create trigger unos_ispita

before insert on ispit
referencing new as unos
for each row
begin atomic
    set unos.ocena= case 
        when unos.bodovi>90 then 10
        when unos.bodovi>80 then 9
        when unos.bodovi>70 then 8
        when unos.bodovi>60 then 7
        when unos.bodovi>50 then 6
        when unos.bodovi>0 then 5
        else null
    end;
end@
```

## Primer 8

```sql
create type rsd as float;
create function iznosskolarine(bodovi integer) --returns rsd
return bodovi*1200.0;
create table skolarina (
  indeks integer not null,
  godina smallint not null,
  bodova integer ,
  iznos rsd ,
  izmireno rsd ,
primary key(indeks, godina) ) ;
from ispit i join predmet p
       on i.id_predmeta=p.id_predmeta
where i.indeks=ug.indeks
      and i.godina=2008
and ocena>5
and status_prijave='o'),
    when unos.bodovi>90 then 10
    when unos.bodovi>80 then 9
    when unos.bodovi>70 then 8
    when unos.bodovi>60 then 7
    when unos.bodovi>50 then 6
    when unos.bodovi>0 then 5
    else null
end;
insert into skolarina (indeks, godina, bodova, iznos)
select indeks, godina, upisano_bodova, iznosskolarine(upisano_bodova) --from upis_godine
where godina=2008 and status='samofinansiranje';
merge into skolarina s
using ( select indeks, godina, upisano_bodova
        from upis_godine
 where status='samofinansiranje' and godina<2010 and upisano_bodova>40) as p
on s.indeks=p.indeks and s.godina=p.godina
when matched then
 update set izmireno=iznos
when not matched then
 insert (indeks, godina, bodova, iznos)
 values(p.indeks, p.godina, p.upisano_bodova, iznosskolarine(upisano_bodova));
```

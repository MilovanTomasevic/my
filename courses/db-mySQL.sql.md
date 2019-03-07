---
layout: page
title: Skripta - mySQL.sql
description: >
  Skripta za šemu baze podataka, mySQL
hide_description: true

---

     

![](../db/1.png)

Model baze podataka
{:.figure}

![](../db/2.png)

Model baze podataka
{:.figure}

```sql

DROP DATABASE stud2011;
CREATE DATABASE stud2011;

create table dosije (
  indeks      INT      not null,  
  ime       varchar(50)  not null,
  prezime     varchar(50)  not null,
  god_rodjenja  INT,  
  mesto_rodjenja varchar(100),      

  primary key (indeks)
);

insert into dosije values
(20100021, 'Milos', 'Peric', 1992, 'Beograd'),
(20100022, 'Marijana', 'Savkovic', 1993, 'Kraljevo'),
(20100023, 'Sanja', 'Terzic', 1991, 'Beograd'),
(20100024, 'Nikola', 'Vukovic', 1992, 'Novi Sad'),
(20100025, 'Predrag', 'Popovic', 1991, 'Kraljevo'),
(20100026, 'Zorica', 'Miladinovic', 1993, 'Vranje')
;

create table predmet (
  id_predmeta     INT      not null,
  sifra           varchar(20)  not null,
  naziv           varchar(200) not null,
  krediti         INT     not null,

  primary key(id_predmeta)
);

insert into predmet values
(1001, 'M111', 'Analiza 1', 6),
(1002, 'M112', 'Analiza 2', 6),
(1003, 'M113', 'Analiza 3', 6),
(1021, 'M131', 'Geometrija', 6),
(1101, 'M105', 'Diskretne strukture 1', 6),
(1102, 'M106', 'Diskretne strukture 2', 6),
(2001, 'P101', 'Programiranje 1', 8),
(2002, 'P102', 'Programiranje 2', 8),
(2003, 'P103', 'Objektno orijentisano programiranje', 6),
(2004, 'P104', 'Algoritmi i strukture podataka', 6),
(3001, 'S1', 'Engleski jezik 1', 5),
(3002, 'S2', 'Engleski jezik 2', 5),
(4001, 'R101', 'Uvod u organizaciju racunara', 5),
(4002, 'R102', 'Uvod u Veb i Internet tehnologije', 5)
;

create table ispitni_rok (
  godina_roka     INT     not null,
  oznaka_roka     varchar(20)  not null,
  naziv           varchar(50)  not null,

  primary key (godina_roka, oznaka_roka)
);

insert into ispitni_rok values
(2011, 'jan', 'Januar 2011'),
(2011, 'feb', 'Februar 2011'),
(2011, 'apr', 'April 2011'),
(2011, 'jun', 'Jun 2011'),
(2011, 'sep', 'Septembar 2011'),
(2011, 'okt', 'Oktobar 2011')
;

create table ispit (
  indeks          INT      not null,
  id_predmeta     INT      not null,
  godina_roka     INT     not null, /*godina*/
  oznaka_roka     char(5)      not null, /*semestar*/
  ocena           INT     not null,
  datum_ispita  date                 , /*datum_pismenog, datum_usmenog */      

  primary key (indeks, id_predmeta, godina_roka, oznaka_roka),
  
  foreign key (godina_roka, oznaka_roka) references ispitni_rok(godina_roka, oznaka_roka),
  foreign key (indeks) references dosije(indeks),
  foreign key (id_predmeta)references predmet(id_predmeta)
);

insert into ispit values 
(20100021, 1001, 2011, 'jan', 9, '20.01.2011'),
(20100022, 1001, 2011, 'jan', 8, '20.01.2011'),
(20100023, 1001, 2011, 'jan', 8, '20.01.2011'),
(20100024, 1001, 2011, 'jan', 10, '20.01.2011'),
(20100025, 1001, 2011, 'jan', 6, '20.01.2011'),
(20100026, 1001, 2011, 'jan', 5, '20.01.2011'),

(20100021, 2001, 2011, 'jan', 10, '25.01.2011'),
(20100022, 2001, 2011, 'jan', 9, '25.01.2011'),
(20100023, 2001, 2011, 'jan', 8, '25.01.2011'),
(20100024, 2001, 2011, 'jan', 7, '25.01.2011'),
(20100025, 2001, 2011, 'jan', 5, '25.01.2011'),

(20100021, 3001, 2011, 'jan', 7, '27.01.2011'),
(20100023, 3001, 2011, 'jan', 5, '27.01.2011'),
(20100024, 3001, 2011, 'jan', 6, '28.01.2011'),
(20100026, 3001, 2011, 'jan', 6, '28.01.2011'),

(20100026, 1001, 2011, 'feb', 7, '10.02.2011'),

(20100025, 2001, 2011, 'feb', 6, '10.02.2011'),
(20100026, 2001, 2011, 'feb', 7, '10.02.2011'),

(20100021, 1021, 2011, 'apr', 7, '03.04.2011'),
(20100022, 1021, 2011, 'apr', 5, '03.04.2011'),
(20100023, 1021, 2011, 'apr', 10, '03.04.2011'),
(20100024, 1021, 2011, 'apr', 6, '03.04.2011'),
(20100026, 1021, 2011, 'apr', 8, '03.04.2011')
;
```
mySQL.sql
{:.figure}
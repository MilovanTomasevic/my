{% extends "base_slides.md" %}
{% block slides %}
name: sadrzaj

# Sadržaj

- [DOMMLite](#dommlite)
- [mobl](#mobl)
- [pyFlies](#pyflies)

---
name: dommlite
class: center, middle, inverse

# DOMMLite

---
layout: true

.section[[DOMMLite](#sadrzaj)]

---

## Šta je DOMMLite?

- DOMMLite.ref[1] je jezik za opis statičke strukture poslovnih aplikacija.ref[2].
- Opisuje entitete, njihove atribute, validatore, veze između entiteta,
  primitivne tipove, pakete, servise i sl.
- Generator koda na osnovu DOMMLite mograma generiše naprednu CRUD aplikaciju sa
  podrškom za pretrage, filtriranje, sortiranje, definisanje servisnih metoda,
  validacije itd. Implementiran u xText-u.
  
.footer[

1. I. Dejanović, *Metamodel, editor modela i generator poslovnih aplikacija*.
   magistarska teza, April 2008.

1. I. Dejanović, G. Milosavljević, B. Perišić, and M. Tumbas, *A domain-specific
   language for defining static structure of database applications*, Computer
   Science and Information Systems, vol. 7, pp. 409–440, June 2010. ISSN
   1820-0214

]

---
## Osnovne osobine

- Opis entiteta, ključeva, veza jedan na jedan, jedan na više, više na više.
- Tekstualna sintaksa. Puna eclipse integracija (dopuna i bojenje koda,
  strukturni pogled, navigacija, validacija sintakse).
- Veliki broj standardnih parametarskih validatora uz mogućnost definisanja
  dodatnih u samom jeziku uz implementaciju na jeziku ciljne platforme.
- Podrška za definisanje korisničkih tipova podataka, validatora i oznaka.
- Generator koda za Django web okvir za razvoj.ref[1] . Generisanje pune CRUD
  aplikacije sa pretragama, filtriranjem, sortiranjem itd.

.footer[
1.  http://www.djangoproject.com
]

---
## Model

![:scale 60%](anatomija-dsla/Model.png)

---
## Paketi

![:scale 50%](anatomija-dsla/Package.png)

---
## Entiteti

![:scale 60%](anatomija-dsla/Entity.png)

---
## Konkretna sintaksa

![:scale 90%](anatomija-dsla/BuildIns.png)

---
## Odeljci

![:scale 40%](anatomija-dsla/FeatureCompartment.png)

![:scale 40%](anatomija-dsla/OperationCompartment.png)

---
## Odeljci - konkretna sintaksa

![:scale 60%](anatomija-dsla/compartments-syntax.png)

---
## Odeljci - strukturni prikaz

![:scale 50%](anatomija-dsla/outline.png)

---
## Odeljci - mapiranje na ekranske forme

![:scale 70%](anatomija-dsla/django-validatori.png)

---
## Atributi i reference

![:scale 30%](anatomija-dsla/Feature.png)

.lcol[
![:scale 60%](anatomija-dsla/Property.png)
]
.rcol[
![:scale 80%](anatomija-dsla/TypedElement.png)
]

---
## Atributi i reference - konkretna sintaksa

![:scale 90%](anatomija-dsla/BuildIns.png)

---
## Oznake (*Tags*)

- Služe za opis dodatne semantike elementa nad kojim su definisane.
- DOMMLite poseduje *11 ugrađenih oznaka* (*plural, searchBy, orderBy, finder,
  filterFields...*) a korisnik može definisati na nivou mograma i svoje oznake.
  
---
## Primer - podrška za specifičnosti prirodnih jezika

![:scale 90%](anatomija-dsla/Akuzativ.svg)

---
## Validatori 

- Definisanje uslova koji mora biti ispunjen da bi se instanca elementa modela
  nad kojom je primenjen smatrala ispravnom.
- DOMMLite poseduje *33 ugrađena validatora* (*isAlphaNumeric, isOnlyDigits,
  isValidEmail...*) a na nivou mograma mogu biti definisani korisnički.

---
## Primer upotrebe validatora

![:scale 90%](anatomija-dsla/Validatori.svg)

---
## Servisi

![](anatomija-dsla/Service.png)

---
## Podrška za *finder* metode

![:scale 60%](anatomija-dsla/Services.png)

![:scale 80%](anatomija-dsla/finder.png)

---
## Dopuna koda

![:scale 60%](anatomija-dsla/DopunaKoda1.png)

![:scale 60%](anatomija-dsla/DopunaKoda2.png)

---
## Generator koda

![](anatomija-dsla/Generisanje.svg)

---
## Prikaz generisane forme

![:scale 80%](anatomija-dsla/django-validatori.png)

---
name: mobl
class: center, middle, inverse
layout: false

# mobl

---
layout: true

.section[[mobl](#sadrzaj)]

---

## mobl

TODO

---
name: pyflies
class: center, middle, inverse
layout: false

# pyFlies

---
layout: true

.section[[pyFlies](#sadrzaj)]

---

## pyFlies

--

class: center, middle, theend, hide-text
layout: false
background-image: url(../theend.gif)

{% endblock %}

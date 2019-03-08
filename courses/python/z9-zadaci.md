{% extends "base_slides.md" %}
{% block slides %}

name: zadaci
name: uvod 
class: center, middle, inverse

# Zadaci

---
layout: true
.section[[Zadaci](#sadrzaj)]

---

## Zadatak 1 

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Implementirati grafove prikazane na slici 1. Graf predstaviti korišćenjem reprezentacije susednih lista čvorova (*adjacency-list representation*) koja je takoĎe prikazana na slici.
- Čvor grafa predstaviti po uzoru na priloženi šablon. 
- Napisati funkcije za (i) ispis svih susednih čvorova v čvora u i (ii) ispis svih veza čvora u i susednih čvorova v.

![:scale 85%](img/z9/z1.png)
]
]

---
## Zadatak 2

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Implementirati pretragu grafa po širini (*Breadth-first search*). 
- Za proveru funkcionalnosti iskoristiti graf sa slike. 

![:scale 72%](img/z9/z2.png)
]
]

---
## Zadatak 3

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Implementirati pretragu grafa po dubini (*Depth-first search*). 
- Za proveru funkcionalnosti iskoristiti graf sa slike.

![:scale 77%](img/z9/z3.png)
]
]

---
## Zadatak 4 <a target="_blank" rel="noopener noreferrer" href="../python-z9-resenja"> ☛ `Rešenja`</a>

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Koristeći pretragu grafa po dubini implementirati topološki sort algoritam čiji je pseudokod prikazan na slici.

![:scale 65%](img/z9/z4.png)
]
]

---

## Rešenja

.message.is-success[
.message-header[
Odgovor
]
.message-body[
- <a target="_blank" rel="noopener noreferrer" href="../python-z9-resenja"> ☛ `Rešenja`</a>
]
]

---

class: center, middle, theend, hide-text
layout: false
background-image: url(../theend.gif)

{% endblock %}
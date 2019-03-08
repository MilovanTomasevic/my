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
- 1. Implementirati Insertion-sort algoritam, proveriti njegovu funkcionalnost i analizirati vreme izvršenja. Pseudokod algoritma je prikazan na slici.

![:scale 50%](img/z2/z2.png)
]
]

---
## Zadaci 2, 3, 4

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Implementirati Bubble sort algoritam, proveriti njegovu funkcionalnost i analizirati vreme izvršenja. Ulazni podaci su niz (lista) brojeva i tražena vrednost. Izlaz je pozicija na kojoj se nalazi tražena vrednost.
- Implementirati algoritam za linearnu pretragu brojeva. Ulazni podaci su niz (lista) brojeva i tražena vrednost. Izlaz je pozicija na kojoj se nalazi tražena vrednost.
- Implementirati algoritam za binarnu pretragu brojeva. Ulazni podaci su niz (lista) brojeva i tražena vrednost. Izlaz je pozicija na kojoj se nalazi tražena vrednost.
]
]

--

.message.is-warning[
.message-header[
Info
]
.message-body[
- Ulazni podaci su celobrojne vrednosti organizovane u listu.
- Funkcionalnost algoritma proveriti na malom broju ulaznih podatka.
- Tokom analize vremena izvršenja algoritma koristiti različite veličine ulaznih podataka.

]
]

--

.message.is-success[
.message-header[
Odgovor
]
.message-body[
- <a target="_blank" rel="noopener noreferrer" href="../python-z2-resenja"> ☛ `Rešenja`</a>

]
]

---

class: center, middle, theend, hide-text
layout: false
background-image: url(../theend.gif)

{% endblock %}
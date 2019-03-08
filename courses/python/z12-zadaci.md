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
- Implementirati rešenje problema nalaženja najdužeg zajedničkog podniza. 
- Analizirati vreme izvršavanja i iscrtati grafik.

![:scale 70%](img/z12/z1.png)
]
]

---
## Zadatak 2

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Implementirati rešenje problema nalaženja najdužeg zajedničkog podniza upotrebom dinamičkog programiranja. 
- Analizirati vreme izvršavanja i iscrtati grafik. Pseudokod algoritam je dat na slici.

![:scale 40%](img/z12/z2.png)
]
]

---
## Zadatak 3

.message.is-info[
.message-header[
Zadatak
]
.message-body[
- Implemetirati iscrtavanje nalaženja najdužeg zajedničkog podniza upotrebom dinamičkog programiranja iz zadatka 2. 
- Pseudokod algoritma je dat na slici.
  ![:scale 57%](img/z12/z3.png)
]
]

--
.message.is-success[
.message-header[
Odgovor
]
.message-body[
- <a target="_blank" rel="noopener noreferrer" href="../python-z12-resenja"> ☛ `Rešenja`</a>
]
]

---

class: center, middle, theend, hide-text
layout: false
background-image: url(../theend.gif)

{% endblock %}
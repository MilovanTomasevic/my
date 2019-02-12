---
title: Courses/Slides
description: >
  ...context are the programming languages as well as methodologies. There are various presentations as well as pieces of training by Milovan Tomašević...
hide_description: true
menu: true
order: 3
permalink: /courses/

---

In this context are the programming languages as well as methodologies. In addition, there are various presentations as well as pieces of training that will serve in further education. It also provides special training that is focused on the IT sector, especially on HPC.

You can read more at the [faculty website](https://www.fis.unm.si/si/){:target="_blank"} or contact me personally if necessary.
I wish you a lot of success during your learning.

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Technologies 
### GIT - Program control system 
  - [Git](/tech/git.html){:target="_blank"}{:.heading.flip-title} --- Basic level.
{:.related-posts.faded}

### Pyhton

  - [Pyhton](/tech/Python.html){:target="_blank"}{:.heading.flip-title} --- Basic level.
  - [PyhtonPro](/tech/python_napredni.html){:target="_blank"}{:.heading.flip-title} --- Advanced level.
{:.related-posts.faded}

### Domain-Specific Languages (DSLs)

1. [O predmetu](/courses/jsd/upoznavanje.html){:target="_blank"}
1. [Programski jezik Python](#pyhton)
1. [Uvod u jezike specifične za domen](/courses/jsd/uvod.html){:target="_blank"}
1. [Jezičke sintakse i metamodelovanje](/courses/jsd/jezicke-sintakse-i-metamodelovanje.html){:target="_blank"}
1. [Tekstualne sintakse](/courses/jsd/tekstualne-sintakse.html){:target="_blank"}
1. [Arpeggio](/courses/tech/arpeggio.html){:target="_blank"}
1. parglare - u pripremi
1. [textX](/courses/tech/textx.html){:target="_blank"}
1. [Xtext](/courses/jsd/06-Xtext.html){:target="_blank"}
1. [Generisanje programskog koda](/courses/jsd/generisanje-programskog-koda.html){:target="_blank"}
1. [Anatomija jednog DSL-a](/courses/jsd/anatomija-dsla.html){:target="_blank"}

- [Literatura](jsd-literatura){:target="_blank"}
  

### High-performance computing (HPC)

#### HPC Complete Courses (C)



| HPC |                                 Teroija                                 |                                 Vežbe                                 |                     Zadaci                     |
|:---:|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|:----------------------------------------------:|
|  1. |        [Uvod](high-performance-computing/uvod){:target="_blank"}        |  [V1-openMP](high-performance-computing/V1-openMP){:target="_blank"}  |  [Z1-openMP](hpc-z1-openMP){:target="_blank"}  |
|  2. | [Arhitektura](high-performance-computing/arhitektura){:target="_blank"} |  [V2-openMP](high-performance-computing/V2-openMP){:target="_blank"}  |  [Z2-openMP](hpc-z2-openMP){:target="_blank"}  |
|  3. | [Upravljanje](high-performance-computing/upravljanje){:target="_blank"} | [V3-openMPI](high-performance-computing/V3-openMPI){:target="_blank"} | [Z3-openMPI](hpc-z3-openMPI){:target="_blank"} |
|  4. | [Tehnologije](high-performance-computing/tehnologije){:target="_blank"} | [V4-openMPI](high-performance-computing/V4-openMPI){:target="_blank"} | [Z4-openMPI](hpc-z4-openMPI){:target="_blank"} |
|  5. |    [Problemi](high-performance-computing/problemi){:target="_blank"}    | [V5-openMPI](high-performance-computing/V5-openMPI){:target="_blank"} | [Z5-openMPI](hpc-z5-openMPI){:target="_blank"} |
|  6. |  [Biblioteke](high-performance-computing/biblioteke){:target="_blank"}  | [V6-openACC](high-performance-computing/V6-openACC){:target="_blank"} | [Z6-openACC](hpc-z6-openACC){:target="_blank"} |
|  7. |   [Algoritmi](high-performance-computing/algoritmi){:target="_blank"}   | [V7-openACC](high-performance-computing/V7-openACC){:target="_blank"} | [Z7-openACC](hpc-z7-openACC){:target="_blank"} |
{:.scroll-table}

- [Literatura](hpc-literatura){:target="_blank"}

#### HPC Short Courses (C)



|--------------------------------------------------------------------------------|------------------------------------------------------|
| [OpenMP presentation](hpc-short-courses/openmp-presentation){:target="_blank"} | [OpenMP training](openmp-training){:target="_blank"} |
| [MPI presentation](hpc-short-courses/mpi-presentation){:target="_blank"}       | [MPI training](mpi-training){:target="_blank"}       |



### Markdown-it 

  - [Api documentation](https://milovantomasevic.github.io/markdown-it/){:target="_blank"}{:.heading.flip-title} --- GitHub.
  - Online editor --- Learning the syntax.
    - [Demo](https://markdown-it.github.io){:target="_blank"}
    - [Demo 2](https://pandao.github.io/editor.md/en.html){:target="_blank"}
    - [Demo 3](https://dillinger.io){:target="_blank"}
    - [Demo 4](https://stackedit.io/app#){:target="_blank"}
    - [Demo 5](https://markdownlivepreview.com){:target="_blank"}
    - [HTML to Markdown](https://www.browserling.com/tools/html-to-markdown){:target="_blank"}

  - Online slides --- Examples online presentation.
    - [Example](https://remarkjs.com/){:target="_blank"}
    - [Example 2](https://revealjs.com/){:target="_blank"}
    - [Example 3](https://murmuring-sierra-54081.herokuapp.com/stash/edit/royal-pine){:target="_blank"}
{:.related-posts.faded}

## Delavnice
### PhD Presentation (in Serbian)


- [Presentation at FIS](/courses/fis/PhDfis.html){:target="_blank"}{:.heading.flip-title} --- PC & Mobile view.
- [Defense at FTS](/courses/PhD-MT/index.html){:target="_blank"}{:.heading.flip-title} --- PC view.
{:.related-posts.faded}

### FIS Presentation (in Serbian)

- Prezentacija prikazuje zašto uspešno izvršavamo obaveze svih 10 godina !
	- [Budi student FIŠ-a](/courses/fis/fis.html){:target="_blank"}{:.heading.flip-title} --- PC & Mobile view.
{:.related-posts.faded}



{% comment %} 

{% plantuml %}

skinparam sequenceArrowThickness 2
skinparam roundcorner 20
skinparam maxmessagesize 60
skinparam sequenceParticipant underline

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoWork
activate A

A -> B: Create Request
activate B

B -> C: DoWork
activate C
C --> B: WorkDone
destroy C

B --> A: Request Created
deactivate B

A --> User: Done
deactivate A

@enduml

@startuml
skinparam backgroundColor #EEEBDC
skinparam handwritten true

skinparam sequence {
	ArrowColor DeepSkyBlue
	ActorBorderColor DeepSkyBlue
	LifeLineBorderColor blue
	LifeLineBackgroundColor #A9DCDF
	
	ParticipantBorderColor DeepSkyBlue
	ParticipantBackgroundColor DodgerBlue
	ParticipantFontName Impact
	ParticipantFontSize 17
	ParticipantFontColor #A9DCDF
	
	ActorBackgroundColor aqua
	ActorFontColor DeepSkyBlue
	ActorFontSize 17
	ActorFontName Aapex
}

actor User
participant "First Class" as A
participant "Second Class" as B
participant "Last Class" as C

User -> A: DoWork
activate A

A -> B: Create Request
activate B

B -> C: DoWork
activate C
C --> B: WorkDone
destroy C

B --> A: Request Created
deactivate B

A --> User: Done
deactivate A

{% endplantuml %}

{% endcomment %}
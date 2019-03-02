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

<script src="http://platform.linkedin.com/in.js" type="text/javascript"></script>
<script type="IN/MemberProfile" data-id="http://www.linkedin.com/in/phdmilovantomasevic/" data-format="inline" data-width="400"></script>


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
{:.related-posts.faded}

  
  - [PyhtonPro](/tech/python_napredni.html){:target="_blank"}{:.heading.flip-title} --- Advanced level.
{:.related-posts.faded}

#### Python-Design-Patterns


| __Creational Patterns__ | [abstract_factory](python-design-patterns-abstract_factory){:target="_blank"} | [borg](python-design-patterns-borg){:target="_blank"} | [builder](python-design-patterns-builder){:target="_blank"}| [factory_method](python-design-patterns-factory_method){:target="_blank"} | [lazy_evaluation](python-design-patterns-lazy_evaluation){:target="_blank"} | [pool](python-design-patterns-pool){:target="_blank"} |[prototype](python-design-patterns-prototype){:target="_blank"} |
|-----------------|--------------|--------------|-----------------|--------------|--------------|--------------|
| __Description__ | use a generic function with specific factories  |   a singleton with shared-state among instances   | instead of using multiple constructors, builder object receives parameters and returns constructed objects  | delegate a specialized function/method to create instances   |   lazily-evaluated property pattern in Python    |   preinstantiate and maintain a group of instances of the same type  | use a factory and clones of a prototype for new instances (if instantiation is expensive)
{:.flip-table}

| __Structural Patterns__ | [3-tier](python-design-patterns-3-tier){:target="_blank"} | [adapter](python-design-patterns-adapter){:target="_blank"} | [bridge](python-design-patterns-bridge){:target="_blank"} | [composite](python-design-patterns-composite){:target="_blank"} |[decorator](python-design-patterns-decorator){:target="_blank"} | [facade](python-design-patterns-facade){:target="_blank"} | [flyweight](python-design-patterns-flyweight){:target="_blank"} | [front_controller](python-design-patterns-front_controller){:target="_blank"} | [mvc](python-design-patterns-mvc){:target="_blank"} | [proxy](python-design-patterns-proxy){:target="_blank"} |
|--------|------|
 __Description__ | data<->business logic<->presentation separation (strict relationships) |  adapt one interface to another using a white-list  | a client-provider middleman to soften interface changes  | lets clients treat individual objects and compositions uniformly   |   wrap functionality with other functionality in order to affect outputs    |   use one class as an API to a number of others  | transparently reuse existing instances of objects with similar/identical state | single handler requests coming to the application | model<->view<->controller (non-strict relationships) | an object funnels operations to something else |
{:.flip-table}


| __Behavioral Patterns__ | [chain](python-design-patterns-chain){:target="_blank"} | [catalog](python-design-patterns-catalog){:target="_blank"} | [chaining_method](python-design-patterns-chaining_method){:target="_blank"} |[command](python-design-patterns-command){:target="_blank"} | [iterator](python-design-patterns-iterator){:target="_blank"}| [mediator](python-design-patterns-mediator){:target="_blank"} | [memento](python-design-patterns-memento){:target="_blank"} | [observer](python-design-patterns-observer){:target="_blank"} |[publish_subscribe](python-design-patterns-publish_subscribe){:target="_blank"} | [registry](python-design-patterns-registry){:target="_blank"} | [specification](python-design-patterns-specification){:target="_blank"} | [state](python-design-patterns-state){:target="_blank"}| [strategy](python-design-patterns-strategy){:target="_blank"} | [template](python-design-patterns-template){:target="_blank"} | [visitor](python-design-patterns-visitor){:target="_blank"} | 
|--------|------|
| __Description__ | apply a chain of successive handlers to try and process the data |general methods will call different specialized methods based on construction parameter | continue callback next object method | bundle a command and arguments to call later | traverse a container and access the container's elements |   an object that knows how to connect other objects and act as a proxy  | generate an opaque token that can be used to go back to a previous state| provide a callback for notification of events/changes to data | a source syndicates events/data to 0+ registered listeners |   keep track of all subclasses of a given class  | business rules can be recombined by chaining the business rules together using boolean logic | logic is organized into a discrete number of potential states and the next state that can be transitioned to |  selectable operations over the same data | an object imposes a structure but takes pluggable components |invoke a callback for all items of a collection |
{:.flip-table}


| __Design for Testability__ <br> __Patterns__ | [constructor_injection](python-design-patterns-constructor_injection){:target="_blank"} |[parameter_injection](python-design-patterns-parameter_injection){:target="_blank"} | [setter_injection](python-design-patterns-setter_injection){:target="_blank"}|
|--------|------|
| __Description__ | for those of you who would like to use final fields, wish to avoid numerous setters, or dislike private field injection and would like nothing more than to just use  | with parameter manipulation attacks, the attacker modifies the data sent between the client and Web application. This may be data sent using query strings, form fields, cookies, or in HTTP headers.  |the client provides the depended-on object to the SUT via the setter injection (implementation variant of dependency injection)  |
{:.flip-table}


| __Fundamental Patterns__ | [delegation_pattern](python-design-patterns-delegation_pattern){:target="_blank"} |
|--------|------|
| __Description__ | an object handles a request by delegating to a second object (the delegate)  |
{:.flip-table}

| __Others__ | [blackboard](python-design-patterns-blackboard){:target="_blank"} | [graph_search](python-design-patterns-graph_search){:target="_blank"}| [hsm](python-design-patterns-hsm){:target="_blank"} |
|--------|------|
|   __Description__  | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern  | graphing algorithms - non gang of four pattern  | hierarchical state machine - non gang of four pattern  |
{:.flip-table}


### Java

- [Java tutorial for Complete Beginners](java-for-complete-beginners){:target="_blank"} 
- [Java Design Patterns - Example Tutorial](https://github.com/MilovanTomasevic/java-design-patterns){:target="_blank"} 

### DataBase training

|                        **Zadaci**                      |                      **Rešenja**                    |
|:------------------------------------------------------:|:---------------------------------------------------:|
|   [ Z1-Zadaci ](db/z1-zadaci.html){:target="_blank"}   |   [ Z1-Rešenja ](db-z1-resenja){:target="_blank"}   |
|   [ Z2-Zadaci ](db/z2-zadaci.html){:target="_blank"}   |   [ Z2-Rešenja ](db-z2-resenja){:target="_blank"}   |
|   [ Z3-Zadaci ](db/z3-zadaci.html){:target="_blank"}   |   [ Z3-Rešenja ](db-z3-resenja){:target="_blank"}   |
|   [ Z4-Zadaci ](db/z4-zadaci.html){:target="_blank"}   |   [ Z4-Rešenja ](db-z4-resenja){:target="_blank"}   |
|   [ Z5-Zadaci ](db/z5-zadaci.html){:target="_blank"}   |   [ Z5-Rešenja ](db-z5-resenja){:target="_blank"}   |
|   [ Z6-Zadaci ](db/z6-zadaci.html){:target="_blank"}   |   [ Z6-Rešenja ](db-z6-resenja){:target="_blank"}   |
|   [ Z7-Zadaci ](db/z7-zadaci.html){:target="_blank"}   |   [ Z7-Rešenja ](db-z7-resenja){:target="_blank"}   |
|   [ Z8-Zadaci ](db/z8-zadaci.html){:target="_blank"}   |   [ Z8-Rešenja ](db-z8-resenja){:target="_blank"}   |
|   [ Z9-Zadaci ](db/z9-zadaci.html){:target="_blank"}   |   [ Z9-Rešenja ](db-z9-resenja){:target="_blank"}   |
|  [ Z10-Zadaci ](db/z10-zadaci.html){:target="_blank"}  |  [ Z10-Rešenja ](db-z10-resenja){:target="_blank"}  |
|  [ Z11-Zadaci ](db/z11-zadaci.html){:target="_blank"}  |  [ Z11-Rešenja ](db-z11-resenja){:target="_blank"}  |
|  [ Z12-Zadaci ](db/z12-zadaci.html){:target="_blank"}  |  [ Z12-Rešenja ](db-z12-resenja){:target="_blank"}  |
| [ Test-Zadaci ](db/test-zadaci.html){:target="_blank"} | [ Test-Rešenja ](db-test-resenja){:target="_blank"} |

- <a target="_blank" rel="noopener noreferrer" href="/courses/db/sema.html"> ☛ `Šema baze podataka`</a>
- <a target="_blank" rel="noopener noreferrer" href="/courses/db-mySQL.sql/"> ☛ skripta-`mySQL.sql`</a>

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


#### First settings
- [Installation, Compilation & Running OpenMP/MPI/OpenACC and HPC Rudolf connection](/courses/hpc-setup){:target="_blank"}

#### HPC Complete Courses (C)
<br>


| HPC |                                 Teroija                                 |                                 Vežbe                                 |                     Zadaci                     |
|:---:|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|:----------------------------------------------:|
|  1. |        [Uvod](high-performance-computing/uvod.html){:target="_blank"}        |  [V1-openMP](high-performance-computing/V1-openMP.html){:target="_blank"}  |  [Z1-openMP](hpc-z1-openMP){:target="_blank"}  |
|  2. | [Arhitektura](high-performance-computing/arhitektura.html){:target="_blank"} |  [V2-openMP](high-performance-computing/V2-openMP.html){:target="_blank"}  |  [Z2-openMP](hpc-z2-openMP){:target="_blank"}  |
|  3. | [Upravljanje](high-performance-computing/upravljanje.html){:target="_blank"} | [V3-openMPI](high-performance-computing/V3-openMPI.html){:target="_blank"} | [Z3-openMPI](hpc-z3-openMPI){:target="_blank"} |
|  4. | [Tehnologije](high-performance-computing/tehnologije.html){:target="_blank"} | [V4-openMPI](high-performance-computing/V4-openMPI.html){:target="_blank"} | [Z4-openMPI](hpc-z4-openMPI){:target="_blank"} |
|  5. |    [Problemi](high-performance-computing/problemi.html){:target="_blank"}    | [V5-openMPI](high-performance-computing/V5-openMPI.html){:target="_blank"} | [Z5-openMPI](hpc-z5-openMPI){:target="_blank"} |
|  6. |  [Biblioteke](high-performance-computing/biblioteke.html){:target="_blank"}  | [V6-openACC](high-performance-computing/V6-openACC.html){:target="_blank"} | [Z6-openACC](hpc-z6-openACC){:target="_blank"} |
|  7. |   [Algoritmi](high-performance-computing/algoritmi.html){:target="_blank"}   | [V7-openACC](high-performance-computing/V7-openACC.html){:target="_blank"} | [Z7-openACC](hpc-z7-openACC){:target="_blank"} |
{:.scroll-table}

- [Literatura](hpc-literatura){:target="_blank"}

#### HPC Short Courses (C)
<br>

|:------------------------------------------------------------------------------:|:----------------------------------------------------:|
| [OpenMP presentation](hpc-short-courses/openmp-presentation.html){:target="_blank"} | [OpenMP training](openmp-training){:target="_blank"} |
|    [MPI presentation](hpc-short-courses/mpi-presentation.html){:target="_blank"}    |    [MPI training](mpi-training){:target="_blank"}    |



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
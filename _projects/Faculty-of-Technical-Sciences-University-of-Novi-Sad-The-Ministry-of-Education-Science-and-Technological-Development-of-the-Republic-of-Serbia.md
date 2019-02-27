---
layout: project
title: 'Development of software for managing the installation and repair of braking systems for rail vehicles'
date: 1 Jan 2012
image: /assets/img/projects/ministarstvoobrazovanja1.jpg
screenshot: /assets/img/projects/ministarstvoobrazovanja1.jpg
links:
  - title: Website
    url: http://www.mpn.gov.rs/
  - title: Demo
    url: http://bscms.golushin.co.rs/
caption: Ministry of Science, Republic of Serbia
description: >
  Milovan Tomašević worked as a researcher at the Faculty of Technical Sciences within the project "Development of software for managing the installation ...
hide_description: true
accent_image: /assets/img/ftn-sc.gif
accent_color: rgb(255,127,80)
---

Milovan Tomašević worked as a researcher at the [_Faculty of Technical Sciences_](http://ftn.uns.ac.rs/n1386094394/faculty-of-technical-sciences) within the project _"Development of software for managing the installation and repair of braking systems for rail vehicles", the Ministry of Science, Republic of Serbia, no. 035 050 for the period 2011-2017th years_.

![](/assets/img/projects/meeting.jpg)
Handshaking with Dragutin Zelenović and Ilija Ćosić PhD, Professor emeritus (Dean was 13 years - [_Faculty of Technical Sciences_](http://ftn.uns.ac.rs/n1386094394/faculty-of-technical-sciences))
{:.figure}

>Dragutin Zelenović (Serbian: Драгутин Зеленовић; born 19 May 1928) is a Serbian university professor, correspondent member of Serbian Academy of Sciences and Arts and politician. He served as the Prime Minister of Serbia in 1991. He also served as the member of the Presidency of Yugoslavia from 1989 to 1991.<br>He was a professor at the Faculty of Technical Sciences and Rector of the University of Novi Sad (1987–89). He is also a member of the Serbian Academy of Arts and Sciences since 1987.

Responsibilities:  
- In the phase of application software development data was collected and research was conducted on the process management software modeling.
After research and representation of the system model specification for management,
- implementation and testing of the system was made as well as training of the users in the company.


>My job consisted of going to work to get familiar with the business itself. In the company where the project was developed, I got instructions from the CEO for each sector and was introduced to the manager of each one, who furthermore provided me with detailed specifications that I documented.<br>This arrangement allowed me to learn that the first phase always consists of becoming familiar with the current stage (procedures, business itself), and the next step, phase 2 is the making of the specifications of the model: the concept, database model, activity diagram, usage and purpose, as well as the information access rights in accordance with the RBAC model.<br>The test version of the system was checked by entering data from the company and verifying whether it functions in accordance with the goal.<br>After that, the final version was presented to a team of experts, managers, as well as employees.<br>The next step was employee training in all sectors.<br>I was in charge of supervision during the probation period in the duration of 10 days.<br>After that, the system was released into production.

![](/assets/img/projects/workDay.JPG)
Office Productivity: A Work in Progress
{:.figure}

Performing exercises with an accredited degree program (Department: Electrical engineering, Department of Software and Information Technology) in the Project Management.
He informed the students:
- Needs, objectives and applications of the concept of Project Management.

Development of the project in MS Project and documentation, consisting of the above document:
- The project design,
- Instruction for allocation of ID projects,
- Project Definition,
- Report on the status of the project,
- The decision to accept the results of the project,
- Instructions for filing of project documentation.

Detailed knowledge of the procedures:
- The procedure for the project implementation,
- The procedure for creating and monitoring the implementation of the project plan and the ICT budget.

![](/assets/img/projects/mt.jpg)
While I teach my students
{:.figure}



## Started and completed his PhD in the project
{:.no_toc}
1. this unordered seed list will be replaced by toc as unordered list
{:toc}

I enrolled my doctoral studies in the Department of engineering management, with the thesis _‘Adaptive model for supply chains management in small and medium enterprises’_.

**_You can see the PhD presentation [here](../PhD-MT/index.html){:target="_blank"}._**


![](/assets/img/projects/mt_phd.png)
**A**daptive **M**odel **for** **S**upply **C**hains **M**anagement (_AM4SCM_)
{:.figure}


This model is a complex system that unifies functional and semi functional business processes, and that enables participants in the supply chain to manage these processes in real time. 

It consists of 3 models:
1. Supply chains management model (_BSCMS_)
1. Customers’ inquiries management model (_Service desk_)
1. Quality of service assessment model (_FAM4QS_)

The hierarchy structure of the **A**daptive **M**odel **for** **S**upply **C**hains **M**anagement (_AM4SCM_) consists of 7 levels of activity and feedback that enable the constant improvement of _AM4SCM_.

### Level 1 - system analysis (_AM4SCM_)

Using the system analysis, it should enable, define and synchronize following activities:
- assessment of the actual condition of the IT system
- definition of the starting point of information generation 
- definition of potential users
- determining the level of access to the information

### Level 2 - Basic Supply Chains Management System (_AM4SCM_)

The general model of the supply chains management contains the majority of business functions.

### Level 3 - Selected models(_AM4SCM_)

On this level the system adjusts to the needs of the respective user by choosing the functions from the previous level, if they exist – if not, they can be created.

### Level 4 - Definitions (_AM4SCM_)

It consists of 4 steps:
1. Defining a partner
1. Defining data and documents needed for business
1. Defining rules on information transfer
1. Information access control

### Level 5 - The system is released (_AM4SCM_)

Chosen processes are implemented and adjusted to the respective enterprise on this level.

### Level 6 - Service Desk (_AM4SCM_)

This level is the integration of the system with the service desk that makes a single point of contact.

![](/assets/img/projects/sd.png)
Service Desk
{:.figure}

### Level 7 - _FAM4QS_ - **F**uzzy **A**ggregation **M**ethod **for** **Q**uality **S**ervice – software  (_AM4SCM_)

Mathematical method ( _FAM4QS_ - **F**uzzy **A**ggregation **M**ethod **for** **Q**uality **S**ervice – software)
- The quality assessment of the service (chain-system), based on:
    - the analysis of customers’ inquiries/problems from level 6
    - the creation of parameters based on the quality defining criteria
    - the model ranks services from worst to best

- Supply chains with bad ranking are improved with the analysis of the results of compared services with 7 levels, as well as with the experiences from good supply chains in order to improve results.

- Problem solving on any level is conducted based on information and experience from previous levels.

- This model is constantly improved circularly through levels.


![](/assets/img/projects/FAM4QS.png)
FAM4QS Algorithm
{:.figure}

~~~csharp
private void CalculateFAM4QS()
        {
            CollectScores();
            var subgroups = Groups.Keys.Where(x => !x.Equals(Const.MainGroupName)).ToList();
            foreach (var subgroupName in subgroups)
            {
                var subgroup = Groups[subgroupName];
                var selectedR = subgroup.RList.Where(x => x.IsSelected).ToList();
                if (selectedR.Count <= 0)
                {
                    //We must have at least one r selected for every subgroup and for the main group
                    //If there are any missing, we will show an error message to the user, and cancel further calculation
                    string message = $"No R selected for {subgroupName}";
                    string caption = "Error";
                    MessageBoxButtons buttons = MessageBoxButtons.OK;
                    MessageBox.Show(message, caption, buttons);
                    return;
                }

                var services = subgroup.Services;
                foreach (var service in services.Values)
                {
                    //clear any previous data
                    service.KrispCalculation.Clear();
                    service.FuzzyCalculations.Clear();
                    foreach (var r in selectedR)
                    {
                        //if (WeightType == NumberType.Krisp)
                        if (subgroup.WeightType == NumberType.Krisp)
                        {
                            KrispWeightCalc(service, r, subgroup.Weights);
                        }
                        else
                        {
                            FuzzyWeightCalc(service, r, subgroup.Weights, subgroup.ScoreType);
                        }
                    }
                }
            }
 ~~~           
FAM4QS Algorithm (program code - C#)
{:.figure}


>The basic research problem of this dissertation is the development of supply chain management (SCM) model in order to improve the quality of service.<br>Therefore, an adaptive SCM model has been developed that consists of a model for: SCM , management of user requirements and assessment of the quality of service provided.<br>For the purpose of application the adaptive model, it is presented an algorithm with precisely defined steps that the user needs to implement in order to raise the level of service quality and maintain the stability of supply.<br>The model verification was done on the example of 17 supply chains in the territory of the Republic of Serbia, which resulted in answers on how to improve the quality of the service.<br>The contribution of the research is reflected in the possibility of direct application of the developed model and providing new information for the scientific and professional public, which can represent a quality basis for the further development of the SCM model.

![](/assets/img/projects/phd.jpeg)
PhD candidate, Faculty of Technical Sciences, University of Novi Sad, Serbia
{:.figure}
---
layout: page
title: Step by step to HPC rudolf connection
description: >
  High-performance computing (HPC)
hide_description: true

---

```consile
# First create a source file in /etc/apt/sources.list.d/nordugrid.list
# apend 
# Base channel - must be enabled
deb http://download.nordugrid.org/repos/15.03/ubuntu/ zesty main
deb-src http://download.nordugrid.org/repos/15.03/ubuntu/ zesty main

# Updates to the base release - should be enabled

deb http://download.nordugrid.org/repos/15.03/ubuntu/ zesty-updates main
deb-src http://download.nordugrid.org/repos/15.03/ubuntu/ zesty-updates main

```

```consile
# Scheduled package updates - optional
#deb http://download.nordugrid.org/repos/15.03/ubuntu/ zesty-experimental main
#deb-src http://download.nordugrid.org/repos/15.03/ubuntu/ zesty-experimental main
```

```consile
# Import the apt-key:
wget -q -O - http://download.nordugrid.org/DEB-GPG-KEY-nordugrid.asc \
 | sudo apt-key add -



wget -q -O - http://download.nordugrid.org/DEB-GPG-KEY-nordugrid.asc \
 | sudo apt-key add -
```

```consile
# Install ARC client:

sudo apt-get update
sudo apt-get install nordugrid-arc-client nordugrid-arc-plugins-globus
```

```consile
# Add EGI-trustanchors and install CA-s /etc/apt/sources.list.d/EGI-trustanchors.list *** 0

#append these lines
#### EGI Trust Anchor Distribution ####

deb http://repository.egi.eu/sw/production/cas/1/current egi-igtf core 
```

```consile
# Import key

wget -q -O - \ 
https://dist.eugridpma.info/distribution/igtf/current/GPG-KEY-EUGridPMA-RPM-3\
 | sudo apt-key add -
```

```consile
#tale je OK  *** 1

wget -q -O - \
     https://dist.eugridpma.info/distribution/igtf/current/GPG-KEY-EUGridPMA-RPM-3 \
     | sudo apt-key add -
```

```consile
# Install CA-s: *** 2

sudo apt-get update
sudo apt-get install ca-policy-egi-core fetch-crl
```


```consile
# Now you need to transform the certiciate and key in .pem format, make sure the key is only readable # by you and move both files in your ~/.arc  directory:

~/.arc/

/home/<username>/.arc/usercert.pem
/home/<username>/.arc/userkey.pem

openssl pkcs12 -in usercert.p12 -clcerts -nokeys -out usercert.pem
openssl pkcs12 -in usercert.p12 -nocerts -out userkey.pem
chmod 400 userkey.pem
chmod 644 usercert.pem
```

```consile
# create .arc/vomses/hpc.fis.unm.si file and insert:

"hpc.fis.unm.si" "voms.sling.si" "15005" "/C=SI/O=SiGNET/O=SLING/CN=voms.sling.si" "hpc.fis.unm.si"
```

```consile
# create .arc/vomsdir/hpc.fis.unm.si file and insert:

/C=SI/O=SiGNET/O=SLING/CN=voms.sling.si
/C=SI/O=SiGNET/CN=SiGNET CA
```

```consile
arcproxy -C .arc/cert.pem -K .arc/key.pem -s .arc/vomsdir -V .arc/vomses
arcproxy -C ~/.arc/usercert.pem -K ~/.arc/userkey.pem -s ~/.arc/vomsdir -V ~/.arc/vomses
```

```consile
# HPC connect 

arcproxy -S hpc.fis.unm.si

arcproxy -C .arc/cert.pem -K .arc/key.pem -s .arc/vomsdir -V .arc/vomses

arcproxy -C ~/.arc/usercert.pem -K ~/.arc/userkey.pem -s ~/.arc/vomsdir -V ~/.arc/vomses


```

```consile
# Connected
mt@mt:~/hpc$ arcproxy -S hpc.fis.unm.si
Enter pass phrase for private key:
Your identity: /C=SI/O=SiGNET/O=FIS Novo mesto/OU=HPC Rudolf/CN=Milovan Tomasevic
Contacting VOMS server (named hpc.fis.unm.si): voms.sling.si on port: 15005
Proxy generation succeeded
Your proxy is valid until: 2019-02-13 12:03:53
```

```consile

# arc

man arcsub

arcsub -c jost.arnes.si -o joblist.xml name.xrsl

arcstat gsiftp://jost.arnes.si:2811/jobs/<-ID->

# example
arcstat gsiftp://jost.arnes.si:2811/jobs/SAVLDmDkUAonmmR0Xox1SiGmABFKDmABFKDmuZFKDmABFKDmPIfaUm
Job: gsiftp://jost.arnes.si:2811/jobs/SAVLDmDkUAonmmR0Xox1SiGmABFKDmABFKDmuZFKDmABFKDmPIfaUm
Name: test
State: Finished
Exit Code: 0

Status of 1 jobs was queried, 1 jobs returned information


 arcstat --all

# When it's finished
arcget gsiftp://jost.arnes.si:2811/jobs/<-ID->

# example
$ arcget gsiftp://jost.arnes.si:2811/jobs/SAVLDmDkUAonmmR0Xox1SiGmABFKDmABFKDmuZFKDmABFKDmPIfaUm
Results stored at: SAVLDmDkUAonmmR0Xox1SiGmABFKDmABFKDmuZFKDmABFKDmPIfaUm
Jobs processed: 1, successfully retrieved: 1, successfully cleaned: 1

$ ls SAVLDmDkUAonmmR0Xox1SiGmABFKDmABFKDmuZFKDmABFKDmPIfaUm/
log  test.log


```console
# Example of a task in C:

# example.c and example.sh must be in the directory from which you will send the task.

# First, prepare a description of the task prime-number.xrsl

& 
(executable="prime-number.sh")
(inputfiles=
("prime-number.sh" "")
("prime-number.c" "")
)
(stdout="prime-number.txt")
(stderr="prime-number.err")
(gmlog="gridlog")
(jobname="NalogaC")
(runtimeenvironment = "APPS/BASE/OPENMPI-2.1")

```

```c

// prime-number.c

#include<stdio.h>
 
int main()
{
   int n = 1000, i = 3, count, c;
 
   if ( n >= 1 )
   {
      printf("First %d prime numbers are :\n",n);
      printf("2\n");
   }
 
   for ( count = 2 ; count <= n ;  )
   {
      for ( c = 2 ; c <= i - 1 ; c++ )
      {
         if ( i%c == 0 )
            break;
      }
      if ( c == i )
      {
         printf("%d\n",i);
         count++;
      }
      i++;
   }
 
   return 0;
}

```


```sh

# prime-number.sh

#!/bin/sh
date 
gcc prime-number.c -o primenumber
./primenumber
date

```


```console

# Example of a task in Python:

# vsota.xrsl

&
(executable="vsota.sh")
(inputfiles=
("vsota.sh" "vsota.sh")
("vsota.py" "vsota.py")
)
(outputfiles=("/"  " ")
)
(stdout="out.txt")
(stderr="err.txt")
(gmlog="vsota.log")
(jobName="vsota")
 (runtimeenvironment = "APPS/FIS/DEFAULT")

```

```py

# vsota.py

sum = 0
print "Printout numbers: "
for x in ["1", "1050","164999"]: print x
print "Number of numbers "
for y in [1,1050,164999]: sum=sum+y
print sum

```


```sh

# vsota.sh

#!/bin/sh
python vsota.py

```


# MPI

```console

# hellompi.xrsl

&
(count = 4)
(jobname = "hellompi")
(inputfiles =
  ("hellompi.sh" "")
  ("hellompi.c" "")
)
(executable = "hellompi.sh")
(stdout = "hellompi.log")
(join = yes)
(walltime = "15 minutes")
(gmlog = log)
(memory = 2000)
(runtimeenvironment = "APPS/FIS/MPI-1.8")

```


```c

/* C Example */
#include <stdio.h>
#include <mpi.h> 


int main (argc, argv)
     int argc;
     char *argv[];
{
  int rank, size;

  MPI_Init (&argc, &argv);      /* starts MPI */
  MPI_Comm_rank (MPI_COMM_WORLD, &rank);        /* get current process id */
  MPI_Comm_size (MPI_COMM_WORLD, &size);        /* get number of processes */
  printf( "Hello world from process %d of %d\n", rank, size );
  MPI_Finalize();
  return 0;
}

```

```console

# hellompi.sh:

#!/bin/bash
date
hostname
echo "Compiling example"
mpicc -o hello hellompi.c
echo "Done."
echo "Running example:"
mpiexec -np 1 ${PWD}/hello
echo "Done."
date

```
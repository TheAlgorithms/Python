Python’s **psutil** module provides an interface with all the PC resources and processes.

We can get some info about the CPU since the boot time like we can information of Hoe many system calls etc...

First things first, we need to install psutil module:
``` pip install psutil```

## PC resources information
We can get our PC's current system state information.
In computing, a system call is the programmatic way in which a computer program requests a service from the kernel of the operating system it is executed on. A system call is a way for programs to interact with the operating system.
```
>>> import psutil
>>> psutil.cpu_stats()
scpustats(ctx_switches=146394627, interrupts=117999888, soft_interrupts=0, syscalls=453854910)
```




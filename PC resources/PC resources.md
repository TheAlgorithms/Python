Python’s **psutil** module provides an interface with all the PC resources and processes.

We can get some info about the CPU since the boot time like we can information of Hoe many system calls etc...

First things first, we need to install psutil module:
``` pip install psutil```

## PC resources information
We can get our PC's current system state information.
```
>>> import psutil
>>> psutil.cpu_stats()
scpustats(ctx_switches=146394627, interrupts=117999888, soft_interrupts=0, syscalls=453854910)
```
- ctx_switches = context switches
- sys_calls = system calls 
You can get more details about [context switches](http://www.linfo.org/context_switch.html) and [system calls](https://www.geeksforgeeks.org/operating-system-introduction-system-call/) here.





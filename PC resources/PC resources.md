Python’s **psutil** module provides an interface with all the PC resources and processes.

We can get some info about the CPU since the boot time like we can information of Hoe many system calls etc...

First things first, we need to install psutil module:
``` C:\Users\Hashish\Desktop> **pip install psutil**```

## PC resources information
We can get our PC's current system state information.
```
>>> import psutil
>>> psutil.cpu_stats()
scpustats(ctx_switches=146394627, interrupts=117999888, soft_interrupts=0, syscalls=453854910)
```
- ctx_switches = no.of context switches from last boot.
- sys_calls = system calls. 
You can get more details about [context switches](http://www.linfo.org/context_switch.html) and [system calls](https://www.geeksforgeeks.org/operating-system-introduction-system-call/) here.

## Information about the disk and memory state:
```
>>> import psutil
>>> psutil.disk_usage("F:")
sdiskusage(total=214748360704, used=170450833408, free=44297527296, percent=79.4)
>>> psutil.virtual_memory()
svmem(total=8470630400, available=3693641728, percent=56.4, used=4776988672, free=3693641728)
```
## Battery Life
```
>>> import psutil
>>> psutil.sensors_battery()
sbattery(percent=100, secsleft=<BatteryTime.POWER_TIME_UNLIMITED: -2>, power_plugged=True)
```
## Temperature of CPU
```
>>> import psutil
>>> psutil..sensors_temperatures()
{'ACPI\\ThermalZone\\THM0_0': [shwtemp(label='', current=49.05000000000001, high=127.05000000000001, critical=127.05000000000001)]}
```






from __future__ import print_function

try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3
    
high=0
for a in xrange(1,100):
    for b in xrange(1,100):
        c=0
        for k in list(str(a**b)):
            c+=int(k)
        if c>high:
            high=c

print(high)
#972--answer

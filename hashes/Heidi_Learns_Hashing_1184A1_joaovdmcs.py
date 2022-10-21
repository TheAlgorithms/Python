r = int(raw_input())

if (r>3) and (((r-3)%2) == 0):
  print "1 %i" % ((r-3)/2)
else:
  print "NO"  

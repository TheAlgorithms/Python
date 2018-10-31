def swap(a,b):
   t=a;
   a=b;
   b=t;
   print "value of a inside the function: :",a
   print "value of b inside the function: ",b
   return(a,b)
# Now we can call swap function
a=50
b=75
print "value of a before sending to function: ",a
print "value of b before sending to function: ",b
x=swap(a,b)
print "value of a after sending to function: ", x[0]
print "value of b after sending to function: ",x[1]

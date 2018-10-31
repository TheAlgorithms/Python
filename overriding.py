class A(object): 
   def disp(self): 
      print "Base Class"  
class B(A): 
   def disp(self): 
      print "Derived Class"  
x = A() 
y = B()  
x.disp() 
y.disp()

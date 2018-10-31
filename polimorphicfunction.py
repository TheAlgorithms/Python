class A(object): 
   def show(self): 
      print "A class method is called" 
  
class B(A): 
   def show(self): 
      print "B class method is called" 
  
def checkmethod(clasmethod): 
   clasmethod.show()  

AObj = A() 
BObj = B() 
  
checkmethod(AObj) 
checkmethod(BObj)

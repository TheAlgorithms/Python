import weakref

class my_list(list):
   pass

new_list = my_list('String') #Use my_list class to define a list
print(new_list)

weak_ref = weakref.ref(new_list)

new_weak_list = weak_ref()
new_proxy = weakref.proxy(new_list)

print(new_weak_list)
print('The object using proxy: ' + str(new_proxy))

if new_list is new_weak_list:
   print("There is a weak reference")
    
print('The Number of Weak references: ' + str(weakref.getweakrefcount(new_list)))
    
del new_list, new_weak_list #Delete both objects
print("The weak reference is: " + str(weak_ref()))

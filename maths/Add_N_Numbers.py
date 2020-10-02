#How to add N numbers
def add_N(*a):
    no_list=[*a]
    try:
        value=sum(no_list)
        print('Sum is  '+ str(value))
    except:
        print('Addition invalid')
  
add_N(1,2,3,6,7) # Output is 19

add_N(5,6,7) #Output is 18

add_N(80+70+3+3+5+5+12) # output is 178

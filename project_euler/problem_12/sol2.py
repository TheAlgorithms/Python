def triangle_number_generator(): 
    for n in range(1,1000000):
        yield n*(n+1)//2
        
def count_divisors(n): 
    return sum([2 for i in range(1,int(n**0.5)+1) if n%i==0 and i*i != n])

print(next(i for i in triangle_number_generator() if count_divisors(i) > 500))

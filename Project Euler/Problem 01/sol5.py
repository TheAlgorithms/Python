number=3
result=0
while number<1000:
  if(number%3==0 or number%5==0):
    result+=number
  elif(number%15==0):
    result-=number
  number+=1
print(result)

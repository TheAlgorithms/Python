from datetime import datetime

lt = list()
n = int(input("Enter the range: "))
for i in range(n):
    lt.append(input())
print("In ascending order: ")
lt.sort(key=lambda date: datetime.strptime(date, "%d/%b/%Y"))
print(lt)
print("In descending order: ")
lt.sort(key=lambda date: datetime.strptime(date, "%d/%b/%Y"), reverse=True)
print(lt)

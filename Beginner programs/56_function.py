def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1=[45,64,56,76]
percentage1=(sum(marks1)/400)*100

marks2=[67,34,78,43]
percentage2=(sum(marks2)/400)*100

print(percentage1,percentage2)
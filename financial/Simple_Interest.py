#Program to calculate the simple interest in python
print("Find Principal, Rate, Time, Simple Interest if any three of them are given.")
print("Select num according to what is unknown to you:")
print("num 1= Principal\nnum 2= Rate\nnum 3= Time\nnum 4= Simple Interest")
num=int(input("Enter num:"))
if num==1:
    r=float(input("Enter Rate(%): "))
    t=float(input("Enter Time(years): "))
    SI=float(input("Enter Simple Interest(Rs.):"))
    p=(SI*100)/(r*t)
    print("Principal is: ","Rs.",p)
elif num==2:
    p=float(input("Enter Principal(Rs.): "))
    t=float(input("Enter Time(years): "))
    SI=float(input("Enter Simple Interest(Rs.):"))
    r=(SI*100)/(p*t)
    print("Rate is: ",r,"%")
elif num==3:
    p=float(input("Enter Principal(Rs.): "))
    r=float(input("Enter Rate(%): "))
    SI=float(input("Enter Simple Interest(Rs.):"))
    t=(SI*100)/(p*r)
    print("Time is: ",t,"years")
elif num==4:
    p=float(input("Enter Principal(Rs.): "))
    r=float(input("Enter Rate(%): "))
    t=float(input("Enter Time(years): "))
    SI=(p*r*t)/100
    print("Simple interest is: ","Rs.",SI)

import math

i = 1
while i == 1:
    mode = input(
        "What will we use to count area of circle? Length of circumference[l], Radius[r] or Diameter[d]?: "
    )
    if mode == "d" or mode == "D":
        d = input("What diameter of circle: ")
        s = (math.pi * math.pow(int(d), 2)) / 4
        print("Area of circle is: ", s)
        break
    elif mode == "r" or mode == "R":
        r = input("What radius of circle: ")
        s = math.pi * (math.pow(int(r), 2))
        print("Area of circle is:", s)
        break
    elif mode == "l" or mode == "L":
        l = input("What length of circumference: ")
        s = math.pow(int(l), 2) / (math.pi * 4)
        print("Area of circle is:", s)
        break
    else:
        print("Wrong input. Try again")

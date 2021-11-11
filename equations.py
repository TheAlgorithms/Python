# by @JymPatel


# edited by ... (editors can put their name and thanks for suggestion) :)
# @bupboi1337


# what we are going to do
print("We can solve the below equations")
print("1  Quadratic Equation")

# ask what they want to solve
sin = input("What you would like to solve?")

# for Qdc Eqn
if sin == '1':
    print("We will solve for equation 'a(x^2) + b(x) + c'")

    # take some user input
    a = int(input("What is value of a?"))
    b = int(input("What is value of b?"))
    c = int(input("What is value of c?"))

    D = b**2 - 4*a*c

    if D < 0:
        print("No real values of x satisfies your equation.")

    else:
        x1 = (-b + D)/(2*a)
        x2 = (-b - D)/(2*a)

        print("Roots for your equation are" , x1, "&", x2) # output root numbers for equation
        

        
# for Lnr Eqn (2 var)        
if sin == '2' :
    print("We will solve for equations a1(x) + b1(y) + c1 & a2(x) + b2(y) + c2")
    
    # take some more user input
    a1 = int(input("Put value of a1"))
    b1 = int(input("Put value of b1"))
    c1 = int(input("Put value of c1"))
    a2 = int(input("Put value of a2"))
    b2 = int(input("Put value of b2"))
    c2 = int(input("Put value of c2"))
    
    # for infinite or no solution
    if (a1/a2) == (b1/b2) :
        if (a1/a2) == (c1/c2) :
            print("Infinite set of values satisfies your equation.")
        if (a1/a2) != (c1/c2) :
            print("No values of variables satisfies your equation.")
    
    else :
        x = (b2*c1 - b1*c2)/(a2*b1 - a1*b2)
        y = (a2*c1 - a1*c2)/(b2*a1 - b1*a2)
        
        print("(", x, ",", y, ")", 'is solution for your equation') # print soulution



else: # error message
    print("You have selected wrong option.")
    print("Select a integer for your equation and run this code again")



# end of code and link to this repo
print("You can visit https://github.com/JymPatel/Python3-FirstEdition")

# more at JymPatel/Python3-FirstEdition
# raspberry-pi-detector by @bupboi1337
# new version of equations.py and much more
# even you can contribute there

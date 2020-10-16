"""#Project Euler Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

blue_discs = 3
Tot_no_discs = 4
LIMIT = 1000
while Tot_no_discs <= LIMIT:
    blue_discs,Tot_no_dicsc = 3*blue_discs + 2*Tot_no_discs - 2, 4*blue_discs + 3*Tot_no_discs - 3
print( "Total disks =", LIMIT)
print("Number of Blue disks, number of total disks =", blue_discs, Tot_no_discs)

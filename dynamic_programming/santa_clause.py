"""
Have you ever wondered how Christmas presents are delivered?
I sure have, and I believe Santa Claus has a list of houses he loops through. 
He goes to a house, drops off the presents, eats the cookies and milk, and moves on to the next house on the list. 
Since this algorithm for delivering presents is based on an explicit loop construction, it is called an iterative algorithm.
"""
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)


"""
But I feel for Santa. At his age, he shouldn’t have to deliver all the presents by himself. 
I propose an algorithm with which he can divide the work of delivering presents among his elves:



1-Appoint an elf and give all the work to him
2-Assign titles and responsibilities to the elves based on the number of houses for which they are responsible:
  > 1 He is a manager and can appoint two elves and divide his work among them
  = 1 He is a worker and has to deliver the presents to the house assigned to him


This is the typical structure of a recursive algorithm. 
If the current problem represents a simple case, solve it. 
If not, divide it into subproblems and apply the same strategy to them.

The algorithm for recursive present delivery implemented in Python:
"""

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

"""
Many people ask where we use the algorithms in real life, For them 
This is not any new algorithm , this is binary search Algorithm
which we learn and this helped use sloving a real life Dynamic Programming Solution
"""
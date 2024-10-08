'''
A list that has the common distinct element from both arrays and 
if there are repetitions of the element then only one occurrence 
is considered, known as the union of both arrays.

A list that has common distinct elements from both arrays, 
is the intersection of both arrays.


Example:
Input: a[] = {1, 2, 2, 3, 4, 8, 10}, b[] = {4, 6, 3, 1}
Output: {1, 2, 3, 4, 6, 8, 10}
Explanation: 1, 2, 3, 4, 6, 8 and 10 is the union of 
elements present in array a[] and array b[].

Input: a[] = {1, 2, 2, 3, 4, 8, 10}, b[] = {4, 6, 3, 1}
Output: {1, 2, 3, 4}
Explanation: 1, 2, 3, and 4 are the intersection(common elements) 
of elements present in array a[] and array b[].


'''

#Taking input lists from user

a=list(map(int,input('Enter elements of first list:').split()))
b=list(map(int,input('Enter elements of second list:').split()))
# Example Input
#Enter elements of first list: 3 4 6 4  4 6 7 41
#Enter elements of second list: 78 3 5 7 -1 9 2 -5



'''bitwise or (|) between the sets of both arrays
 to find union and assign it into a variable A
  in the form of lists.
  bitwise and (&) between the sets of both arrays
 to find intersection and assign it into a variable A
  in the form of lists.
'''


A=list(set(a)|set(b))
B=list(set(a)&set(b))



print('Union of the arrays:',A)
print('intersection of the arrays:',B)

#Output
'''Union of the arrays: [2, 3, 4, 5, 6, 7, 41, 9, 78, -5, -1]
intersection of the arrays: [3, 7]
'''

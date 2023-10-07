class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True
            if not swapped:
                break

# Test Case 1: Sorting a list of integers
arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort1 = BubbleSort(arr1)
bubble_sort1.sort()
print("Test Case 1:", arr1)

# Test Case 2: Sorting a list of strings
arr2 = ["apple", "banana", "grape", "date", "cherry"]
bubble_sort2 = BubbleSort(arr2)
bubble_sort2.sort()
print("Test Case 2:", arr2)

# Test Case 3: Sorting a list of custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35), Person("David", 22)]
bubble_sort3 = BubbleSort(people, key=lambda x: x.age)
bubble_sort3.sort()
print("Test Case 3:")
for person in people:
    print(person)

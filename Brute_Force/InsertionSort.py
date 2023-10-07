class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            current_element = self.arr[i]
            j = i - 1

            while j >= 0 and current_element < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = current_element

# Test Case 1: Sorting a list of integers
numbers = [64, 25, 12, 22, 11]
sorter = InsertionSort(numbers)
sorter.sort()
print("Test Case 1 - Sorted array:", numbers)

# Test Case 2: Sorting a list of strings
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
sorter = InsertionSort(fruits)
sorter.sort()
print("Test Case 2 - Sorted array:", fruits)

# Test Case 3: Sorting a list of custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35), Person("David", 28)]
sorter = InsertionSort(people, key=lambda person: person.age)  # Sort by age
sorter.sort()
print("Test Case 3 - Sorted array:")
for person in people:
    print(person)

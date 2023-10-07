class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]


# Test case 1: Sorting a list of integers in ascending order
arr1 = [64, 25, 12, 22, 11]
sorter1 = SelectionSort(arr1)
sorter1.sort()
print("Sorted array 1:", arr1)

# Test case 2: Sorting a list of strings in lexicographical order
arr2 = ["apple", "banana", "cherry", "date", "blueberry"]
sorter2 = SelectionSort(arr2)
sorter2.sort()
print("Sorted array 2:", arr2)


# Test case 3: Sorting a list of custom objects by a specific attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age} years)"


people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Carol", 35),
    Person("David", 22),
]
sorter3 = SelectionSort(people, key=lambda x: x.age)  # Sort people by age
sorter3.sort()
print("Sorted array 3:", [str(person) for person in people])

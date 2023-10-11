class Person:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
        self.someBigObject = object()

    def getSalary(self):
        return self.salary

    def __str__(self):
        return (
            "Person{"
            + "id="
            + str(self.id)
            + ", salary="
            + str(self.salary)
            + ", someBigObject="
            + str(self.someBigObject)
            + "}"
        )


def tagSort(persons, tag):
    n = len(persons)
    for i in range(n):
        for j in range(i + 1, n):
            if persons[tag[i]].getSalary() > persons[tag[j]].getSalary():
                tag[i], tag[j] = tag[j], tag[i]


if __name__ == "__main__":
    # Creating objects and their original order
    n = 5
    persons = [
        Person(0, 233.5),
        Person(1, 23),
        Person(2, 13.98),
        Person(3, 143.2),
        Person(4, 3),
    ]
    tag = [i for i in range(n)]

    # Every Person object is tagged to an element in the tag array.
    print("Given Person and Tag")
    for i in range(n):
        print(str(persons[i]) + " : Tag: " + str(tag[i]))

    # Modifying tag array so that we can access persons in sorted order.
    tagSort(persons, tag)

    print("New Tag Array after getting sorted as per Person[]")
    for i in range(n):
        print(tag[i])

    # Accessing persons in sorted (by salary) way using modified tag array.
    for i in range(n):
        print(persons[tag[i]])

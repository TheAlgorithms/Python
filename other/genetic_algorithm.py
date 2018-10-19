import random

population = 200
poolLength = 20
generations = 0
mutation = 0.01

alphabet = "abcdefghijklmnopqrstuvwxyz! "
target = "target text"
output = ""
data = []
pool = []
score_range = []

class Item:
    def __init__(self, data, target):
        self.target = target
        self.data = data
        self.score = self.get_score()

    def get_score(self):
        score = 0
        for i in range(len(self.data)):
            if self.data[i] == self.target[i]:
                score += 1
        return score / len(self.data)

    def __str__(self):
        return 'String: ' + ''.join(self.data) + ', Score: ' + str(self.score)

# SETUP
for i in range(population):
    randomString = ''
    for j in range(len(target)):
        randomString += random.choice(alphabet)      
    data.append(Item(randomString, target))

while output != target:

    pool = []

    sortedData = sorted(data, key=lambda item: item.score, reverse=True)
    pool = sortedData[0: poolLength]

    data = []
    while len(data) < population:
        parentA = pool[random.randint(0,len(pool)-1)]
        parentB = pool[random.randint(0,len(pool)-1)]

        parentAScore = parentA.score / (parentA.score + parentB.score)        

        childData = []
        for i in range(len(target)):
            probability = random.uniform(0,1)
            if probability <= parentAScore:
                childData.append(parentA.data[i])
            else:
                childData.append(parentB.data[i])

        for i in range(len(childData)):
            m = mutation * 100
            r = random.randint(0,100/m)
            if r == 0:
                childData[i] = random.choice(alphabet)

        child = Item(childData, target)
        data.append(child)
        output = "".join(child.data)
        if output == target:
            break
    best = None
    for i in range(len(data)):
        if best == None:
            best = data[i]
        elif data[i].score > best.score:
            best = data[i]
    print(best)
    generations += 1
    print("Generation: " + str(generations))

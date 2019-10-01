import math

class Ponto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return ("(%d, %d, %d)" % (self.x, self.y, self.z))


b = Ponto(2, -1, 7)
a = Ponto(1, -3, 5)
print("Ponto A: %s" % a)
print("Ponto B: %s" % b)
delta = math.sqrt(abs(((b.x - a.x)**2 + (b.y - a.y)**2 + (b.z - a.z)**2)))

print(delta)
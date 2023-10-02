class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1= ""
        index = 0
        for i in self.vec   :
            str1 += f" {i}a{index} + "
            index +=1
        return str1[:-1]

v1= Vector([1, 4, 6 , 45, 88, 854])
print(v1)
class things:
    def __init__(self, n, v, w):
        self.name=n
        self.value=v
        self.weight=w

    def get_value(self):
        return self.value
    
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def value_Weight(self):
        return self.value/self.weight


def build_menu(name,value,weight):
    menu=[]
    for i in range(len(value)):
        menu.append(things(name[i],value[i],weight[i]))
    return  menu
def greedy(item,maxCost,keyFunc):
    itemsCopy=sorted(item,key=keyFunc,reverse=True)
    result=[]
    totalValue,total_cost=0.0,0.0
    for i in range(len(itemsCopy)):
        if (total_cost+itemsCopy[i].get_weight()) <= maxCost:
            result.append(itemsCopy[i])
            total_cost+=itemsCopy[i].get_weight()
            totalValue+=itemsCopy[i].get_value()
    return (result,totalValue)


def testgreedy(max):
    result,totalValue=greedy(foods,max,things.get_value)
    for i in range(len(result)):
        print(result[i].get_name(),result[i].get_value())
food=['Burger','Pizza','Coca Cola','Rice','Sambhar','Chicken','Fries','Milk']
value=[80,100,60,70,50,110,90,60]
weight=[40,60,40,70,100,85,55,70]
foods=build_menu(food,value,weight)
testgreedy(500)

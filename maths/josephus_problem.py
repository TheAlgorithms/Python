'''
For more information about this prtoblem-
https://en.wikipedia.org/wiki/Josephus_problem#:~:text=In%20computer%20science%20and%20mathematics,a%20certain%20counting%2Dout%20game
https://www.geogebra.org/m/ExvvrBbR
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
class CircularLinkedList:
    def __init__(self, head = None):
        self.head = head
   
    def append(self, new_value):
        new_node = Node(new_value)
        
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            return
        else:
            new_node.next = self.head
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.next = new_node
                    
    def remove_node(self, node_to_remove):
        if self.head == node_to_remove and self.head.get_next() == self.head:
            self.head.next = None
            self.head = None
            return
        elif self.head == node_to_remove:
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.next = self.head.get_next()
            self.head = self.head.get_next()
            return
        else:
            current_node = self.head
            while current_node.get_next() != node_to_remove:
                current_node = current_node.get_next()
            current_node.next = current_node.get_next().get_next()
            return
           
    def length(self):
        if not self.head:
            return 0
        else:
            count = 0
            current_node = self.head
            while current_node.get_next() != self.head:
                count += 1
                current_node = current_node.get_next()
            return count + 1

    def get_survivor(self):
        return self.head.get_value()   
         
    def josephus(self, step):
        current_node = self.head
        while self.length() > 1:
            count = 1
            while count != step:
                current_node = current_node.get_next()
                count += 1
            print("KILLED", current_node.get_value())
            self.remove_node(current_node)
            current_node = current_node.get_next()
            
            

def main():
    n = int(input("Enter the number of people:\n"))
    step = int(input("Enter the number of people to be skipped each time:\n"))
    
    c = CircularLinkedList()
    for i in range(1, n + 1):
        c.append(i)
        
    c.josephus(step)
    print("The final survivor is:", c.get_survivor())
    
    
main()

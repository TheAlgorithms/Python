# -*- coding: utf-8 -*-
'''
An auto-balanced binary tree!
'''
import math
class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
    def isEmpty(self):
        return self.head == self.tail
    def push(self,data):
        self.data.append(data)
        self.tail = self.tail + 1
    def pop(self):
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret
    def count(self):
        return self.tail - self.head
    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])
        
class my_node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getheight(self):
        return self.height
    def setdata(self,data):
        self.data = data
        return
    def setleft(self,node):
        self.left = node
        return
    def setright(self,node):
        self.right = node
        return
    def setheight(self,height):
        self.height = height
        return

def getheight(node):
#    print("xxx")
    if node is None:
        return 0
    return node.getheight()

def my_max(a,b):
    if a > b:
        return a
    return b



def leftrotation(node):
    ret = node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rightrotation(node):
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def lrrotation(node):
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)

def rlrotation(node):
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)

def insert_node(node,data):
    if node is None:
        return my_node(data)
    if data < node.getdata():
        node.setleft(insert_node(node.getleft(),data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2:
            if data < node.getleft().getdata():
                node = leftrotation(node)
            else:
                node = rlrotation(node)
    else:
        node.setright(insert_node(node.getright(),data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    return node

class AVLtree:
    def __init__(self):
        self.root = None
    def getheight(self):
#        print("yyy")
        return getheight(self.root)
    def insert(self,data):
        self.root = insert_node(self.root,data)
    def traversale(self):
        q = my_queue()
        q.push(self.root)
        layer = self.getheight()
        cnt = 0
        while not q.isEmpty():
            node = q.pop()
            space = " "*int(math.pow(2,layer) - 1)
            print(space,end = " ")
            if node is None:
                print("*",end = " ")
            else:
                print(node.getdata(),end = " ")
                q.push(node.getleft())
                q.push(node.getright())
            print(space,end = " ")
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2,i) - 1:
                    layer = layer -1 
                    print()
                    break
        print()
        print("*************************************")
        return
    
    def test(self):
        getheight(None)
        print("****")
        self.getheight()
if __name__ == "__main__":
#    t = AVLtree()
#    t.test()
#    q = my_queue()
##    q.push(1)
##    q.push(2)
#    for i in range(10):
#        q.push(i)
#    q.print()
#    q.push(90)
#    q.print()
#    
#    q.pop()
#    q.print()
    t = AVLtree()
    t.traversale()
#    t.insert(7)
#    t.traversale()
    
    t.insert(8)
    t.traversale()
    t.insert(3)
    t.traversale()
    t.insert(6)
    t.traversale()
    t.insert(1)
    t.traversale()
    t.insert(10)
    t.traversale()
    t.insert(14)
    t.traversale()
    t.insert(13)
    t.traversale()
#    t.traversale()
    t.insert(4)
    t.traversale()
    t.insert(7)
    t.traversale()
    
        






























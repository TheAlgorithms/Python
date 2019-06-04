from __future__ import print_function

class Node: #create a node
  def __init__(self,data):
    self.data = data   #giving data
    self.next = None   #giving next to None

class Circular_Linked_List:
  def __init__(self):
    self.last = None    #Initializing last to None
  
  def insert_beginning(self,data):
    newNode = Node(data)   #create node
    if self.last == None:   #If last is None, Make newNode last
      self.last = newNode
      self.last.next = self.last
    else:
      newNode.next = self.last.next   #set newnode's next as head
      self.last.next = newNode
      

  def insert_end(self,data):
    newNode = Node(data) 
    if self.last == None:
      self.last = newNode
      self.last.next = self.last
    else:
      newNode.next = self.last.next #set newnode's next as head
      self.last.next = newNode    
      self.last = newNode #set newnode as last node

  def delete_beginning(self):
    node = self.last.next
    self.last.next = node.next  #set last's next to first node's next
    return node.data
  
  def delete_end(self):
    temp = self.last.next
    while temp.next is not self.last:   #Traversing the list
      temp=temp.next
    node = self.last
    temp.next = self.last.next   #set second last node's next to last's next
    self.last = temp
    return node.data
  
  def print_list(self):
    print("The list is:")
    temp = self.last.next   #Creating iterator
    while temp is not self.last:    #Traversing the list
      print(temp.data)
      temp = temp.next
    print(temp.data)    #print last node

def main():
  LL = Circular_Linked_List()
  print("Inserting at beginning: ")
  a1 = input()
  LL.insert_beginning(a1)
  print("Inserting at beginning: ")
  a2 = input()
  LL.insert_beginning(a2)
  LL.print_list()
  print("Inserting at the end: ")
  a1 = input()
  LL.insert_end(a1)
  print("Inserting at the end: ")
  a2 = input()
  LL.insert_end(a2)
  LL.print_list()
  print("Deleting from beginning")
  print(LL.delete_beginning()," deleted")
  LL.print_list()
  print("Deleting from end")
  print(LL.delete_end()," deleted")
  LL.print_list()

if __name__ == '__main__':
	main()

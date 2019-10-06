###### Driver program to test the queue ###
from listQueueModule import listQueue
que = listQueue()
def menu():
    print()
    print("1. Add an item to queue")
    print("2. Remove an item from queue")
    print("3. Display the queue")
    print("4. Length of queue")
    print("5. Exit from program")
    choice = int(input("Enter your choice(1-5) :"))
    return choice
while True:
    c = menu()
    if c == 1:
        item = int(input("Enter an item :"))
        que.enqueue(item)
    elif c == 2:
        item = 0
        underflow = False
        item, underflow = que.dequeue(item, underflow)
        if underflow:
            print("Queue is empty")
        else:
            print("Dequeue :", item)
    elif c == 3:
        que.printQueue()
    elif c == 4:
        print("Length of queue is ", que.length())
    else:
        break

    

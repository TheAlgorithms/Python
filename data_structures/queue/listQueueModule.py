class listQueue:
    def __init__(self):
        self.qList = list = []
    #----------------------
    def isEmpty(self):
        return len(self.qList) == 0
    #------------------------
    def length(self):
        return len(self.qList)
    #------------------------
    def enqueue(self, item):
        self.qList.append(item)
    #-------------------------
    def dequeue(self,item, underflow):
        if self.isEmpty() is True:
            underflow = True
        else:
            underflow = False
            item =self.qList.pop(0) 
        return item , underflow
    def printQueue(self):
        print("Queue is: ")
        for item in self.qList:
            print(item, end = "  ")
    #---------------------------------
















        
                 

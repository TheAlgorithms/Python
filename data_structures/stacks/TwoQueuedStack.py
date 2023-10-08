class StackUsingQueues:
    def __init__(self):
        """
        Initialising required queues using lists data structure
        """
        self.queue1 = []
        self.queue2 = []

    def push(self,item):
        while len(self.queue1)!= 0:
            """
            enqueuing queue 2 using the values from queue 1 bringing them out in First
            In First Out (F.I.F.O) order.
            """
            self.queue2.append(self.queue1[0])
            self.queue1 .pop(0)
            """
            adding the new value to queue 1
            """
        self.queue1.append(item)

        """
        returning the values from queue 2 to queue 1 so as
        to replicate the stack data structure
        """
        while len(self.queue2)!= 0:
            self.queue1.append(self.queue2[0])
            self.queue2.pop(0)




    def pop(self):
        if len(self.queue1) != 0:
            """
            The first value of queue 1 is being popped here as it
            has been implemented in a way that the
            first value of the queue which gets popped is the last value of the stack.
            And since stack follows Last In First Out (L.I.F.O) order the
            following has been implemented.
            """
            popped = self.queue1[0]
            self.queue1.pop(0)
            return popped
        else:
            return None







    def peek(self):
        """
        Function to see the last value inserted in the stack
        implemented using queue here, which has the last
        value of the stack as its first.
        """
        if len(self.queue1) != 0:
            return self.queue1[0]
        else:
            return None



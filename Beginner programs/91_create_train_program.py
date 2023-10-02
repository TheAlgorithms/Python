class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print("**************")
        print(f"The name of the train is {self.name}")
        print(f"The seats avilable in the train are {self.seats}")
        print("**************")

    def fareInfo(self):
        print(f"the price of the ticket is : Rs {self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked and your seat no is {self.seats}")
            self.seats=self.seats-1 
        else:
            print("Sorry this train is full kindly try in tatkal")

    def cancelTicket(self,seatNo):
        pass


intercity=Train("Intercity Express: 14015",90,2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookticket()
intercity.bookticket()
intercity.getStatus()
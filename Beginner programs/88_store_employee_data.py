class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"the name of the {self.company} programer is {self.name} and the product is {self.product}")


Yash = Programmer("Yash", "Skype")
Alka = Programmer("Alka", "Github")
Yash.getInfo()
Alka.getInfo()
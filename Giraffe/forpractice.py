#Lottery game
import random
import time
import matplotlib.pyplot as plt
x = []
y = []
plt.xlabel("Month")
plt.ylabel("Account Balance")
plt.title("Account vs Month graph")
account = 1000
print("Initial balance is :",account)
print("Entry fee is 100 and prize is 500")
bet_number = random.randint(0,11)
months = int(input("Enter the number of months you want to play: "))
for month in range(1,months+1):
	prize_number = random.randint(0, 11)
	x.append(month)
	y.append(account)
	if bet_number == prize_number:
		account = account + 500 - 100
	else:
		account = account - 100
print("The balance left is :",account)
plt.plot(x,y)
plt.show()



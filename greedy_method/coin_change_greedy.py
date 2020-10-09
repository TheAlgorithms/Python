def coin_change_greedy(n,coins):
  i = 0
  coins = sorted(coins,reverse=True)
  if(n<0):
    print("Not Possible")
  elif n==0:
    print("0 Coins")
  while(n>0):
    if(coins[i] > n):
      i = i+1
    else:
      print(coins[i],end=' ')
      n = n-coins[i];
  print("\n\n\n\n")

if __name__ == '__main__':
  target = int(input("Enter Target: "))
  coins = results = list(map(int, input("Enter Available Coins: ").split()))
  coin_change_greedy(target,coins)

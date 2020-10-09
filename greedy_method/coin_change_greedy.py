def coin_change_greedy(n,coins):
  """returns minimum coin needed for change with greedy"""
  '''
  >>Enter Target: 10
  Enter Available Coins: 1 5 3 7
  7 3 
  >>Enter Target: 44
  Enter Available Coins: 1 10 20 2
  20 20 2 2
      '''
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

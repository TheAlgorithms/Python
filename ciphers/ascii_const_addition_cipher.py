choice = input("Choose an option: (1) - Encrypt a message (2) - Decrypt a message: ")
i = 0
x = 0
string_1 = ""
string_2 = ""

if choice == "1":
  user_input1 = input("Enter the  message here: ")
  user_constant = input("Enter the constant number here: ")
  for z in user_input1:
     asciicode = ord(user_input1[i])
     i += 1
     asciicode += int(user_constant)
     string_1 += str(asciicode)
     string_1 += " "
     if i == len(user_input1):
       print(string_1)
elif choice == "2":
  user_input2 = input("Enter the message here: ")
  user_constant2 = input("Enter the constant number: ")
  while True:
    split = user_input2.split()
    english = int(split[x])
    english += - int(user_constant2)
    english = chr(english)
    x += 1
    string_2 += str(english)
    if x == len(split):
      print(string_2)
      break
else:
  print("You were supposed to type 1 or 2, not %s!" % choice)
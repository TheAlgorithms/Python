#This cipher is really simple. It adds and subtracts a constant added to the ascii values of the letters in the messages.
#To decrypt, the user must have both the message and the constant, otherwise it becomes a trial-and-error of guessing different values.

choice = input("Choose an option: (1) - Encrypt a message (2) - Decrypt a message: ")
choice1_location = 0
choice2_location = 0
choice_1_string = ""
choice_2_string = ""

if choice == "1":
  user_input1 = input("Enter the  message here: ")
  user_constant = input("Enter the constant number here: ")

  for z in user_input1:
     asciicode = ord(user_input1[choice1_location])
     choice1_location += 1
     asciicode += int(user_constant)
     choice_1_string += str(asciicode)
     choice_1_string += " "
     if choice1_location == len(user_input1):
       print(choice_1_string)
elif choice == "2":
  user_input2 = input("Enter the message here: ")
  user_constant2 = input("Enter the constant number: ")
  while True:
    split = user_input2.split()
    english = int(split[choice2_location])
    english += - int(user_constant2)
    english = chr(english)
    choice2_location += 1
    choice_2_string += str(english)
    if choice2_location == len(split):
      print(choice_2_string)
      break
else:
  print("You were supposed to type 1 or 2, not {}!".format(choice))
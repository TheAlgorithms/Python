# originalString = str(input("Type in any string: "))
# You can use the input but for testing I used a predefined string

originalString = "Test"


def stringToAscii(string):
  NumberDec = []
  NumberBin = []
  NumberHex = []
  NumberOct = []

  for i in string:
    NumberBin.append(bin(ord(i)))
    NumberHex.append(hex(ord(i)))
    NumberOct.append(oct(ord(i)))
    NumberDec.append(ord(i))
  message = ""
  message += "Decimal numbers: "
  for i in NumberDec:
      message += str(i) + ", "
  message += "\n"
  message += "Hex numbers: "
  for i in NumberHex:
      message += str(i)[2:] + ", "
  message += "\n"
  message += "Octal numbers: "
  for i in NumberOct:
      message += str(i)[2:] + ", "
  message += "\n"
  message += "Binary numbers: "
  for i in NumberBin:
      message += str(i)[2:] + ", "

  return message;

print(stringToAscii(originalString))
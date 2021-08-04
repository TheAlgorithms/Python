def cypher_mesage(txt):
  alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', "X", 'Y', 'Z']

  info = []
  for char in txt:
    if (char.isalpha() == False):
      info.append(2)
    elif char.isupper() == True:
      info.append(1)
    else:
      info.append(0)

  indx_lst=[]
  for char in txt:
    if (char.isalpha() == False):
      indx_lst+=char
    else:
      if char.isupper() == True:
        indx_lst.append(alphabet_upper.index(char))
      else:
        indx_lst.append(alphabet_lower.index(char))

  res_indx=[]
  for char in indx_lst:
    if type(char) == int:
      if int(char) <= 2:
        res_indx.append(26 + (int(char) - 3))
      else:
        res_indx.append(int(char) - 3)
    else:
      res_indx+=char
      

  res_str = ""
  count = 0
  for char in res_indx:
    if type(char) != int:
      res_str += char
    else:
      if info[count] == 0:
        res_str += str(alphabet_lower[int(char)])
      elif info[count] == 1:
        res_str += str(alphabet_upper[int(char)])
    count+=1

  print(res_str)



code_mesage("xXyzabB!1234")
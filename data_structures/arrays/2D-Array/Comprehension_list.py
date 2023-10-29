# to print square of given list.
# li = [1, 2, 3, 4]
# li_new = []
# for ele in li:
#     li_new.append(ele**2)
# print(li_new)
# or
li = [1, 2, 3, 4, 5]
li_new = [ele ** 2 for ele in li]
print(li)

# to print only even integer square values
li = [1, 2, 3, 4, 5]
li_new2 = [ele ** 2 for ele in li if ele % 2 == 0]
print(li_new2)
# to print numer divisible by 2&3 square values
li = [1, 2, 3, 4, 5, 6]
li_new3 = [ele ** 2 for ele in li if ele % 2 == 0 and ele % 3 == 0]
print(li_new3)
# to print intersection of 2 list.
li_1 = [1, 2, 3, 4, 5]
li_2 = [2, 4, 6, 7]
li_ele = [ele for ele in li_1 for ele_2 in li_2 if ele == ele_2]
print(li_ele)
# print ele squares if divisible by 2 ele print ele only.
li = [1, 2, 3, 4, 5]
li_inter = [ele ** 2 if ele % 2 == 0 else ele for ele in li]
print(li_inter)
# to print separate :
s = "Garvit"
li = [ele for ele in s]
print(li)
li = "Garvit", "Anshuman", "Shalvin"
li_s = [{a for a in ele} for ele in li]
print(li_s)

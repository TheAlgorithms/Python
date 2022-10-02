at = open('atempts.txt')
atemptsls = at.readlines()
at.close()



def sets(atemptsls1):
	""""
	returns the set of all the digits in atrmptsls1

	we can use this to find all the digits used in the password.
	we know it will probably be {'0', '1','2','3','4','5','6','7','8','9','\\n'}
	but trying doesn't costs a supercomputer

	"""
	abcs = []
	for atempt in atemptsls1:
		for digit in atempt:
			abcs.append(digit)
	return set(abcs)

# applying sets(atemptsls)
# we get:
# {'8', '7', '\n', '9', '6', '1', '0', '2', '3'}

# aranging we get:
# {0, 1, 2, 3, 6, 7, 8, 9}
# 

# so we got 8 digits
# NOW, How do we get the password


# the ans is to check what comes after what

#here is the code to do that

a = '9'
after = []
before = []
for atempt in atemptsls:
	if a in atempt:
		if atempt[0] == a:
			after.append(atempt[1])
			after.append(atempt[2])
		elif atempt[1] == a:
			after.append(atempt[2])
			before.append(atempt[0])
		else:
			before.append(atempt[0])
			before.append(atempt[1])
print(set(before),set(after), sep='\n')



# 0
# before: {'7', '8', '6', '2', '1', '3', '9'}
# after: {}

# 1
# before: {'3', '7'}
# after: {'0', '8', '9', '2', '6'}

# 2
# before: {'1', '6', '7', '3'}
# after: {'9', '8', '0'}

# 3
# before: {'7'}
# after: {'2', '6', '8', '9', '0', '1'}

# 6
# before: {'1', '7', '3'}
# after: {'9', '2', '8', '0'}

# 7
# before: {}
# after: {'3', '9', '6', '1', '2', '8', '0'}

# 8
# before: {'6', '7', '1', '2', '3'}
# after: {'0', '9'}

# 9
# before: {'3', '1', '2', '8', '6', '7'}
# after: {'0'}

# NOW, by analysing 
# 7 is the first
# since nothing is after this
# 3 is after
# since 7 is the only number before 3
# and we get the ans just by this

# # 73162890
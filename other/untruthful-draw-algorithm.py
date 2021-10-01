
			#------Untruthful Draw Algorithm Implimentation--#
			#-----Created By: Group2 -------#
			import random

# Using a ascending order list and shuffle it to create a list of random 
#numbers, will be used as draw number and also to generate preference list
def randomNumbers(Numbers, size):
	Num=Numbers
	random.shuffle(Num)
	return Num

# Used to sort the list with draw numbers in ascending order of draw numbers
def sortDrawList(choiceWithDrawNumber): 
	choiceWithDrawNumber.sort(key=lambda num:num[1])

#Helps to generate preference list and write it in the file     
def generateStudentChoice(n):
	subList=[]
	for i in range(0,n):
		tempList=[i+1 for i in range(n)]
		randomNum=randomNumbers(tempList,n)
		subList.append(randomNum)
		choiceList=[]
	# Generating random choice list
	for i in range(n):
		string=""
		for j in range(n):
			if j==0:
				string += str(subList[i][j])
			else:
				string += " "+str(subList[i][j])
				choiceList.append(string)
				print("Student Choice List:")
				for i in range(n):
					print(choiceList[i])
					print(" ")

	# Writing on file
	f=open('input.txt','w')
	for i in range(n):
		f.writelines(str(choiceList[i]))
		f.write("\n")

# def untruthfulDraw(untruthfulNum, studentChoice, 
#   currentPreferenceListNum, alloted, finalAllotmentList,n, j):
#   if j <= untruthfulNum:
#       picked=studentChoice[currentPreferenceListNum][j]
#       if alloted[picked]==0:
#           finalAllotmentList[currentPreferenceListNum]=picked
#           alloted[picked]=1
#           break
#   elif j > untruthfulNum:
#       tempList=studentChoice[currentPreferenceListNum]
#       equalPriorityList=tempList[int(n/2):]
#                       #print(" For prefernce list num ",currentPreferenceListNum)
#       print(equalPriorityList)
#       newPicked= random.choice(equalPriorityList)
#       print("new picked", newPicked)
#       if alloted[newPicked]==0 :
#           print("Finall Picked", newPicked)
#           finalAllotmentList[currentPreferenceListNum]= newPicked
#           alloted[newPicked]=1
#           break
#           #break
#       else:
#           while(alloted[newPicked])==1:
#               #print("loop")
#               newPicked= random.choice(equalPriorityList)
#               if alloted[newPicked]==0:
#                   #print("Finally")
#                   finalAllotmentList[currentPreferenceListNum]=newPicked
#                   break
#           alloted[newPicked]=1
#           break
#                               #print('here')
# Draw Algorithm Main part
def drawAlgoithm(studentChoice, finalAllotmentList,n):
	#Generating n preference list
	generateStudentChoice(n)
	# Storing all preference list in inputChoice list
	inputChoices=[]
	
	inputFromFile=open('input.txt','r')
	stringLine=inputFromFile.read()
	inputChoices.append(stringLine.splitlines())
	
	for i in range(0,n):
		tempVariable=[int(num) for num in inputChoices[0][i].split()]
		studentChoice.append(tempVariable)
	# DrawNumbers will store all random draw numbers    
	drawNumbers=[i+1 for i in range(n)]
	drawNumbers=randomNumbers(drawNumbers,n)
	print("Draw Numbers are:",drawNumbers)
	#ChoiceWithDrawNumber keeps track of which preference list got which draw number
	choiceWithDrawNumber=[]
	for i in range(0,n):
		pair=(i,drawNumbers[i])
		choiceWithDrawNumber.append(pair)
	#print("Chice With Draw Num",choiceWithDrawNumber)  
	sortDrawList(choiceWithDrawNumber)
	# alloted will keep count which prefereces are already alloted
	alloted=[0]*(n+1)
	# First n/2 preferences will be taken in priority order,while rest 
	# of n/2 preferences have same priority
	untruthfulNum=n/2
	picked=0
	for i in range(0,n):
		currentPreferenceListNum=choiceWithDrawNumber[i][0]
		#print("Current list",currentPreferenceListNum)
		for j in range(0,n):
			# untruthfulDraw(untruthfulNum,studentChoice,
			#   currentPreferenceListNum, alloted,finalAllotmentList,n, j)
			if j <= untruthfulNum:
				picked=studentChoice[currentPreferenceListNum][j]
				if alloted[picked]==0:
					finalAllotmentList[currentPreferenceListNum]=picked
					alloted[picked]=1
					break
				elif j > untruthfulNum:
					tempList=studentChoice[currentPreferenceListNum]
					equalPriorityList=tempList[int(n/2):]
								#print(" For prefernce list num ",currentPreferenceListNum)
								#print(equalPriorityList)
					newPicked= random.choice(equalPriorityList)
								#print("new picked", newPicked)
					if alloted[newPicked]==0 :
										#print("Finall Picked", newPicked)
						finalAllotmentList[currentPreferenceListNum]= newPicked
						alloted[newPicked]=1
						break
					else:
						while( alloted[newPicked])==1:
												#print("loop")
							newPicked= random.choice(equalPriorityList)
							if alloted[newPicked]==0:
														#print("Finally")
								finalAllotmentList[currentPreferenceListNum]=newPicked
								break
						alloted[newPicked]=1
										#print('here')
						break


			print("Alloted Rooms to the student are:", finalAllotmentList)

def main():
	print("Implimentation of a Draw Algorithm for allotment of hostel room")
	studentChoice=[]
	n=int(input("Enter the number of student to allot rooms:"))
	finalAllotmentList=[0]*n            #Final alloted list
	
	drawAlgoithm(studentChoice,finalAllotmentList,n);
	print("------End-----")

if __name__=="__main__":
	main()




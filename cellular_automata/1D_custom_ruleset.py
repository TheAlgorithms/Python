from PIL import Image


#Creates the outputing image
RESULT = Image.new('RGB', (31, 16))
PIXELS = RESULT.load()

#Formats inputted ruleset
RULE_NUM = bin(int(input('Rule\n')))[2:]
RULE = [int(a) for a in RULE_NUM]
while True:
    if len(RULE) == 8:
        break
    else:
        RULE.insert(0,0)

#Defines the first generation of cells
CELLS = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#Mainloop
for time in range(16):

    NEW_ROW = []

    for i in range(31):
        #Gets neighbors of a cell

        #If leftmost cell is in consideration
        if i == 0:
            left_neighbor = 0
            right_neighbor = CELLS[time][i+1]

        #If rightmost cell is in consideration
        elif i == 30:
            left_neighbor = CELLS[time][i-1]
            right_neighbor = 0
        
        #All other cells
        else:
            left_neighbor = CELLS[time][i-1]
            right_neighbor = CELLS[time][i+1]

        #Defines new cell in and adds it to the new generation
        SITUATION = 7 - int(str(left_neighbor)+str(CELLS[time][i])+str(right_neighbor),2)
        NEW_ROW.append(RULE[SITUATION])

    #Adds new generation
    CELLS.append(NEW_ROW)

#Generates image
for w in range(31):
    for h in range(16):
        color = 255-255*CELLS[h][w]
        PIXELS[w,h] = (color,color,color)

#Uncomment for saving the image
#RESULT.save('RULE '+str(RULE_NUM))

#Shows the image
RESULT.show()

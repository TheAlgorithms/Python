import math

def BoxCipher():
    message = input("Enter Message to be encrypted: ").strip()
    message = message.replace(" ", "")
    l = len(message)
    sl = math.sqrt(l)
    r = math.floor(sl)
    c = int(sl)
    decry=[]
    fin=''
    decry=message.split(' ')
    for i in range(0,len(decry)):
    	fin=fin+str(decry[i])
    	i=i+1
    dole=list(fin)
    box_rows=[dole[i:i+r] for i in range(0, len(dole), r)]
    print("")
    for _ in range(0,len(box_rows)):
    	print(box_rows[_])
    for i in range(0, c):
    	print(message[i : l : r], end = " ")

def BoxCipherDecryption():
	message=input("Please enter message to be Decrypted:")
	message=message.split(" ")
	tex=''
	for i in range(len(message)):
		tex+=message[i]
	l=len(tex)
	sl=math.sqrt(l)
	r=math.floor(sl)
	c=int(sl)
	fin=list(tex)
	boxr=[fin[i:i+c] for i in range(0,len(fin),c)]
	#for i in range(0, c):
	#	print(tex[i : l : c+1], end = " ")
	jj=''
	x=0
	for i in range(c):
		for j in range(l%r):
			jj+=tex[x]
			x+=c+1
		for j in range(r-l%r):
			jj+=tex[x]
			x+=c
		x=i+1
	last=''
	for i in range(l%r):
		last+=message[i][-1]
	print("The encrypted message is:\n"+str(jj+last))

if(__name__=="__main"):
    inp=input("Please choose an option:\n1)Encrypt\n2)Decrypt\n-$~")
    if(inp=="1"):
        BoxCipher()
    elif(inp=="2"):
        BoxCipherDecryption()
    else:
        print("This is not a valid option.\nExiting")
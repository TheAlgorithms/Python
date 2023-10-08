import os
LC=0  #location counter initialization
"""
mnemonic dictionary elements are:
Key is mnemonic e.g. "STOP"
Value of that key is a tuple consiting of opcode value, instruction class or type and number of operands required for that mnemonic
e.g. "STOP":('00','IS',0)
This states that 'STOP' is a mnemonic whereas value tuple consisting of '00' is opcode, 'IS' is instruction type, 0 is number of operands that mnemonics required. 
"""
mnemonics={'STOP':('00','IS',0),'ADD':('01','IS',2),'SUB':('02','IS',2),'MUL':('03','IS',2),'MOVER':('04','IS',2),'MOVEM':('05','IS',2),'COMP':('06','IS',2),'BC':('07','IS',2),'DIV':('08','IS',2),'READ':('09','IS',1),'PRINT':('10','IS',1),'LTORG':('05','AD',0),'ORIGIN':('03','AD',1),'START':('01','AD',1),'EQU':('04','AD',2),'DS':('01','DL',1),'DC':('02','DL',1),'END':('AD',0)}
file=open("input.txt")  #Enter input file with complete path if not in same directory

ifp=open("inter_code.txt","a")  #output file having intermediate code
ifp.truncate(0)                 #cleaning file to remove previous data
REG={'AREG':1,'BREG':2,'CREG':3,'DREG':4}  #Registers
lit=open("literals.txt","a+")    #literals and their address containing file
lit.truncate(0)
tmp=open("tmp.txt","a+")
tmp.truncate(0)
symtab={}   #Sybol Table
pooltab=[]	#Pool Table
words=[]

#prints literal table
def littab():
    print("literal table:")
    lit.seek(0,0)
    for x in lit:
        print(x)

#prints pool table
def pooltab2():
    global pooltab
    print("Pool Table:")
    print(pooltab)

#prints symbol table
def symbol():
    global symtab
    print("Symbol Table:")
    print(symtab)

#handles END directive        
def END():
    global LC
    pool=0
    z=0
    ifp.write("\t(AD,02)\n")
    lit.seek(0,0)
    for x in lit:
        if "**" in x:
            pool+=1
            if pool==1:
                pooltab.append(z)
            y=x.split()
            tmp.write(y[0]+"\t"+str(LC)+"\n")
            LC+=1
        else:
            tmp.write(x)
        z+=1
    lit.truncate(0)
    tmp.seek(0,0)
    for x in tmp:
        lit.write(x)
    tmp.truncate(0)
   
        
#handles LTORG mnemonic
def LTORG():
    global LC
    pool=0
    z=0
    lit.seek(0,0)
    x=lit.readlines()
    i=0
    while(i<len(x)):
        f=[]
        if("**" in x[i]):
            j=0
            pool+=1
            if pool==1:
                pooltab.append(z)
            while(x[i][j]!="'"):
                j+=1
            j+=1
            while(x[i][j]!="'"):
                f.append(x[i][j])
                j+=1
            if(i!=len(x)-1):
                ifp.write("\t(AD,05)\t(DL,02)(C,"+str(f[0])+")\n")
                y=x[i].split()
                tmp.write(y[0]+"\t"+str(LC)+"\n")
                LC+=1
                ifp.write(str(LC))
            else:
                ifp.write("\t(AD,05)\t(DL,02)(C,"+str(f[0])+")\n")
                y=x[i].split()
                tmp.write(y[0]+"\t"+str(LC)+"\n")
                LC+=1
        else:
            tmp.write(x[i])
        z+=1
        i+=1
    lit.truncate(0)
    tmp.seek(0,0)
    for x in tmp:
        lit.write(x)
    tmp.truncate(0)
          

#handles ORIGIN mnemonic
def ORIGIN(addr):
    global LC
    ifp.write("\t(AD,03)\t(C,"+str(addr)+")\n")
    LC =int(addr)

#handles DS mnemonic
def DS(size):
    global LC
    ifp.write("\t(DL,01)\t(C,"+size+")\n")
    LC=LC+int(size)

#handles DC mnemonic
def DC(value):
    global LC
    ifp.write("\t(DL,02)\t(C,"+value+")\n")
    LC+=1

'''
def EQU(words):
    global symindex
    if words[2] in symtab.keys():
        z=symtab[words[2]]
        if words[0] not in symtab.keys():
            symtab[words[0]]=(z[0],symindex)
            symindex+=1
        
        else:
            w=symtab[words[0]]
            symtab[words[0]]=(z[0],w[-1])
    
    #else:#error words[2] not defined 
    '''
 #identifies type of operands i.e. registers, literals, symbols and add approprite data in intermediate code file, literal table and symbol table as well as pool table.   
def OTHERS(mnemonic,k):
    global words
    global mnemonics 
    global symtab
    global LC,symindex
    z=mnemonics[mnemonic]
    ifp.write("\t("+z[1]+","+z[0]+")\t")
    i=0
    y=z[-1]
    #print("y="+str(y))
    for i in range(1,y+1):
        words[k+i]=words[k+i].replace(",","")
        if(words[k+i] in REG.keys()):
            ifp.write("(RG,"+str(REG[words[k+i]])+")")
        elif("=" in words[k+i]):
            #print(words[k+i])
            lit.seek(0,2)
            lit.write(words[k+i]+"\t**\n")
            lit.seek(0,0)
            x=lit.readlines()
            #print(len(x))
            ifp.write("(L,"+str(len(x))+")")
        else:
            #print(words,symtab)
            if(words[k+i] not in symtab.keys()):
                symtab[words[k+i]]=("**",symindex)
                ifp.write("(S,"+str(symindex)+")")
                symindex+=1
            else:
                w=symtab[words[k+i]]
                ifp.write("(S,"+str(w[-1])+")")
    #print(symtab)
    ifp.write("\n")
    LC+=1
 
 #idenifies mnemonic and redirect to resepective function    
def detect_mn(k):
    global words,LC
    if(words[k]=="START"):
        LC=int(words[1])
        ifp.write("\t(AD,01)\t(C,"+str(LC)+')\n')
    elif(words[k]=='END'):
        END()
    elif(words[k]=="LTORG"):
       LTORG()
    elif(words[k]=="ORIGIN"):
       ORIGIN(words[k+1])
    elif(words[k]=="DS"):
        DS(words[k+1])
    elif(words[k]=="DC"):
        DC(words[k+1])
    #elif(words[k]=="EQU"):
        #EQU(words)
    else:
        OTHERS(words[k],k)
    littab()
    pooltab2()
    symbol()

#actual code execution starts from here
symindex=0
for line in file:
    #print(line)
    words=line.split()
    #print(words)
    if(LC>0):
        ifp.write(str(LC))
    print("LC=",LC)
    print(line)
    print(words)
    k=0
        
    if words[0] in mnemonics.keys():
        print("Mnemonic:",words[0])
        val=mnemonics[words[0]]
        k=0
        detect_mn(k)
    else:
        print("Label:",words[0],"Mnemonic:",words[1])
        if words[k] not in symtab.keys():
            symtab[words[k]]=(LC,symindex)
            #ifp.write("\t(S,"+str(symindex)+")\t")
            symindex+=1
            symbol()
        else:
            #print(words)
            x=symtab[words[k]]
            if x[0]=="**":
                print("yes")
                symtab[words[k]]=(LC,x[1])
            #ifp.write("\t(S,"+str(symindex)+")\t")
            symbol()
        k=1
        detect_mn(k)
#print(symtab)
#print(pooltab)
ifp.close()
lit.close()
tmp.close()
sym=open("SymTab.txt","a+")
sym.truncate(0)
for x in symtab:
    sym.write(x+"\t"+str(symtab[x][0])+"\n")
sym.close()
pool=open("PoolTab.txt","a+")
pool.truncate(0)
for x in pooltab:
    pool.write(str(x)+"\n")
pool.close()
if os.path.exists("tmp.txt")==True:
    os.remove("tmp.txt")

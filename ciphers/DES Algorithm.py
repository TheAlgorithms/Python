class DesAlgo:
    initial_permutation=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
    inverse_permutaion=[40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    exp_table=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
    pc1_table=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    shifts=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    bit_shuffle=[16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    pc2_table=[14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    keys=list()
    shifted_keys=list()
    s_boxes=[[ 
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], 
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8], 
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0], 
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13] 
    ], 
    [ 
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10], 
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], 
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15], 
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9] 
    ], 
    [ 
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8], 
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1], 
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7], 
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12] 
    ], 
    [ 
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15], 
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9], 
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4], 
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14] 
    ], 
    [ 
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9], 
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6], 
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14], 
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3] 
    ], 
    [ 
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11], 
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8], 
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], 
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ], 
    [ 
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1], 
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6], 
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], 
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12] 
    ], 
    [ 
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7], 
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2], 
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8], 
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11] 
    ]]

    def singleString(self,s):
        return ''.join(s.split())

    def hexToBin(self,n):
        return bin(int(n,16))

    def binToHex(self,n):
        n=self.singleString(n)
        temp=hex(int(n,2))[2:]
        return '0'*(16-len(temp))+temp

    def crank(self,msg,table):
        msg=self.singleString(msg)
        s=''
        for i in range(len(table)):
            s+=msg[table[i]-1]
        return s
    
    def pretty(self,s):
        s=self.singleString(s)
        t=''
        i=0
        if len(s)==64 or len(s)==16:
            i=4
        else:
            i=len(s)//8
        for j in range(i,len(s)+1,i):
            t+=s[j-i:j]+' '
        return t

    def initialPermutation(self,msg):
        return self.crank(self.singleString(msg),self.initial_permutation)

    def inversePermutation(self,msg):
        return self.crank(self.singleString(msg),self.inverse_permutaion)

    def expansion(self,msg):
        return self.crank(self.singleString(msg),self.exp_table)

    def keyToFiftySix(self,key):
        key=self.singleString(key)
        t=''
        for i in range(len(key)):
            if i==0 or i%8!=0:
                t+=key[i]
        return t
    
    def pc1(self,key):
        return self.crank(self.singleString(key),self.pc1_table)

    def shiftLeft(self,key,round):
        key=self.singleString(key)
        left=key[0:28]
        right=key[28:]
        i=self.shifts[round-1]
        return (left[i:len(left)]+left[0:i])+(right[i:len(right)]+right[0:i])

    def pc2(self,key):
        return self.crank(self.singleString(key),self.pc2_table)

    def xor(self,s1,s2):
        s1=self.singleString(s1)
        s2=self.singleString(s2)
        ans=''
        for i in range(len(s1)):
            ans+=str(int(s1[i])^int(s2[i]))
        return ans

    def sBox(self,msg):
        msg=self.singleString(msg)
        ans,n='',0
        for i in range(0,48,6):
            temp=msg[i:i+6]
            row=int(temp[0]+temp[5],2)
            col=int(temp[1:5],2)
            l=bin(self.s_boxes[n][row][col])[2:]
            ans+='0'*(4-len(l))+l
            n+=1
        return ans

    def bitShuffle(self,msg):
        return self.crank(self.singleString(msg),self.bit_shuffle)

    def generateKeys(self,key):
        key=self.singleString(key)
        key=self.pc1(key)
        print(self.pretty(key))
        for i in range(16):
            key=self.shiftLeft(key,i+1)
            self.shifted_keys.append(key)
            self.keys.append(self.pc2(key))

    def solve(self,msg,key,round):
        msg=self.singleString(msg)
        key=self.singleString(key)
        r_half,l_half='',''
        print("Input message m:")
        print(self.pretty(msg))
        print("After applying initial permutation we get:")
        msg=self.initialPermutation(msg)
        print(self.pretty(msg))
        print("After applying message expansion to the right half, we get:")
        r_half=msg[32:]
        l_half=msg[0:32]
        r_half=self.expansion(r_half)
        print(self.pretty(r_half))
        print("Given key string is given below:")
        print(self.pretty(key))
        print("Now applying PC-1 we get: ")
        key=self.pc1(key)
        print(self.pretty(key))
        print("Rotating {} bit to the left we get:".format(self.shifts[round]))
        key=self.shiftLeft(key,round)
        print(self.pretty(key))
        print("Applying PC-2 we get:")
        key=self.pc2(key)
        print(self.pretty(key))
        print("Xor-ing with right half:")
        r_half=self.xor(r_half,key)
        print(self.pretty(r_half))
        print("Applying S-box we get:")
        r_half=self.sBox(r_half)
        print(self.pretty(r_half))
        print("Applying bit shuffling we get:")
        r_half=self.bitShuffle(r_half)
        print(self.pretty(r_half))
        print("Now Xor-ing with left half will give:")
        r_half=self.xor(r_half,l_half)
        print(self.pretty(r_half))
        print("Encrypted message for this round is:")
        print('Binary:\n'+self.pretty(l_half)+self.pretty(r_half))
        print('Hex:\n'+self.pretty(self.binToHex(msg[32:]+r_half)))
        return msg[32:]+r_half
"""
Find-s Algorithm :
1. Load Data set
2. Initialize h to the most specific hypothesis in H
3. For each positive training instance x
• For each attribute constraint ai in h
If the constraint ai in h is satisfied by x then do nothing
else replace ai in h by the next more general constraint that is satisfied by x
4. Output hypothesis h
"""

import csv
def loadCsv(filename):
 lines = csv.reader(open(filename, "r"))
 dataset = list(lines)
 for i in range(len(dataset)):
 dataset[i] = dataset[i]
 return dataset
attributes = ['Sky','Temp','Humidity','Wind','Water','Forecast']
print('Attributes =',attributes)
num_attributes = len(attributes)
filename = "finds.csv"
dataset = loadCsv(filename)
print(dataset)
hypothesis=['0'] * num_attributes
print("Intial Hypothesis")
print(hypothesis)
print("The Hypothesis are")
for i in range(len(dataset)):
 target = dataset[i][-1]
 if(target == 'Yes'):
 for j in range(num_attributes):
 if(hypothesis[j]=='0'):
 hypothesis[j] = dataset[i][j]
 if(hypothesis[j]!= dataset[i][j]):
 hypothesis[j]='?'
 print(i+1,'=',hypothesis)
print("Final Hypothesis")
print(hypothesis)


"""
or
"""

import random
import csv
def read_data(filename):
 with open(filename, 'r') as csvfile:
 datareader = csv.reader(csvfile, delimiter=',')
 traindata = []
 for row in datareader:
 traindata.append(row)
 return (traindata)
h=['phi','phi','phi','phi','phi','phi'
data=read_data('finds.csv')
def isConsistent(h,d):
 if len(h)!=len(d)-1:
 print('Number of attributes are not same in hypothesis.')
 return False
 else:
 matched=0
 for i in range(len(h)):
 if ( (h[i]==d[i]) | (h[i]=='any') ):
 matched=matched+1
 if matched==len(h):
 return True
 else:
 return False
def makeConsistent(h,d):
for i in range(len(h)):
 if((h[i] == 'phi')):
 h[i]=d[i]
 elif(h[i]!=d[i]):
 h[i]='any'
 return h
print('Begin : Hypothesis :',h)
print('==========================================')
for d in data:
 if d[len(d)-1]=='Yes':
 if ( isConsistent(h,d)):
 pass
 else:
 h=makeConsistent(h,d)
 print ('Training data :',d)
 print ('Updated Hypothesis :',h)
 print()
 print('--------------------------------')
print('==========================================')
print('maximally sepcific data set End: Hypothesis :',h)

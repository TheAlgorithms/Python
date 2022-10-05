"""
Program to split bills among a group by given
- Number of people in group. eg: 5
- Name of contributer and amount of contribution separated by space. eg: John 100

"""
from os import system
def createContri(s:str):
  '''
  >>> createContri('Rohan 500')
  {'name': 'Rohan', 'contri': 500}
  >>> createContri('Sam 10')
  {'name': 'Sam', 'contri': 10}
  >>> createContri('Peter 0')
  {'name': 'Peter', 'contri': 0}
  '''
  s=s.split(' ')
  return {'name':s[0],'contri':int(s[1])}

#function to split bill among group
#pool: [...{'name':str,'contri':int},{'name':str,'contri':int}]
def splitBill(pool):
  '''
  >>> splitBill([{'name': 'sam', 'contri': 500}, {'name': 'rohan', 'contri': 200}, {'name': 'john', 'contri': 50}])
  {'sol': [{'name': 'sam', 'payment': [{'name': 'rohan', 'contri': 50.0}, {'name': 'john', 'contri': 200.0}]}], 'total': 750, 'each': 250.0, 'pool': [{'name': 'sam', 'contri': 500}, {'name': 'rohan', 'contri': 200}, {'name': 'john', 'contri': 50}]}
  '''
  contriList=[x['contri'] for x in pool]
  total=sum(contriList)
  each=total/len(contriList)
  more=[]
  less=[]
  sol=[]
  for i in pool:
    if i['contri']<each:
      less.append({'name':i['name'],'contri':each-i['contri']})
    else:
      more.append({'name':i['name'],'contri':i['contri']-each})
  for i in more:
    a=i['contri']
    m = [{'name':k['name'],'contri':0} for k in less]
    for j in range(len(less)):
      b=less[j]['contri']
      if a==0:
        m[j]['contri']=0
      elif a-b==0:
        a=a-b
        m[j]['contri']=b
        less[j]['contri']=0
      elif a-b>0:
        a=a-b
        less[j]['contri']=0
        m[j]['contri']=b
      elif a-b<0:
        less[j]['contri']=b-a
        m[j]['contri']=a
        a=0
    sol.append({'name':i['name'],'payment':m})
  return {'sol':sol,'total':total,'each':each,'pool':pool}

#function to print solution in a format
def printSolution(result):
  for i in result['pool']:
    print(i['name'],' paid    $',i['contri'])
  print('-------------------------------------------------------------------------------')
  print('Total pool amount  : $',result['total'])
  print('Per head           : $',result['each'])
  print('-------------------------------------------------------------------------------')
  for i in result['sol']:
    for j in i['payment']:
      if j['contri']>0:
        print(j['name'],' should pay $',j['contri'],' to ', i['name'])
    print('-------------------------------------------------------------------------------')

def printBanner():
  banner='''
███████╗██████╗ ██╗     ██╗████████╗    ██████╗ ██╗██╗     ██╗     ███████╗
██╔════╝██╔══██╗██║     ██║╚══██╔══╝    ██╔══██╗██║██║     ██║     ██╔════╝
███████╗██████╔╝██║     ██║   ██║       ██████╔╝██║██║     ██║     ███████╗
╚════██║██╔═══╝ ██║     ██║   ██║       ██╔══██╗██║██║     ██║     ╚════██║
███████║██║     ███████╗██║   ██║       ██████╔╝██║███████╗███████╗███████║
╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝       ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝     
  '''
  print(banner)

system('cls')
printBanner()
pool=[]
n=int(input('Number of participants : '))
for i in range(n):
  print('Enter name and contribution of participant ',i+1,' : ')
  pool.append(createContri(input()))
system('cls')
printBanner()
printSolution(splitBill(pool))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
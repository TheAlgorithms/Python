
import csv
def get_int(prompt,low):
    
    returnLoan=int(input(prompt))
    return returnLoan
def get_float(prompt,low):
    
    getFloat=float(input(prompt))
    return getFloat
def calculate_simple_interest(principle,interest_rate,year=1):
        simpleInterest = principle*(interest_rate/100)*year
        return simpleInterest
def write_to_csv(file_name,data,col_separator):
    header=['Loan', 'Rate', 'Time', 'Interest']
    with open(file_name,"w",newline='\n') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
        
def read_and_display(file_name,col_separator=","):
    r=[]
    with open(file_name,'r') as f:
        csvreader=csv.reader(f)
        flag=0
        for row in csvreader:
            if(flag==0):
                flag=1
                print(row,"\n")
            else:
                for rows in row:
                    s=''
                    l=[]
                    print(rows)
                    l=list(rows.split(","))
                    s="The interest on a loan of $"+str(l[0][1:])+" at "+str(l[1])+"% interest rate for "+str(l[2])+" yearsis $"+str(l[3][0:-1])+"."
                    r.append(s)
                    
    for i in r:
        print(i)
    f.close()
        
        
result=[]
while(True):
    while(True):
        principle=get_int("Please enter the amount of loan:",0)
        if(principle<=0):
            print("Entry must be an integer greater than 0 please try again")
        else:
            break
    while(True):
        interestRate=get_float("Please enter the interest rate:",0)
        if(interestRate<0):
            print("Entry must be a floating number greater than 0 Please try again")
        else:
            break
    while(True):
        year=get_int("Please enter the number of years:",0)
        if(year<0):
            print("Entry must be an integer greater than 0 Please try again")
        else:
            break
    result.append([principle,interestRate,year,calculate_simple_interest(principle,interestRate,year)])
    
    choice=input("Do you want to do another calculation? (y for yes)")
    if(choice=='n'):
        
        write_to_csv("simple.CSV",result,",")
        break
read_and_display("simple.CSV",",")
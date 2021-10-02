# Reading from a file

# "r" for reading,"w" is for writng,"a" is for append, "r+"

employee_file = open("employee.txt","r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()

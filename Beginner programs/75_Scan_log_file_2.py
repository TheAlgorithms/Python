# this program is for mine a log file whether it contains python string in it and also print where is that sring in which line. 

content=True
i=1
with open("log.txt") as f:
    
    while content:

        content=f.readline() # it will read line

        if 'python' in content.lower():
            print(content)  
            print(f"Yes Python is present on line number-{i}")
        i+=1
import os

path = '\\examplepc\smb'

#check if network path available and user has rights to access it
def check_share(path:str)->bool:
    if os.path.exists(path):
        err = 1
        return True
    else:
        err = 0
        return False
      
#check if user has rights for network path
def check_rights(path:str)->bool:
    try:
        os.listdir(path)
        return True
    except:
        i = 2
        return False
      
#return error to stdout if i <> 1
def check_share_error(i:int):
    if i == 0:
        print("Network path not available")
    elif i == 2:
        print("User has no rights to access network path")
    else:
        print("Network path available and user has rights to access it")
      
#first check if share exist, then check if user has rights to access it
def check_share_rights(path:str):
    if check_share(path) is True:
        check_share_error(check_rights(path))
    else:
        check_share_error(0)
      
#call function
check_share_rights(path)

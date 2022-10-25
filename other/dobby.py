import os

print("                  [ DOBBY ]              ")
print("[     I'M VIRTUAL ASSISTANT HOW MAY I HELP YOU !!  ]")


p = input()
print("=>", p)


if "list" in p :
    print("I can start app like: CALCULATOR   ATOM   NOTEPAD   COMMAND PROMPT   CONTROL PANEL  "
          " \n BLUETOOTH  FTP  MAGNIFYER  TASK MANAGER  PAINT "
          "\n USER ACCOUNTS   ONSCREEN KEYBOARD   SYSTEM PERFORMANCE   STEP RECORDER   SNIPPING TOOL  "
          "\n VOL+-  CHECK WINDOWS INFORMATION   WORDPAD   PYTHON TERMINAL "
          " FILE EXPLORER   VLC PLAYER  INTERNET BROWSER")

elif("calculator" in p):
    print(os.system("calc"), end="")

elif ("atom" in p):
    print(os.system("atom"), end="")

elif ("notepad" in p):
    print(os.system("notepad"), end="")

elif ("command" in p):
    print(os.system("cmd"), end="")

elif ("panel" in p):
    print(os.system("control"), end="")

elif ("bluetooth" in p):
    print(os.system("fsquirt"), end="")

elif ("ftp" in p):
    print(os.system("ftp"), end="")

elif("magnifyer" in p):
    print(os.system("magnify"), end="")

elif ("task" in p):
    print(os.system("launchtm"), end="")

elif("paint" in p):
    print(os.system("mspaint"), end="")

elif("account" in p):
    print(os.system("netplwiz"), end="")

elif ("keyboard" in p):
    print(os.system("osk"), end="")

elif ("system performance" in p):
    print(os.system("perfmon"), end="")

elif("steps recorder" in p):
    print(os.system("psr"), end="")

elif("snipping tool" in p):
    print(os.system("snippingtool"), end="")

elif ("volume" in p):
    print(os.system("sndvol"), end="")

elif ("window" in p):
    print(os.system("winver "), end="")

elif ("start" in p) and ("run" in p) or ("wordpad" in p):
    print(os.system("write"), end="")

elif ("python" in p) or("terminal" in p):
    print(os.system("py"), end="")

elif ("open" in p) and ("run" in p) or ("file explorer" in p):
    print(os.system("explorer"), end="")

elif ("vlc" in p):
    print(os.system("vlc"), end="")

elif "browser" in p:
    print(os.system("msedge"), end="")

elif ("logoff" in p) and ("computer" in p):
 choices = input("Logoff your computer ? (y or n)")
 if choices == "y" or choices == "Y":
    print(os.system("shutdown /l"), end="")

elif ("shutdown" in p) and ("computer" in p):
 choices = input("Shut down your computer ? (y or n)")
 if choices == "y" or choices =="Y":
    print(os.system("shutdown /s"), end="")


elif ("restart" in p) and ("computer" in p):
 choices = input("Do you want to restart your computer ? (y and n)")
 if choices == "y" or choices =="Y":
    print(os.system("shutdown /r"), end="")

else:
 print(" INVALID COMMAND !! Exiting the program doing nothing")
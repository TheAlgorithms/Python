f=open('poems.txt')
t=f.read()
if  'twinkle' in t:
    print("twinkle is present")
else:
    print("Twinkle is not present")

f.close()
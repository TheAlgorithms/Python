from PIL import Image

im = Image.open("Sample.png")

reply = 0
print("What you want to do??")
print("Enter 1 to flip image left to right")
print("Enter 2 to flip image Top to Bottom")
print("Enter 0 to show original photo")
reply = int(input("Enter your choice:  "))
if(reply == 1):
    im1 = im.transpose(Image.FLIP_LEFT_RIGHT)
    im1.show()
elif (reply == 2):
    im1 = im.transpose(Image.FLIP_TOP_BOTTOM)
    im1.show()
elif(reply==0):
    im.show()
else:
    print("Wrong value entered Retry")

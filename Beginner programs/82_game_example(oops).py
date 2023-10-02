class Remote:
    pass

class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1=Remote()
player1=Player()

if(remote1.isleftpressed()):
    player1.moveLeft()
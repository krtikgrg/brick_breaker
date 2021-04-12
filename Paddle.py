import globals
class Paddle:
    def __init__(self,x,y):
        self.symbol = globals.PADDLE
        self.xCor = x
        self.yCor = y
        self.grabBall = 0
        self.size = 13
    def getSize(self):
        return self.size
    def expand(self):
        self.symbol = globals.PADDLEEXTENDED
        self.size = len(self.symbol)
        if globals.shootingPowerUp != "":
            self.changeSymbol()
    def shrink(self):
        self.symbol = globals.PADDLESHRINKED
        self.size = len(self.symbol)
        if globals.shootingPowerUp != "":
            self.changeSymbol()
    def normal(self):
        self.symbol = globals.PADDLE
        self.size = len(self.symbol)
        if globals.shootingPowerUp != "":
            self.changeSymbol()
    def setGrab(self,val):
        self.grabBall = val
    def getGrabStatus(self):
        return self.grabBall
    def changeSymbol(self):
        length = len(self.symbol)
        if length == 13:
            self.symbol = globals.PADDLEFIRE
        elif length == 17:
            self.symbol = globals.PADDLEFIREEXTENDED
        else:
            self.symbol = globals.PADDLEFIRESHRINKED
    def restoreSymbol(self):
        length = len(self.symbol)
        if length == 13:
            self.symbol = globals.PADDLE
        elif length == 17:
            self.symbol = globals.PADDLEEXTENDED
        else:
            self.symbol = globals.PADDLESHRINKED
import globals
class Ball:
    def __init__(self,x,y):
        self.symbol = "@"
        self.xCor = x #row number
        self.yCor = y #column number
        self.thruBall = 0
        self.xSpeed = -1 #horizontal
        self.ySpeed = 1 #vertical
        self.movBall = 0
        globals.balls.append(self)
        globals.Number_Of_Balls +=1

    def updateCords(self,x,y):
        self.xCor = x
        self.yCor = y
    def removeBall(self):
        return self.xCor,self.yCor
    
    def addBall(self):
        return self.xCor,self.yCor

    def getBallStatus(self):
        return self.movBall

    def setBallStatus(self,status):
        self.movBall = status

    def activeThruBall(self):
        self.thruBall = 1

    def deactiveThruBall(self):
        self.thruBall = 0

    def getSpeed(self):
        return self.ySpeed

    def incSpeed(self):
        if abs(self.ySpeed) != 2:
            self.ySpeed *=2
            self.xSpeed *=2 

    def decSpeed(self):
        if abs(self.ySpeed)!= 1:
            self.ySpeed = int(self.ySpeed/2)
            self.xSpeed = int(self.xSpeed/2)

    def moveBall(self):
        corX = self.xCor
        corY = self.yCor
        velX = int(self.xSpeed/abs(self.ySpeed))
        velY = int(self.ySpeed/abs(self.ySpeed))
        for i in range(abs(self.ySpeed)):
            ple,corX,corY,revertY,revertX = globals.canvas.checkCollision(corX,corY,velY,velX,self)
            if(ple == 0):
                if(revertY == 1):
                    velY = 0 - velY
                if(revertX == 1):
                    velX = 0 - velX
            elif ple == 1:
                # if globals.fallBrick == 1:
                    # globals.canvas.drop()
                if (revertX == -1):
                    return -1,revertY,1
                else:
                    self.ySpeed = 0-self.ySpeed
                    sin = int(self.xSpeed/abs(self.xSpeed))
                    self.xSpeed = abs(revertX * self.ySpeed)*sin
                    self.xCor =corX
                    self.yCor = corY
                    if globals.pedal.getGrabStatus() == 1:
                        self.movBall = 0
                    return self.xCor,self.yCor,1
            else:
                self.ySpeed = 0-self.ySpeed
                self.xSpeed = 0-self.xSpeed
                self.xCor = corX
                self.yCor = corY
                return self.xCor,self.yCor,0
        #print(self.xSpeed)
        #print(self.ySpeed)
        if velY != int(self.ySpeed/abs(self.ySpeed)):
            self.ySpeed = 0- self.ySpeed
        if velX != int(self.xSpeed/abs(self.ySpeed)):
            self.xSpeed = 0-self.xSpeed
        #print(corX)
        #print(corY)
        self.xCor = corX
        self.yCor = corY
        #print(self.xSpeed)
        #print(self.ySpeed)
        return self.xCor,self.yCor,0
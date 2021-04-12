import time
import globals
from Ball import Ball
import copy
class PowerUp:
    def __init__(self,x,y,speedX,speedY):
        self.xCor = x
        self.yCor = y
        self.active = 0
        self.xSpeed = speedX
        self.ySpeed = speedY
        self.ultimateSpeed = -abs(self.ySpeed)
        self.ctr = 0
        globals.powerUp.append(self)
    def getStatus(self):
        return self.active
    def movePowerUp(self):
        globals.canvas.movePowerUp(self.xCor,self.yCor,self,self.xSpeed,self.ySpeed,self.ultimateSpeed)
    def getTme(self):
        return self.tme
    def updateCords(self,x,y):
        self.xCor = x
        self.yCor = y
    def updateVel(self,velX,velY):
        self.xSpeed = velX
        self.ySpeed = velY

class ExpandPaddle(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = "+"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        self.active = 1
        self.tme = time.perf_counter()
        globals.pedal.expand()
    def becomeInActive(self):
        if self.active == 1:
            globals.pedal.normal()
        self.active = 2

class ShrinkPaddle(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = "-"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        self.active = 1
        self.tme = time.perf_counter()
        globals.pedal.shrink()
    def becomeInActive(self):
        if self.active == 1:
            globals.pedal.normal()
        self.active = 2

class BallMultiplier(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = "%"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        tlist = []
        for i in range(len(globals.balls)):
            if globals.balls[i]!= " ":
                newBall = copy.deepcopy(globals.balls[i])
                globals.Number_Of_Balls+=1
                if abs(newBall.getSpeed()) == 1:
                    newBall.incSpeed()
                else:
                    newBall.decSpeed()
                globals.balls[i].setBallStatus(1)
                newBall.setBallStatus(1)
                tlist.append(newBall)
                tlist.append(globals.balls[i])
        globals.balls = tlist
        self.active = 1
        self.tme = time.perf_counter()
    def becomeInActive(self):
        self.active = 2

class FastBall(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = ">"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        for i in range(len(globals.balls)):
            if globals.balls[i] != " ":
                globals.balls[i].incSpeed()
        self.active = 1
        self.tme = time.perf_counter()
    def becomeInActive(self):
        for i in range(len(globals.balls)):
            if globals.balls[i] != " ":
                globals.balls[i].decSpeed()
        self.active = 2

class ThruBall(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = "/"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        for i in range(len(globals.balls)):
            if isinstance(globals.balls[i],(Ball)):
                globals.balls[i].activeThruBall()
        self.active = 1
        self.tme = time.perf_counter()
    def becomeInActive(self):
        if self.active == 1:
            for i in range(len(globals.balls)):
                if isinstance(globals.balls[i],(Ball)):
                    globals.balls[i].deactiveThruBall()
        self.active = 2


class PaddleGrab(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = "#"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        globals.pedal.setGrab(1)
        self.active = 1
        self.tme = time.perf_counter()
    def becomeInActive(self):
        globals.pedal.setGrab(0)
        self.active = 2
        for i in range(len(globals.balls)):
            if globals.balls[i] != " ":
                globals.balls[i].setBallStatus(1)

class PaddleShoot(PowerUp):
    def __init__(self,x,y,speedX,speedY):
        self.symbol = "!"
        super().__init__(x,y,speedX,speedY)
    def becomeActive(self):
        if globals.shootingPowerUp == "":
            globals.shootingPowerUp = self
            self.active = 1
            globals.pedal.changeSymbol()
            self.tme = time.perf_counter()
        else:
            globals.shootingPowerUp.tme += 15
            self.active = 2
    
    def becomeInActive(self):
        if self.active == 1:
            globals.shootingPowerUp = ""
            globals.pedal.restoreSymbol()
        self.active = 2


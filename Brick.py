import globals
import random
from Ball import Ball
from Paddle import Paddle
from PowerUp import PowerUp
from Bullet import Bullet
import os
class Brick:
    def __init__(self,x,y):
        self.symbol = "[|||]"
        self.xCor = x
        self.yCor = y

    def explode(self):
        oldstrength = self.strength
        self.strength = 0
        globals.Score += ((oldstrength - self.strength)*2)
        #if self.strength == 0:
        globals.canvas.generatePowerUp(self.xCor,self.yCor,0,-1)

    def getStrength(self):
        return self.strength

    def updateCords(self,x,y):
        self.xCor = x
        self.yCor = y

class DynamicBrick(Brick):
    def __init__(self,x,y,power):
        self.strength = power
        super().__init__(x,y)
    def getHit(self,ball = " ",eplode = 0):
        # os.system("aplay Explosion.wav > /dev/null 2>&1 &")
        if eplode == 1:
            #print("\033[40;1H gg,bois")
            super().explode()
            return 0
        else:
            oldstrength = self.strength
            self.strength -=1
            if ball != " ":
                if ball.thruBall == 1:
                    self.strength = 0
            globals.Score += ((oldstrength - self.strength)*2)
            if self.strength <= 0:
                self.strength = 0
                if ball != " ":
                    globals.canvas.generatePowerUp(self.xCor,self.yCor,ball.xSpeed,ball.ySpeed)
                else:
                    globals.canvas.generatePowerUp(self.xCor,self.yCor,0,-1)
            return 0
    #def getStrength(self):
    #    return self.strength

class FixedBrick(Brick):
    def __init__(self,x,y):
        self.strength = 4
        super().__init__(x,y)
    def getHit(self,ball = " ",eplode = 0):
        # os.system("aplay Explosion.wav > /dev/null 2>&1 &")
        if (globals.level == 4) and (globals.pressed == 0):
            if self.xCor < 7:
                globals.bossHealth -= 1
                # print("\033[40;1H Kartik "+str(globals.bossHealth))
            return 0

        if eplode == 1:
            #print("\033[40;1H gg,bois")
            super().explode()
            return 0
        else:
            if ball != " ":
                if ball.thruBall == 1:
                    self.strength = 0
                    globals.Score += 10
                    globals.canvas.generatePowerUp(self.xCor,self.yCor,ball.xSpeed,ball.ySpeed)
            return 0
            

    #def getStrength(self):
    #    return self.strength

class ExplodingBrick(Brick):
    def __init__(self,x,y):
        self.strength = -1
        super().__init__(x,y)

    #def getStrength(self):
    #    return self.strength

    
    def getHit(self,ball = " ",eplode = 0):
        # os.system("aplay Explosion.wav > /dev/null 2>&1 &")
        #print("\033[45;1H")
        #print(self.xCor)
        #print(self.yCor)
        if self.yCor > 0:
            for i in range(self.xCor-1,self.xCor+2):
                temp = []
                temp.append(i)
                temp.append(self.yCor-5)
                globals.temp_left_exploding.append(temp)
        if self.yCor<70 :
            for i in range(self.xCor-1,self.xCor+2):
                temp = []
                temp.append(i)
                temp.append(self.yCor+5)
                globals.temp_right_exploding.append(temp)
        globals.Score += 14
        super().explode()
        for i in range(self.yCor-4,self.yCor+5):
            if not(isinstance(globals.canvas.getComponent(self.xCor-1,i),(Paddle,PowerUp,Ball,Bullet))) and globals.canvas.getComponent(self.xCor-1,i)!= " ":
                globals.canvas.getComponent(self.xCor-1,i).getHit(ball,1)
            if not(isinstance(globals.canvas.getComponent(self.xCor+1,i),(Paddle,PowerUp,Ball,Bullet))) and globals.canvas.getComponent(self.xCor+1,i)!= " ":
                globals.canvas.getComponent(self.xCor+1,i).getHit(ball,1)
        return 0
        

class RainbowBrick(Brick):
    def __init__(self,x,y):
        self.strength = random.choices([1,2,3,4,-1])[0]
        super().__init__(x,y)

    def getHit(self,ball = " ",eplode = 0):
        # os.system("aplay Explosion.wav > /dev/null 2>&1 &")
        if eplode == 1:
            super().explode()
            return 0
        else:
            return 1


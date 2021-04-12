import random
import globals
from Brick import Brick,DynamicBrick,FixedBrick,ExplodingBrick,RainbowBrick
from Paddle import Paddle
from Ball import Ball
from Bullet import Bullet
from PowerUp import PowerUp,ExpandPaddle,ShrinkPaddle,BallMultiplier,FastBall,ThruBall,PaddleGrab, PaddleShoot
import time
colors= ["\033[1;37m","\033[0;34m","\033[0;32m","\033[0;36m","\033[0;37m","\033[1;33m"] #white,blue,green,cyan,grey.yellow
colorBoss = "\033[1;33m"

class Board:
    def __init__(self):
        self.length = 75
        self.height = 33
        compo = []
        for i in range(33):
            cur = []
            for j in range(75):
                cur.append(" ")
            compo.append(cur)
        self.components = compo

    def update(self):
        print("\033[2"+";"+str(9)+"H"+str(globals.Score))
        print("\033[2"+";"+str(41)+"H"+str(globals.Lives))
        print("\033[2"+";"+str(69)+"H"+str(globals.Tme))
        for i in range(1,32):
            j=0
            while j<75:
                if (self.components[i][j] != globals.oldConfig[i][j]) :
                    if isinstance(self.components[i][j],(Brick,DynamicBrick,FixedBrick)):
                        print(colors[4-self.components[i][j].strength])
                        print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                        j+=5
                    elif isinstance(self.components[i][j],(Ball)):
                        print(colors[0])
                        print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                        j+=1
                    else:
                        print("\033["+str(i+2)+";"+str(j+3)+"H"+" ")
                        j+=1
                else:
                    if isinstance(self.components[i][j],(Brick,DynamicBrick,FixedBrick)):
                        j+=5
                    elif isinstance(self.components[i][j],(Ball)):
                        j+=1
                    else:
                        j+=1    
        print(colors[0]);
        j=0
        while j<75:
            if isinstance(self.components[32][j],(Paddle)):
                print("\033[34;"+str(j+3)+"H"+self.components[32][j].symbol)
                j+=self.components[32][j].size
            else:
                print("\033[34;"+str(j+3)+"H"+" ")
                j+=1    

    def generateBullet(self):
        for i in range(75):
            if isinstance(self.components[32][i],(Paddle)):
                break
        bullet1 = Bullet(31,i,1)
        bullet2 = Bullet(31,i+len(self.components[32][i].symbol)-1,1)
        if not(isinstance(self.components[31][i],(Brick))):
            self.components[31][i] = bullet1
        if not(isinstance(self.components[31][i+len(self.components[32][i].symbol)-1],(Brick))):
            self.components[31][i+len(self.components[32][i].symbol)-1] = bullet2
             
    def dropBombBoss(self):
        for i in range(75):
            if isinstance(self.components[6][i],(Brick)):
                break
        i+=2
        bullet1 = Bullet(8,i,-1)
        bullet2 = Bullet(8,i+10,-1)
        self.components[8][i] = bullet1
        self.components[8][i+10] = bullet2

    def displayBoard(self):
        for j in range(75):
            print("\033[2;"+str(j+3)+"H"+self.components[0][j])
        if globals.shootingPowerUp == "":
            print("\033[2"+";"+str(9)+"H"+str(globals.Score))
            print("\033[2"+";"+str(41)+"H"+str(globals.Lives))
            print("\033[2"+";"+str(69)+"H"+str(int(time.perf_counter() - globals.Tme)))
        else:
            for j in range(75):
                print("\033[2;"+str(j+3)+"H"+" ")
            print("\033[2;3HScore:")
            print("\033[2"+";"+str(9)+"H"+str(globals.Score))
            print("\033[2;18HTimePowerup:")
            print("\033[2;30H"+str(int(globals.shootingPowerUp.tme+15-time.perf_counter())))
            print("\033[2;42HLives:")
            print("\033[2"+";"+str(48)+"H"+str(globals.Lives))
            print("\033[2;64HTime:")
            print("\033[2"+";"+str(69)+"H"+str(int(time.perf_counter() - globals.Tme)))
        if globals.level == 4 and globals.pressed == 0:
            strk = ""
            for i in range(globals.bossHealth):
                strk = strk + "+"
            for i in range(50-globals.bossHealth):
                strk = strk + " "
            print("\033[2;90HBoss Health:"+strk)
        for i in range(1,32):
            j=0
            while j<75:
                if isinstance(self.components[i][j],(Brick,DynamicBrick,FixedBrick)):
                    if not(isinstance(self.components[i][j],(FixedBrick))) or i>=7:
                        # print("\033[40;1H"+str(self.components[i][j].getStrength()))
                        print(colors[4-self.components[i][j].getStrength()])
                        print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                        if isinstance(self.components[i][j],(RainbowBrick)):
                            self.components[i][j] = " "
                            self.components[i][j] = RainbowBrick(i,j)
                    else:
                        if (globals.level == 4) and (globals.pressed == 0):
                            print(colorBoss)
                            print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                        else:
                            print(colors[4-self.components[i][j].getStrength()])
                            print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                    j+=5
                elif isinstance(self.components[i][j],(Ball)):
                    print(colors[0])
                    print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                    j+=1
                elif isinstance(self.components[i][j],(PowerUp)):
                    print(colors[0])
                    print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                    j+=1
                elif isinstance(self.components[i][j],(Bullet)):
                    print(colors[0])
                    print("\033["+str(i+2)+";"+str(j+3)+"H"+self.components[i][j].symbol)
                    j+=1
                else:
                    print("\033["+str(i+2)+";"+str(j+3)+"H"+" ")
                    j+=1
        print(colors[0])
        
        j=0
        while j<75:
            if isinstance(self.components[32][j],(Paddle)):
                print("\033[34;"+str(j+3)+"H"+self.components[32][j].symbol)
                j+=self.components[32][j].size
            else:
                print("\033[34;"+str(j+3)+"H"+" ")
                j+=1
        for i in range(0,33):
            print("\033["+str(i+2)+";"+"1"+"H"+"||")
            print("\033["+str(i+2)+";"+"78"+"H"+"||")
        for j in range(0,75):
            print("\033[1;"+str(j+3)+"H*")
            print("\033[35;"+str(j+3)+"H*")
        print("\033[35;1H ")
        print("\033[36;1H ")

    def spawnlayer(self):
        curind = 0
        if globals.trigger == 1:
            i=20
        elif globals.trigger == 0:
            i=21
        
        while curind<71:
            sel = random.choices([1,2,3]) #add 5,1 in the corresponding arrays if adding exploding in general
            if sel[0] == 0 :
                curind = curind + 1
            elif sel[0] == 1 :
                self.components[i][curind]= DynamicBrick(i,curind,3)
                curind = curind + 5
                globals.BreakableBricks += 1
            elif sel[0] == 2 :
                self.components[i][curind]= DynamicBrick(i,curind,2)
                curind = curind + 5
                globals.BreakableBricks += 1
            elif sel[0] == 3 :
                self.components[i][curind]= DynamicBrick(i,curind,1)
                curind = curind + 5
                globals.BreakableBricks += 1
            elif sel[0] == 6:
                self.components[i][curind]= RainbowBrick(i,curind)
                curind = curind + 5
                globals.BreakableBricks += 1
            else:
                self.components[i][curind]= FixedBrick(i,curind)
                curind = curind + 5  


    def moveBullet(self,x,y,velY,bullet):
        if velY>0:
            if x == 1:
                if isinstance(self.components[x][y],(Bullet)):
                    self.components[x][y] = " "
                return -1
            else:
                x -= 1
                j = y-4
                if j<0:
                    j=0
                for i in range(j,y+1):
                    if isinstance(self.components[x][i],(Brick)):
                        typ = self.components[x][i].getHit()
                        if typ == 1:
                            woahX = x
                            woahY = i
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        if isinstance(self.components[x+1][y],(Bullet)):
                            self.components[x+1][y] = " "
                        return -1
                bullet.updateCords(x,y)
                if not(isinstance(self.components[x][y],(Brick))):
                    self.components[x][y] = bullet
                if isinstance(self.components[x+1][y],(Bullet)):
                    self.components[x+1][y] = " "
                return 0
        else:
            if x == 31:
                for i in range(75):
                    if isinstance(self.components[32][i],(Paddle)):
                        break
                startI = i
                endI = i + len(self.components[32][i].symbol)-1
                if y<startI or y>endI:
                    if isinstance(self.components[x][y],(Bullet)):
                        self.components[x][y] = " "
                else:
                    globals.Lives -= 1
                    if isinstance(self.components[x][y],(Bullet)):
                        self.components[x][y] = " "
                return -1
            else:
                x += 1
                if not(isinstance(self.components[x][y],(Brick,Ball))):
                    self.components[x][y] = bullet
                if isinstance(self.components[x-1][y],(Bullet)):
                    self.components[x-1][y] = " "
                bullet.updateCords(x,y)
                return 0    
    def drop(self):
        for j in range(75):
            if isinstance(self.components[30][j],(DynamicBrick,RainbowBrick,ExplodingBrick)):
                globals.endGame = 1
        for i in range(30,1,-1):
            for j in range(75):
                self.components[i][j] = self.components[i-1][j]
                self.components[i-1][j] = " "
                if self.components[i][j]!= " ":
                    self.components[i][j].updateCords(i,j)
        return


    def getConfig(self):
        globals.oldConfig = self.components.copy()

    def getComponent(self,x,y):
        return self.components[x][y]

    def generatePowerUp(self,xCor,yCor,speedX,speedY):
        

        if isinstance(self.components[xCor][yCor],(DynamicBrick,ExplodingBrick,RainbowBrick)):
            globals.BreakableBricks -= 1
        check = 1
        # for i in range(xCor+1,32):
            # #if(isinstance(self.components[i][yCor+2],(Brick,DynamicBrick,FixedBrick))):
            # for j in range(yCor+2-4,yCor+2+1):
                # if(isinstance(self.components[i][j],(Brick,DynamicBrick,FixedBrick))):
                    # check = 0
                    # break
            # if check == 0:
                # break
        self.components[xCor][yCor] = " "
        if globals.level == 4 and globals.pressed == 0:
            return
        if check == 1:
            powerup = random.choices([0,1,2,3,4,5,6,7],weights = [2, 1, 1, 1, 1, 1, 1, 1])
            powerup = powerup[0]
            yCor+=2
            if powerup == 0:
                self.components[xCor][yCor] = " "
            elif powerup == 1:
                self.components[xCor][yCor] = ExpandPaddle(xCor,yCor,speedX,speedY)
            elif powerup == 2:
                self.components[xCor][yCor] = ShrinkPaddle(xCor,yCor,speedX,speedY)
            elif powerup == 5:
                self.components[xCor][yCor] = ThruBall(xCor,yCor,speedX,speedY)
            elif powerup == 4:
                self.components[xCor][yCor] = FastBall(xCor,yCor,speedX,speedY)
            elif powerup == 6:
                self.components[xCor][yCor] = PaddleGrab(xCor,yCor,speedX,speedY)
            elif powerup == 7:
                self.components[xCor][yCor] = PaddleShoot(xCor,yCor,speedX,speedY)
            else:
                self.components[xCor][yCor] = BallMultiplier(xCor,yCor,speedX,speedY)
                

    def movePowerUp(self,x,y,powerup,velX,velY,U_velY):
        powerup.ctr += 1
        if x==31:
            for i in range(75):
                if isinstance(self.components[32][i],(Paddle)):
                    paddleI = i
                    break
            paddleE = paddleI - 1 + self.components[32][paddleI].getSize()
            if y>=paddleI and y<=paddleE:
                powerup.becomeActive()
            else:
                powerup.becomeInActive()
            if not(isinstance(self.components[x][y],(Brick))):
                self.components[x][y] = " "
        else:

            #velX will change y coordinate
            #velY will change x coordinate

            #self.components[x+1][y]=self.components[x][y]
            #self.components[x][y]=" "
            #self.components[x+1][y].updateCords(x+1,y)
            finX = x
            finY = y

            if velY > 0:            
                finX -= velY
                if finX < 1:
                    finX = 1+1-finX
                    velY = -velY
            else:
                finX -= velY
                if finX>31:
                    finX = 31
            if velX > 0:
                finY += velX
                if finY > 74:
                    finY = 74 -finY+74
                    velX = -velX
            else:
                finY += velX
                if finY<0:
                    finY = -finY
                    velX = -velX
            #if velY> U_velY:
            if powerup.ctr%3 == 0:
                velY -= 1
            powerup.updateCords(finX,finY)
            powerup.updateVel(velX,velY)
            if not(isinstance(self.components[finX][finY],(Brick))):
                self.components[finX][finY] = powerup
            if not(isinstance(self.components[x][y],(Brick))):
                self.components[x][y] =" "

    def moveBall(self):
        testlist = []
        for i in range(32):
            for j in range(75):
                if isinstance(self.components[i][j],(Ball)):
                    if(self.components[i][j] in testlist):
                        continue
                    else:
                        x,y = self.components[i][j].moveBall()
                        if x!=-1:
                            self.components[x][y] = self.components[i][j]
                            if not((x==i) and(y==j)):
                                self.components[i][j] = " "
                            testlist.append(self.components[x][y])
                        else:
                            globals.moveBall = 0
                            globals.Lives -= 1 #for multiple ball change will occur here
                            self.components[i][j] = " "
                            self.components[31][y] = Ball(31,y)
                            return
                             
    def finMoveBall(self,ball,i):
        c,d = ball.removeBall()
        x,y,ple = ball.moveBall()
        #print("\033[43;1H"+str(x)+" "+str(y))
        if x!=-1:
            self.components[c][d] = " "
            self.components[x][y] = ball
        else:
            self.components[c][d] = " "
            globals.balls[i] = " "
            globals.Number_Of_Balls -= 1
            if globals.Number_Of_Balls == 0:
                globals.Lives -= 1
                balln = Ball(31,y)
                self.components[31][y] = balln
        
        if (ple == 1) and (globals.fallBrick == 1):
            self.drop()
        return

    def setNull(self,xCor,yCor):
        self.components[xCor][yCor] = " "
        return
    
    def setBall(self,ball,xCor,yCor):
        self.components[xCor][yCor]=ball

    def moveBoss(self,c):
        if c == 'a':
            if isinstance(self.components[4][0],(Brick)):
                return
            else:
                check = 1
                i = 1
                while(i<7):
                    j=0
                    while(j<75):
                        if isinstance(self.components[i][j],(Brick)):
                            break
                        j+=1
                    if isinstance(self.components[i][j-1],(Ball)):
                        check = 0
                        return
                    else:
                        i+=1
                for i in range(1,7):
                    j=0
                    while j<75:
                        if isinstance(self.components[i][j],(Brick)):
                            self.components[i][j] = " "
                            self.components[i][j-1] = FixedBrick(i,j-1)
                            j += 5
                        else:
                            j+=1
        else:
            if isinstance(self.components[4][70],(Brick)):
                return
            else:
                
                check = 1
                i = 1
                while(i<7):
                    j=74
                    while(j>=0):
                        if isinstance(self.components[i][j],(Brick)):
                            break
                        j-=1
                    if isinstance(self.components[i][j+1],(Ball)):
                        check = 0
                        return
                    else:
                        i+=1

                for i in range(1,7):
                    j=74
                    while j>=0:
                        if isinstance(self.components[i][j],(Brick)):
                            self.components[i][j] = " "
                            self.components[i][j+1] = FixedBrick(i,j+1)
                            j -= 5
                        else:
                            j-=1

    def movePaddle(self,c):
        j=0
        while j<75:
            if(isinstance(self.components[32][j],(Paddle))):
                if c=='a':
                    if j>0:
                        self.components[32][j-1]=self.components[32][j]
                        self.components[32][j] = " "
                        #if globals.moveBall == 0:
                        #    for i in range(75):
                        #        if isinstance(self.components[31][i],(Ball)):
                        #            if(i>0):
                        #                self.components[31][i-1]=self.components[31][i]
                        #                self.components[31][i]=" "
                        #                self.components[31][i-1].updateCords(31,i-1)
                        for i in range(len(globals.balls)):
                            if isinstance(globals.balls[i],(Ball)):
                                if globals.balls[i].getBallStatus() == 0:
                                    c,d = globals.balls[i].removeBall()
                                    if d>0:
                                        globals.balls[i].updateCords(c,d-1)
                                        self.components[c][d-1]=globals.balls[i]
                                        self.components[c][d] = " "
                else:
                    temp = j+self.components[32][j].getSize()
                    if temp < 75:
                        self.components[32][j+1]=self.components[32][j]
                        self.components[32][j] = " "
                        #if globals.moveBall == 0:
                        #    for i in range(74,-1,-1):
                        #        if isinstance(self.components[31][i],(Ball)):
                        #            if(i<74):
                        #                self.components[31][i+1]=self.components[31][i]
                        #                self.components[31][i]=" "
                        #                self.components[31][i+1].updateCords(31,i+1)
                        for i in range(len(globals.balls)):
                            if isinstance(globals.balls[i],(Ball)):
                                if globals.balls[i].getBallStatus() == 0:
                                    c,d = globals.balls[i].removeBall()
                                    if d<74:
                                        globals.balls[i].updateCords(c,d+1)
                                        self.components[c][d+1]=globals.balls[i]
                                        self.components[c][d] = " "
                j=75
            else:
                j+=1
    def getBounds(self,X,finX,Y):
        rightBd = 75
        leftBd = -1
        brickRX = 0
        brickLX = 0
        for i in range(Y+1,75,1):
            if(isinstance(self.components[finX][i],(Brick,DynamicBrick,FixedBrick,Paddle))):
                rightBd = i
                brickRX = finX 
                break
            if(isinstance(self.components[X][i],(Brick,DynamicBrick,FixedBrick,Paddle))):
                rightBd = i
                brickRX = X
                break
        for i in range(Y-1,-1,-1):
            if(isinstance(self.components[finX][i],(Brick,DynamicBrick,FixedBrick,Paddle))):
                if not(isinstance(self.components[finX][i],(Paddle))):
                    leftBd = i+4
                else:
                    leftBd = i+self.components[finX][i].getSize()-1
                brickLX = finX 
                break
            if(isinstance(self.components[X][i],(Brick,DynamicBrick,FixedBrick,Paddle))):
                if not(isinstance(self.components[X][i],(Paddle))):
                    leftBd = i+4
                else:
                    leftBd = i+self.components[X][i].getSize()-1
                brickLX = X
                break
        return leftBd,rightBd,brickLX,brickRX
    def checkCollision(self,X,Y,vY,vX,ball):
        brickUp = 0
        brickBelow = 0
        brickUpI = " "
        brickBelowI = " "
        brickSameR = 75
        brickSameL = -1
        brickOtherR = 75
        brickOtherL = -1
        rightBound = 75
        leftBound = -1
        strt = Y-4
        finY = -1
        finX = -1
        revertX = 0
        revertY = 0
        factY = -1
        if ball.thruBall == 1:
            if vY>0:
                if X==1:
                    finX = 2
                    revertY = 1
                else:
                    finX = X-1
            else:
                if X == 31:
                    finX = 31
                    paddleI = -1
                    paddleE = -1
                    for i in range(75):
                        if(isinstance(self.components[32][i],(Paddle))):
                            paddleI = i
                            break
                    paddleE = paddleI-1+self.components[32][paddleI].getSize()
                    if (Y>=paddleI) and (Y<=paddleE):
                        finY = Y
                        k=abs(int((paddleE+paddleI)/2) - Y)-1
                        if(k<0):
                            factX = 1
                        else:
                            factX = int(k/2)+2
                    elif Y<paddleI:
                        finY = Y
                        if vX>0:
                            if (Y+vX+1)>= paddleI:
                                finY = paddleI
                                finX = 31
                                k = int((paddleE-paddleI)/2)-1
                                factX = int(k/2)+2
                            else:
                                factX = -1
                        else:
                            if (abs(vX)-Y+1) >=paddleI:
                                finY = paddleI
                                finX = 31
                                k = int((paddleE-paddleI)/2)-1
                                factX = int(k/2)+2
                            else:
                                factX = -1
                    elif Y>paddleE:
                        finY = Y
                        if(vX<0):
                            if(Y+vX-1)<=paddleE:
                                finY = paddleE
                                finX = 31
                                k = int((paddleE-paddleI)/2)-1
                                factX = int(k/2)+2
                            else:
                                factX = -1
                        else:
                            if(147-vX-Y)<=paddleE:
                                finY = paddleE
                                finX = 31
                                k = int((paddleE-paddleI)/2)-1
                                factX = int(k/2)+2
                            else:
                                factX = -1
                    if(factX == -1):
                        factY = int((paddleI+paddleE)/2)
                    return 1,finX,finY,factY,factX
                else:
                    finX = X+1
            finY = Y
            for i in range(abs(vX)):
                for j in range(finY-4,finY+1):
                    if j>=0 and isinstance(self.components[X][j],(Brick,DynamicBrick,FixedBrick)):
                        ifchnge = self.components[X][j].getHit(ball)
                        if ifchnge == 1:
                            woahX = X
                            woahY = j
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                    if j>=0 and isinstance(self.components[finX][j],(Brick,FixedBrick,DynamicBrick)):
                        ifchnge = self.components[finX][j].getHit(ball)
                        if ifchnge == 1:
                            woahX = finX
                            woahY = j
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                if(vX>0):
                    finY+=1
                elif (vX<0):
                    finY-=1
                if finY == 75:
                    finY = 73
                    revertX = 1 -revertX
                    vX = 0-vX
                elif finY == -1:
                    finY = 1
                    revertX = 1 - revertX
                    vX = 0-vX
            for j in range(finY-4,finY+1):
                if j>=0 and isinstance(self.components[X][j],(Brick,DynamicBrick,FixedBrick)):
                    ifchnge = self.components[X][j].getHit(ball)
                    if ifchnge == 1:
                        woahX = X
                        woahY = j
                        streng = self.components[woahX][woahY].getStrength()
                        if streng == 4:
                            self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                            globals.BreakableBricks -= 1
                        elif streng == -1:
                            self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                        else:
                            self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                if j>=0 and isinstance(self.components[finX][j],(Brick,FixedBrick,DynamicBrick)):
                    ifchnge = self.components[finX][j].getHit(ball)
                    if ifchnge == 1:
                        woahX = finX
                        woahY = j
                        streng = self.components[woahX][woahY].getStrength()
                        if streng == 4:
                            self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                            globals.BreakableBricks -= 1
                        elif streng == -1:
                            self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                        else:
                            self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
            return 0,finX,finY,revertY,revertX

        brickUp = 0
        brickBelow = 0
        brickUpI = " "
        brickBelowI = " "
        brickSameR = 75
        brickSameL = -1
        brickOtherR = 75
        brickOtherL = -1
        rightBound = 75
        leftBound = -1
        strt = Y-4
        finY = -1
        finX = -1
        revertX = 0
        revertY = 0
        factY = -1
        if(X == 31) and (vY<0):
            finX = 31
            paddleI = -1
            paddleE = -1
            for i in range(75):
                if(isinstance(self.components[32][i],(Paddle))):
                    paddleI = i
                    break
            paddleE = paddleI-1+self.components[32][paddleI].getSize()
            if (Y>=paddleI) and (Y<=paddleE):
                finY = Y
                k=abs(int((paddleE+paddleI)/2) - Y)-1
                if(k<0):
                    factX = 1
                else:
                    factX = int(k/2)+2
            elif Y<paddleI:
                finY = Y
                if vX>0:
                    if (Y+vX+1)>= paddleI:
                        finY = paddleI
                        finX = 31
                        k = int((paddleE-paddleI)/2)-1
                        factX = int(k/2)+2
                    else:
                        factX = -1
                else:
                    if (abs(vX)-Y+1) >=paddleI:
                        finY = paddleI
                        finX = 31
                        k = int((paddleE-paddleI)/2)-1
                        factX = int(k/2)+2
                    else:
                        factX = -1
            elif Y>paddleE:
                finY = Y
                if(vX<0):
                    if(Y+vX-1)<=paddleE:
                        finY = paddleE
                        finX = 31
                        k = int((paddleE-paddleI)/2)-1
                        factX = int(k/2)+2
                    else:
                        factX = -1
                else:
                    if(147-vX-Y)<=paddleE:
                        finY = paddleE
                        finX = 31
                        k = int((paddleE-paddleI)/2)-1
                        factX = int(k/2)+2
                    else:
                        factX = -1
            if(factX == -1):
                factY = int((paddleI+paddleE)/2)
            return 1,finX,finY,factY,factX
        if(strt < 0):
            strt = 0
        for i in range(strt,Y+1):
            if((X-1)==0):
                brickUp = 1
            else:
                if(isinstance(self.components[X-1][i],(Brick,DynamicBrick,FixedBrick))):
                    brickUp = 1
                    brickUpI = i
            if((X+1)==32):
                brickBelow = 1
            elif X!=32:
                if(isinstance(self.components[X+1][i],(Brick,DynamicBrick,FixedBrick))):
                    brickBelow = 1
                    brickBelowI = i
        if vX>0 and vY>0:
            if X>1 and Y<74:
                if isinstance(self.components[X-1][Y+1],(Brick,DynamicBrick,FixedBrick)):
                    if brickUp !=1 and not(isinstance(self.components[X][Y+1],(Brick,DynamicBrick,FixedBrick))):
                        brickUp = 1
                        brickUpI = Y+1
                        ifchnge = self.components[X-1][Y+1].getHit(ball)
                        if ifchnge == 1:
                            woahX = X-1
                            woahY = Y+1
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        return 2,X,Y,1,1
        elif vX<0 and vY>0:
            if X>1 and Y>5:
                if isinstance(self.components[X-1][Y-5],(Brick,DynamicBrick,FixedBrick)):
                    if brickUp !=1 and not(isinstance(self.components[X][Y-5],(Brick,DynamicBrick,FixedBrick))):
                        brickUp = 1
                        brickUpI = Y-1
                        ifchnge = self.components[X-1][Y-5].getHit(ball)
                        if ifchnge == 1:
                            woahX = X-1
                            woahY = Y-5
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        return 2,X,Y,1,1

        elif vX>0 and vY<0:
            if X<30 and Y<74:
                if isinstance(self.components[X+1][Y+1],(Brick,DynamicBrick,FixedBrick)):
                    if brickBelow !=1 and not(isinstance(self.components[X][Y+1],(Brick,DynamicBrick,FixedBrick))):
                        brickBelow = 1
                        brickBelowI = Y+1
                        ifchnge = self.components[X+1][Y+1].getHit(ball)
                        if ifchnge == 1:
                            woahX = X+1
                            woahY = Y+1
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        return 2,X,Y,1,1
        elif vX<0 and vY<0:
            if X<30 and Y>5:
                if isinstance(self.components[X+1][Y-5],(Brick,DynamicBrick,FixedBrick)):
                    if brickBelow !=1 and not(isinstance(self.components[X][Y-5],(Brick,DynamicBrick,FixedBrick))):
                        brickBelow = 1
                        brickBelowI = Y-1
                        ifchnge = self.components[X+1][Y-5].getHit(ball)
                        if ifchnge == 1:
                            woahX = X+1
                            woahY = Y-5
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        return 2,X,Y,1,1
        
        #for i in range(Y+1,75):
        #    if(isinstance(self.components[X][i],(Brick,FixedBrick,DynamicBrick))):
        #        brickSameR = i
        #        break
        #for i in range(Y-1,-1,-1):
        #    if(isinstance(self.components[X][i],(Brick,FixedBrick,DynamicBrick))):
        #        brickSameL = i
        #        break
        if(vY > 0):
            if(brickUp == 1 ):
                finX = X+1
                revertY = 1
                if(brickUpI != " "):
                    ifchnge = self.components[X-1][brickUpI].getHit(ball)
                    if ifchnge == 1:
                        woahX = X-1
                        woahY = brickUpI
                        streng = self.components[woahX][woahY].getStrength()
                        if streng == 4:
                            self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                            globals.BreakableBricks -= 1
                        elif streng == -1:
                            self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                        else:
                            self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                    #if(self.components[X-1][brickUpI].getStrength() == 0):
                    #    self.components[X-1][brickUpI] = " "
                if(brickBelow == 1):
                    finX = X
                    revertY = random.choices([0,1])
                    revertY = revertY[0]
                    if(brickBelowI != " "):
                        ifchnge = self.components[X+1][brickBelowI].getHit(ball)
                        if ifchnge == 1:
                            woahX = X+1
                            woahY = brickBelowI
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        #if(self.components[X+1][brickBelowI].getStrength() == 0):
                        #    self.components[X+1][brickBelowI] = " "
                    #rightBound = brickSameR
                    #leftBound = brickSameL
                #else:
                #    for i in range(Y+1,brickSameR):
                #        if(isinstance(self.components[X+1][i],(Brick,FixedBrick,DynamicBrick))):
                #            rightBound = i
                #            break
                #    for i in range(Y-1,brickSameL,-1):
                #        if(isinstance(self.components[X+1][i],(Brick,FixedBrick,DynamicBrick))):
                #            leftBound = i
                #            break
            else:
                finX = X-1
                revertY = 0
                #for i in range(Y+1,brickSameR):
                #    if(isinstance(self.components[X-1][i],(Brick,FixedBrick,DynamicBrick))):
                #        rightBound = i
                #        break
                #for i in range(Y-1,brickSameL,-1):
                #    if(isinstance(self.components[X-1][i],(Brick,FixedBrick,DynamicBrick))):
                #        leftBound = i
                #        break
        else:
            if(brickBelow == 1 ):
                finX = X-1
                revertY = 1
                if(brickBelowI != " "):
                    ifchnge = self.components[X+1][brickBelowI].getHit(ball)
                    if ifchnge == 1:
                        woahX = X+1
                        woahY = brickBelowI
                        streng = self.components[woahX][woahY].getStrength()
                        if streng == 4:
                            self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                            globals.BreakableBricks -= 1
                        elif streng == -1:
                            self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                        else:
                            self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                    #if(self.components[X+1][brickBelowI].getStrength() == 0):
                    #    self.components[X+1][brickBelowI] = " "
                if(brickUp == 1):
                    finX = X
                    revertY = random.choices([0,1])
                    revertY = revertY[0]
                    if(brickUpI != " "):
                        ifchnge = self.components[X-1][brickUpI].getHit(ball)
                        if ifchnge == 1:
                            woahX = X-1
                            woahY = brickUpI
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        #if(self.components[X-1][brickUpI].getStrength() == 0):
                        #    self.components[X-1][brickUpI] = " "
                    #rightBound = brickSameR
                    #leftBound = brickSameL
                #else:
                #    for i in range(Y+1,brickSameR):
                #        if(isinstance(self.components[X-1][i],(Brick,FixedBrick,DynamicBrick))):
                #            rightBound = i
                #            break
                #    for i in range(Y-1,brickSameL,-1):
                #        if(isinstance(self.components[X-1][i],(Brick,FixedBrick,DynamicBrick))):
                #            leftBound = i
                #            break
            else:
                finX = X+1
                revertY = 0
                #for i in range(Y+1,brickSameR):
                #    if(isinstance(self.components[X+1][i],(Brick,FixedBrick,DynamicBrick))):
                #        rightBound = i
                #        break
                #for i in range(Y-1,brickSameL,-1):
                #    if(isinstance(self.components[X+1][i],(Brick,FixedBrick,DynamicBrick))):
                #        leftBound = i
                #        break
        finY = Y
        for i in range(abs(vX)):
            if(vX > 0):
                finY+=1
            elif (vX < 0):
                finY-=1
            leftBound,rightBound,brickLX,brickRX = self.getBounds(X,finX,Y)
            #print("\033[40;1H")
            #print(str(rightBound)+"right"+str(leftBound)+"left"+str(brickLX)+"lx"+str(brickRX)+"rx"+str(X)+"X"+str(finX)+"finX"+str(Y)+"Y"+str(finY)+"finY")
            if(finY == rightBound):
                #print("Woah!!")
                revertX = 1 - revertX
                vX = 0-vX
                if(finY < 75):
                    if not(isinstance(self.components[brickRX][finY],(Paddle))):
                        ifchnge = self.components[brickRX][finY].getHit(ball)
                        if ifchnge == 1:
                            woahX = brickRX
                            woahY = finY
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        #if(self.components[brickRX][finY].getStrength() == 0):
                        #    self.components[brickRX][finY] = " "
                finY-=2
                if finY == leftBound:
                    finY +=1
            elif(finY == leftBound):
                revertX = 1-revertX
                vX=0-vX
                if(finY>=0):
                    if not(isinstance(self.components[brickLX][finY-4],(Paddle))):
                        ifchnge = self.components[brickLX][finY-4].getHit(ball)
                        if ifchnge == 1:
                            woahX = brickLX
                            woahY = finY-4
                            streng = self.components[woahX][woahY].getStrength()
                            if streng == 4:
                                self.components[woahX][woahY] = FixedBrick(woahX,woahY)
                                globals.BreakableBricks -= 1
                            elif streng == -1:
                                self.components[woahX][woahY] = ExplodingBrick(woahX,woahY)
                            else:
                                self.components[woahX][woahY] = DynamicBrick(woahX,woahY,streng)
                        #if(self.components[brickLX][finY].getStrength() == 0):
                        #    self.components[brickLX][finY] = " "
                finY+=2
                if(finY == rightBound):
                    finY-=1
        return 0,finX,finY,revertY,revertX 

    def initializeBoss(self):
        scre = "Score"
        for i in range(len(scre)):
            self.components[0][i] = scre[i]
        self.components[0][5] = ":"
        scre = "Lives"
        for i in range(len(scre)):
            self.components[0][i+32] = scre[i]
        self.components[0][37] = ":"
        scre = "Time"
        for i in range(len(scre)):
            self.components[0][i+61] = scre[i]
        self.components[0][65] = ":"
        for i in range(1,33):
            for j in range(75):
                self.components[i][j] = " "
        
        self.components[1][35] = FixedBrick(1,35)
        self.components[2][33] = FixedBrick(2,33)
        self.components[2][38] = FixedBrick(2,38)
        self.components[3][30] = FixedBrick(3,30)
        self.components[3][35] = FixedBrick(3,35)
        self.components[3][40] = FixedBrick(3,40)
        self.components[4][25] = FixedBrick(4,25)
        self.components[4][30] = FixedBrick(4,30)
        self.components[4][35] = FixedBrick(4,35)
        self.components[4][40] = FixedBrick(4,40)
        self.components[4][45] = FixedBrick(4,45)
        self.components[5][25] = FixedBrick(5,25)
        self.components[5][30] = FixedBrick(5,30)
        self.components[5][35] = FixedBrick(5,35)
        self.components[5][40] = FixedBrick(5,40)
        self.components[5][45] = FixedBrick(5,45)
        self.components[6][30] = FixedBrick(6,30)
        self.components[6][40] = FixedBrick(6,40)

        for i in range(9,18):
            curind = 0
            while curind<71:
                sel = random.choices([0,1], weights = [125,1])[0]
                if sel == 0:
                    curind +=1
                else:
                    self.components[i][curind] = FixedBrick(i,curind)
                    curind += 5

        self.components[32][32] = Paddle(32,32)
        globals.pedal = self.components[32][32]
        self.components[31][38] = Ball(31,38)
        #self.components[31][34] = Ball(31,34)
        globals.oldConfig = self.components.copy()
            


        
        

    def initializeBoard(self):
        scre = "Score"
        for i in range(len(scre)):
            self.components[0][i] = scre[i]
        self.components[0][5] = ":"
        scre = "Lives"
        for i in range(len(scre)):
            self.components[0][i+32] = scre[i]
        self.components[0][37] = ":"
        scre = "Time"
        for i in range(len(scre)):
            self.components[0][i+61] = scre[i]
        self.components[0][65] = ":"
        for i in range(1,16):
            curind = 0
            while curind<71:
                sel = random.choices([0,1,2,3,4,6], weights = [125, 1, 1, 1, 1, 1]) #add 5,1 in the corresponding arrays if adding exploding in general
                if sel[0] == 0 :
                    curind = curind + 1
                elif sel[0] == 1 :
                    self.components[i][curind]= DynamicBrick(i,curind,3)
                    curind = curind + 5
                    globals.BreakableBricks += 1
                elif sel[0] == 2 :
                    self.components[i][curind]= DynamicBrick(i,curind,2)
                    curind = curind + 5
                    globals.BreakableBricks += 1
                elif sel[0] == 3 :
                    self.components[i][curind]= DynamicBrick(i,curind,1)
                    curind = curind + 5
                    globals.BreakableBricks += 1
                elif sel[0] == 6:
                    self.components[i][curind]= RainbowBrick(i,curind)
                    curind = curind + 5
                    globals.BreakableBricks += 1
                else:
                    self.components[i][curind]= FixedBrick(i,curind)
                    curind = curind + 5  
                #to add exploding bricks to the general pane
                
                #elif sel[0] == 5:
                #    self.components[i][curind]= ExplodingBrick(i,curind)
                #    curind+=5
                #    globals.BreakableBricks +=1
        
        #for i in range(0,75,5):
        #    self.components[17][i]= FixedBrick(17,i)
        #    self.components[18][i]= ExplodingBrick(18,i)
        #    globals.BreakableBricks += 1
        
        #curind = 0
        #while curind<71:
        #    sel = random.choices([1,2,3], weights = [1, 1, 1])
        #    if sel[0] == 1 :
        #        self.components[19][curind]= DynamicBrick(19,curind,3)
        #        curind = curind + 5
        #        globals.BreakableBricks += 1
        #    elif sel[0] == 2 :
        #        self.components[19][curind]= DynamicBrick(19,curind,2)
        #        curind = curind + 5
        #        globals.BreakableBricks += 1
        #    elif sel[0] == 3 :
        #        self.components[19][curind]= DynamicBrick(19,curind,1)
        #        globals.BreakableBricks += 1
        #        curind = curind + 5
        
        #exploding brick test
        curind=5
        for i in range(17,23):
            sel = random.choices([1,2,3], weights = [1, 1, 1])
            if sel[0] == 1 :
                self.components[i][curind]= DynamicBrick(i,curind,3)
                curind = curind + 5
                globals.BreakableBricks += 1
            elif sel[0] == 2 :
                self.components[i][curind]= DynamicBrick(i,curind,2)
                curind = curind + 5
                globals.BreakableBricks += 1
            elif sel[0] == 3 :
                self.components[i][curind]= DynamicBrick(i,curind,1)
                globals.BreakableBricks += 1
                curind = curind + 5
            if i<22:
                self.components[i][curind] = ExplodingBrick(i,curind)
                globals.BreakableBricks += 1
                if i<21:
                    self.components[i][curind+5] = FixedBrick(i,curind+5)
                else:
                    self.components[i][curind+5] = ExplodingBrick(i,curind+5)
                    globals.BreakableBricks += 1

        

        curind=65
        for i in range(17,23):
            sel = random.choices([1,2,3], weights = [1, 1, 1])
            if sel[0] == 1 :
                self.components[i][curind]= DynamicBrick(i,curind,3)
                curind = curind - 5
                globals.BreakableBricks += 1
            elif sel[0] == 2 :
                self.components[i][curind]= DynamicBrick(i,curind,2)
                curind = curind - 5
                globals.BreakableBricks += 1
            elif sel[0] == 3 :
                self.components[i][curind]= DynamicBrick(i,curind,1)
                globals.BreakableBricks += 1
                curind = curind - 5
            if i<22:
                self.components[i][curind] = ExplodingBrick(i,curind)
                globals.BreakableBricks += 1
                if i<21:
                    self.components[i][curind-5] = FixedBrick(i,curind-5)



        
        self.components[32][32] = Paddle(32,32)
        globals.pedal = self.components[32][32]
        self.components[31][38] = Ball(31,38)
        #self.components[31][34] = Ball(31,34)
        globals.oldConfig = self.components.copy()




#      [|||][|||][|||]                                   [|||][|||][|||]
#           [|||][|||][|||]                         [|||][|||][|||]
#                [|||][|||][|||]               [|||][|||][|||]
#                     [|||][|||][|||]     [|||][|||][|||]
#                          [|||][|||][|||][|||][|||]
#                               [|||]     [|||]

import globals
import signal
import reset
from input import _GetchUnix,_Getch
from Board import Board
from Ball import Ball
from os import system
from time import sleep
from copy import deepcopy
from Brick import Brick
from Bullet import Bullet
import random
import time


class AlarmException(Exception):
    pass


system('clear')
canvas = Board()
globals.canvas = canvas
canvas.initializeBoard()

#getip = _GetchUnix()

testip = _Getch()


def alarmHandler(signum, frame):
    raise AlarmException


def iput():
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL,0.1)
    try:
        #text = getip()
        text = testip()
        signal.alarm(0)
        signal.setitimer(signal.ITIMER_REAL,0)
        return text
    except AlarmException:
        text = "n"
    signal.setitimer(signal.ITIMER_REAL,0)
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return 'n'


globals.Tme = time.perf_counter()
globals.levelStrtTime = time.perf_counter()
while(1 and globals.level !=4):              #and globals.level != 4
    canvas.displayBoard()


    print("\033[35;1H")
    c = iput()
    print("\033[35;1H")


    if c == "q":
        break
    elif c == "a" or c == "d":
        canvas.movePaddle(c)
    elif c == " ":
        for i in range(len(globals.balls)):
           if isinstance(globals.balls[i],(Ball)):
               if globals.balls[i].getBallStatus() == 0:
                   globals.balls[i].setBallStatus(1)
        if globals.shootingPowerUp != "" :
            canvas.generateBullet()
    elif c == "=":
        globals.level += 1
        if globals.level < 4:
            reset.reset()
            system('clear')
            canvas = Board()
            globals.canvas = canvas
            canvas.initializeBoard()
            globals.levelStrtTime = time.perf_counter()
            continue
        else:
            reset.reset()
            system('clear')
            canvas = Board()
            globals.canvas = canvas
            break
    
    for i in range(len(globals.balls)):
        if isinstance(globals.balls[i],(Ball)):
            if globals.balls[i].getBallStatus() == 1:
                canvas.finMoveBall(globals.balls[i],i)


    for i in range(len(globals.bullets)):
        if isinstance(globals.bullets[i],(Bullet)):
            tempVar = globals.bullets[i].moveBullet()
            if tempVar == -1:
                globals.bullets[i] = " "


    globals.left_exploding = deepcopy(globals.temp_left_exploding)
    globals.temp_left_exploding = []
    globals.right_exploding = deepcopy(globals.temp_right_exploding)
    globals.temp_right_exploding = []
    for i in range(len(globals.left_exploding)):
        if isinstance(canvas.getComponent(globals.left_exploding[i][0],globals.left_exploding[i][1]),(Brick)) and canvas.getComponent(globals.left_exploding[i][0],globals.left_exploding[i][1]) != " ":
            canvas.getComponent(globals.left_exploding[i][0],globals.left_exploding[i][1]).getHit(" ",1)
    for i in range(len(globals.right_exploding)):
        if isinstance(canvas.getComponent(globals.right_exploding[i][0],globals.right_exploding[i][1]),(Brick)) and canvas.getComponent(globals.right_exploding[i][0],globals.right_exploding[i][1]) != " ":
            canvas.getComponent(globals.right_exploding[i][0],globals.right_exploding[i][1]).getHit(" ",1)
    #print("\033[40;1H")
    #print(globals.canvas.getComponent(21,35))
    
    #print(canvas.getComponent(21,35))
    for i in range(len(globals.powerUp)):
        if globals.powerUp[i].getStatus() == 1:
            if int(time.perf_counter() - globals.powerUp[i].getTme()) >=15:
                globals.powerUp[i].becomeInActive()
        if globals.powerUp[i].getStatus() == 0:
            globals.powerUp[i].movePowerUp()

    if globals.BreakableBricks == 0:
        # canvas.displayBoard()
        # print("\033[36;1H You Successfully broke all the bricks in the given number of lives, Have a nice day!!!")
        # break
        if globals.level == 3:
            globals.level += 1
            reset.reset()
            system('clear')
            canvas = Board()
            globals.canvas = canvas
            break
        elif globals.level == 4:
            canvas.displayBoard()
            globals.level += 1
            print("\033[36;1H You Successfully broke all the bricks in the given number of lives, Have a nice day!!!")
            break
        else:
            globals.level += 1
            reset.reset()
            system('clear')
            canvas = Board()
            globals.canvas = canvas
            canvas.initializeBoard()
            globals.levelStrtTime = time.perf_counter()

    if globals.fallBrick == 0:
        if int(time.perf_counter() - globals.levelStrtTime)>=30:
            globals.fallBrick = 1 
    
    if globals.endGame == 1:
        print("\033[36;1H Game Over, Have a nice day!!!")
        break

    if globals.Lives <= 0:
        canvas.displayBoard()
        print("\033[36;1H Game Over, Have a nice day!!!")
        break
if globals.level == 4 and globals.pressed == 0:
    canvas = globals.canvas
    canvas.initializeBoss()
    globals.levelStrtTime = time.perf_counter()
    prev = -1
    while(1):
        canvas.displayBoard()


        print("\033[35;1H")
        c = iput()
        print("\033[35;1H")


        if c == "q":
            break
        elif c == "a" or c == "d":
            canvas.movePaddle(c)
            canvas.moveBoss(c)
        elif c == " ":
            for i in range(len(globals.balls)):
               if isinstance(globals.balls[i],(Ball)):
                   if globals.balls[i].getBallStatus() == 0:
                       globals.balls[i].setBallStatus(1)
            if globals.shootingPowerUp != "" :
                canvas.generateBullet()
        elif c == "=":
            if globals.level != 4:
                if globals.pressed == 0:
                    globals.level = 4
                    globals.pressed = 1
            else:
                if globals.pressed!=1:
                    globals.level += 1
                    print("\033[36;1H Game Over, Have a nice day!!!")
                    break

        for i in range(len(globals.balls)):
            if isinstance(globals.balls[i],(Ball)):
                if globals.balls[i].getBallStatus() == 1:
                    canvas.finMoveBall(globals.balls[i],i)

        for i in range(len(globals.bullets)):
            if isinstance(globals.bullets[i],(Bullet)):
                tempVar = globals.bullets[i].moveBullet()
                if tempVar == -1:
                    globals.bullets[i] = " "     
        val = random.choices([2,3,5,7,11])[0]
        newPrev = int(time.perf_counter()-globals.levelStrtTime)
        if newPrev!= prev:
            prev = newPrev
            if newPrev%val == 0:
                canvas.dropBombBoss()

        for i in range(len(globals.balls)):
            if isinstance(globals.balls[i],(Ball)):
                break

        if globals.bossHealth <=33 and globals.trigger == 2 and globals.balls[i].xCor >20:
            globals.trigger -= 1
            canvas.spawnlayer() 
        
        if globals.bossHealth <=15 and globals.trigger == 1 and globals.balls[i].xCor >21:
            globals.trigger -= 1
            canvas.spawnlayer()

        if globals.bossHealth <= 0:
            globals.bossHealth = 0
            canvas.displayBoard()
            print("\033[36;1HCongratulations!! You made it to the end")
            break   

        if globals.Lives <= 0:
            globals.Lives = 0
            canvas.displayBoard()
            print("\033[36;1H Game Over, Have a nice day!!!")
            break

import globals
class Bullet:
    def __init__(self,x,y,speedY):
        self.symbol = "`"
        self.xCor = x
        self.yCor = y
        self.ySpeed = speedY
        globals.bullets.append(self)
    def updateCords(self,x,y):
        self.xCor = x
        self.yCor = y
    def moveBullet(self):
        x = globals.canvas.moveBullet(self.xCor,self.yCor,self.ySpeed,self)
        return x
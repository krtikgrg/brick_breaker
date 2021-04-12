import globals
import time
def reset():
    globals.BreakableBricks = 0
    globals.Number_Of_Balls = 0
    globals.moveBall = 0
    globals.oldConfig = ""
    globals.canvas = ""
    globals.pedal = ""
    globals.powerUp = []
    globals.balls = []
    globals.left_exploding = []
    globals.right_exploding = []
    globals.temp_left_exploding = []
    globals.temp_right_exploding = []
    globals.shootingPowerUp = ""
    globals.levelStrtTime = time.perf_counter()
    globals.fallBrick = 0
    globals.endGame = 0
    globals.bullets = []

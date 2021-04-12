BRICK = "[|||]"
PADDLE = "^===========^"
PADDLEEXTENDED = "^===============^"
PADDLESHRINKED = "^=======^"
PADDLEFIRE = "/\\=========/\\"
PADDLEFIREEXTENDED = "/\\=============/\\"
PADDLEFIRESHRINKED = "/\\=====/\\"
BALL = "@"
HIGH = "\033[0;34m"
MEDIUM = "\033[0;32m"
LOW = "\033[0;36m"
STONE = "\033[0;37m"
WHITE = "\033[1;37m"


Tme = 0
Score = 0
Lives = 60
BreakableBricks = 0


Number_Of_Balls = 0
moveBall = 0
oldConfig = ""


canvas = ""
pedal = ""
powerUp = []
shootingPowerUp = ""
balls = []
left_exploding = []
right_exploding = []
bullets = []

temp_left_exploding = []
temp_right_exploding = []

level = 1
levelStrtTime = ""
fallBrick = 0
endGame = 0
pressed = 0
bossHealth = 50
trigger = 2

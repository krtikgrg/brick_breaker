# Déjà vu - Brick Breaker
## This game is a terminal based version of the classic brick breaker game with almost all of the functionality implemented.
1. Total 6 types of bricks - Fixed (Unbreakable,White Color is used for this), Dynamic Blue Colored Brick, Dynamic Green Colored brick, Dynamic Cyan Colored Brick, Rainbow Brick and Yellow Explosive Brick
1. Blue Brick Changes to Green Brick on a hit and Green Brick Changes to Cyan Brick on getting hit.
1. Cyan Brick Ultimately vanishes on a hit.
1. Explosive Yellow Colored Brick on Hit will cause all of the adjacent Bricks to explode.
1. Rainbow brick on hit changes to any of the other 5 bricks and behaves accordingly.
1. I have Seven PowerUps implemented which are Expand Paddle(+), Shrink Paddle(-), Thru Ball(/), Fast Ball(>), Multi Ball(%), Paddle Grab(#), Shooting Paddle(!)

## What each file contains
1. __main.py__ : This is the file with the main loop of the Code.
1. __globals.py__ : This file contains the necessary global variables that i require so as to avoid the creation of multiple copies thereby saving space.
1. __Board.py__ : This Canvas of the game that is the Board which is Displayed is implemented in this file. All the functionalities related to the Board are implemented in here like moving the ball on the canvas, moving powerups, moving paddle, collision handling etc.
1. __Ball.py__ : This is file containing the Ball class, it contains the functions related to the Balls like moving it, updating the coordinates etc.
1. __PowerUp.py__ : This file implements the PowerUp class and all its inherited classes. Further using the concepts of encapsulation and Polymorphism.
1. __Paddle.py__ : As the name suggests this file is Paddle class.
1. __Brick.py__ : This file implements the Brick class and all of its inherited classes.
1. __input.py__ : This file is responsible for scanning the terminal input.
1. __Bullet.py__ : This is the bullet class, basically for lasers from the paddle and for the bombs from the boss.
1. __reset.py__ : This is the reset file, it is used to reset all the variable when moving on from one level to another.
1. __Hit.mp3__ : The sound effect for collision with bricks of ball. Also the collision of the bullet with the brick.


## All the components of the game are implemented as Objects and Classes and all the functionality is made to happen through functions of these objects, thereby obeying the principles of Object Oriented Programming

## To Run the game
1. Open the directory in terminal
1. Run "python3 main.py"
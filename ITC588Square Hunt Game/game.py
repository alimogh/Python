import turtle
import threading
import random
import math
import sys
import time

# Global Variables
BOTTOM_GRID_X = -300
BOTTOM_GRID_Y = -325
GRID_LW = 600
START_LLEFT_X = -30
START_LLEFT_Y = 300
START_WIDTH = 58
START_HEIGHT = 20
SCORE = 0
COUNT = 0
START = 0
ableClick = 1

# Main Function
def main():
    setup_screen()
    draw_title()
    draw_start()
    draw_score()
    draw_grid()
    select_dificulty()

def setup_screen():
    # Disable animations and hide turtle
    turtle.hideturtle()
    turtle.speed(0)
    turtle.title("Square Hunt by David Arnold")
    turtle.setup(700, 760) # Setup screen
    turtle.penup() # Raise turtle pen

def draw_title():
    turtle.goto(-300, 300)
    turtle.write("Square Hunt by David Arnold", False, align="Left", font=("Arial"))

def draw_start():
    turtle.goto(START_LLEFT_X, START_LLEFT_Y)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(3)
    turtle.fillcolor("green")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(START_WIDTH)
        turtle.left(90)
        turtle.forward(START_HEIGHT)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 300)
    turtle.write("START", False, align="center", font=("Arial"))

def draw_count():
    turtle.goto(0, 300)
    turtle.pencolor("black")
    turtle.write(f"[{COUNT}]", False, align="center", font=("Arial"))

def draw_score():
    turtle.goto(210,285)
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    
    turtle.goto(300, 300)
    turtle.pencolor("black")
    turtle.write(f'SCORE: {SCORE}', False, align="right", font=("Arial"))

def draw_grid():
    global gridDivider
    validInput = True
    while validInput is True:
        gridInputSize = int(turtle.textinput("Grid Size", "Please select grid size between 3-8: "))
        if gridInputSize >= 3 and gridInputSize <= 8:
            gridDivider = GRID_LW // gridInputSize
            turtle.goto(BOTTOM_GRID_X, BOTTOM_GRID_Y)
            turtle.pendown()
            turtle.pencolor("black")
            turtle.pensize(3)
            # Loop to draw border
            for i in range(4):
                turtle.forward(GRID_LW)
                turtle.left(90)
            # Loop to draw vertical grid markings
            turtle.goto(BOTTOM_GRID_X, BOTTOM_GRID_Y)
            for i in range(gridInputSize - 1):
                turtle.forward(gridDivider)
                turtle.left(90)
                turtle.forward(GRID_LW)
                turtle.back(GRID_LW)
                turtle.right(90)
            # Loop to draw horizontal markings
            turtle.goto(BOTTOM_GRID_X, BOTTOM_GRID_Y)
            for i in range(gridInputSize - 1):
                turtle.left(90)
                turtle.forward(gridDivider)
                turtle.right(90)
                turtle.forward(GRID_LW)
                turtle.back(GRID_LW)
            turtle.penup()
            validInput = False

def select_dificulty():
    global speed
    validInput = True
    while validInput is True:
        difficulty = int(turtle.textinput("Select Difficulty", "Choose a difficulty level (1-3):"))
        if difficulty == 1:
            speed = 2500
            validInput = False
        elif difficulty == 2:
            speed = 2000
            validInput = False
        elif difficulty == 3:
            speed = 1500
            validInput = False
        else:
            validInput = True

def handle_click(x, y):
    global START,target_x,target_y, gridDivider,SCORE,COUNT,ableClick 
    turtle.goto(x, y)
    if (turtle.xcor() >= START_LLEFT_X and turtle.xcor() <= (START_LLEFT_X + START_WIDTH)
    and turtle.ycor() >= START_LLEFT_Y and turtle.ycor() <= (START_LLEFT_Y + START_HEIGHT)) and START == 0:
        turtle.goto(START_LLEFT_X, START_LLEFT_Y)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(START_WIDTH)
            turtle.left(90)
            turtle.forward(START_HEIGHT)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        draw_square()
        START = 1
        print(START)
    elif START ==1 and ableClick ==1:
        if (target_x-10 <= x and target_x +  gridDivider >= x) and  (target_y-10 <= y and target_y+gridDivider >= y):
            SCORE +=1
            draw_score()
            
            turtle.goto(target_x, target_y)
            turtle.fillcolor("red")
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(gridDivider-20)
                turtle.left(90)
            turtle.end_fill()
            ableClick = 0
            
        else:
            #if(target_x-10 <= -300 or target_x +  gridDivider >= 300) or  (target_y-10 <= -325 or target_y+gridDivider >= 275):
             #   print("nothing change")
             #   ableClick = 1
            #else:    
                COUNT = COUNT+1
                turtle.goto(target_x, target_y)
                turtle.fillcolor("white")
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(gridDivider-20)
                    turtle.left(90)
                turtle.end_fill() 
                update_count(COUNT)  
                
                if SCORE >=1 :
                    SCORE = SCORE-1
                    draw_score()  
                ableClick = 0    

def update_count(COUNT):
    global START
    turtle.goto(-40,285)
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    
    turtle.pencolor("black")
    turtle.goto(0, 300)
    if COUNT < 10:
        turtle.write(f"[{COUNT}]", False, align="center", font=("Arial"))
    else:
        turtle.pencolor("red")
        turtle.write("Game Over", False, align="center", font=("Arial"))
        START = 0

def draw_square():
        global targetLW, target_x, target_y, COUNT, speed,START,ableClick
        ableClick = 1
        targetLW = gridDivider - 20
        if START == 1:
            turtle.goto(target_x, target_y)
            turtle.fillcolor("white")
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(targetLW)
                turtle.left(90)
            turtle.end_fill()
        
        target_x = random.randrange(-300, (300 - gridDivider), gridDivider) + 10
        target_y = random.randrange(-325, (275 - gridDivider), gridDivider) + 10
        turtle.goto(target_x, target_y)
        #turtle.pen()
        turtle.fillcolor("green")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(targetLW)
            turtle.left(90)
        turtle.end_fill()
        
        if COUNT<10:
            turtle.ontimer(draw_square,speed)
        

def draw_hit():
    turtle.goto(target_x, target_y)

main()
turtle.listen()
turtle.onscreenclick(handle_click)
turtle.done()

#turtle.done()
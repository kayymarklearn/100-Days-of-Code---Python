2026-01-01 13:38

Status: Complete

Tags:  [[Day 20 - 21 - Class Inheritance & Slicing]]
[[Day 20 - 21 - Class Inheritance & Slicing (code)]]


## Code: Project Code
### *main.py*
```
from turtle import Screen

from snake import Snake

import time

from food import Food

from scoreboard import ScoreBoard

  

screen = Screen()

screen.setup(width=600, height=600)

screen.bgcolor("black")

screen.title("Snake Game")

screen.tracer(0)

  

snake = Snake()

food = Food()

scoreboard = ScoreBoard()

  
  

screen.listen()

screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "Right")

  
  

game_on = True

while game_on:

screen.update()

time.sleep(0.1)

snake.move()

  

#Detect collisions with food

if snake.head.distance(food) < 15:

food.refresh()

snake.extend()

scoreboard.increase_score()

#Detect collisions with wall

if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

game_on = False

scoreboard.game_over()

#Detect collisions with your own tail

for segment in snake.segments[1:]:

if snake.head.distance(segment) < 10:

game_on = False

scoreboard.game_over()

  

screen.exitonclick()
```

### *food.py*
```
from turtle import Turtle

import random

class Food(Turtle):

def __init__(self):

super().__init__()

self.shape("turtle")

self.penup()

self.shapesize(stretch_len=0.5, stretch_wid=0.5)

self.color("blue")

self.speed("fastest")

self.refresh()

def refresh(self):

random_x = random.randint(-280, 280)

random_y = random.randint(-280, 280)

self.goto(random_x, random_y)
```

### *snake.py*
```
from turtle import Turtle 

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90

DOWN = 270

LEFT = 180

RIGHT = 0

class Snake:

def __init__(self):

self.x_position = 0

self.segments = []

self.create_snake()

self.head = self.segments[0]

def create_snake(self):

for position in STARTING_POSITIONS:

self.add_segment(position)

  

def add_segment(self, position):

_ = Turtle(shape="square")

_.color("white")

_.penup()

_.goto(position)

self.segments.append(_)

  
  

def extend(self):

# add a new segment to the code

self.add_segment(self.segments[-1].position())

def move(self):

for seg_num in range(len(self.segments) - 1, 0, -1):

self.new_x = self.segments[seg_num - 1].xcor()

self.new_y = self.segments[seg_num - 1].ycor()

self.segments[seg_num].goto(self.new_x, self.new_y)

self.head.forward(20)

def up(self):

if self.head.heading() != DOWN:

self.head.setheading(UP)

def down(self):

if self.head.heading() != UP:

self.head.setheading(DOWN)

def left(self):

if self.head.heading() != RIGHT:

self.head.setheading(LEFT)

def right(self):

if self.head.heading() != LEFT:

self.head.setheading(RIGHT)
```

### *scoreboard.py*
```
from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Courier", 36, "normal")

  

class ScoreBoard(Turtle):

def __init__(self):

super().__init__()

self.score = 0

self.color("white")

self.penup()

self.goto(0, 290)

self.update_scoreboard()

self.hideturtle()

  

def update_scoreboard(self):

self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

  

def increase_score(self):

self.score += 1

self.clear()

self.update_scoreboard()

def game_over(self):

self.goto(0, 0)

self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
```



## References


2025-12-28 20:19

Status: Incomplete

Tags: [[Day 19 - Instances, State and Higher Order funcs]]
[[Day 19 - Projects]]

# Code snippets and Examples
### Event listeners and Higher order funcs
```
from turtle import Turtle, Screen

  

tom = Turtle()

screen = Screen()

  

def move_forward():

tom.forward(10)

  

screen.listen()

screen.onkey(key="space", fun=move_forward)

  
  

screen.exitonclick()
```

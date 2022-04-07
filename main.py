import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help


def drawSineCurve(my_turtle = None):
  for x in range(-360,361):
    y = math.sin(math.radians(x))
    my_turtle.goto(x,y)
  my_turtle.up()

def setupWindow(mywindow = None):
  mywindow.setworldcoordinates(-360, -1, 361, 1)
  mywindow.bgcolor("pink")

  
def setupAxis (myturtle = None):
  myturtle.up()
  myturtle.goto(-360, 0)
  myturtle.down()
  myturtle.goto(361,0)
  myturtle.up()
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.goto(0,1)
  myturtle.up()
  myturtle.goto(-360,0)
  myturtle.down()

  
  

def drawSineCurve(my_turtle = None):
  my_turtle.goto(-360,0)
  my_turtle.down()
  for x in range(-360,361):
    y = math.sin(math.radians(x))
    my_turtle.goto(x,y)
  my_turtle.up()
  
  
def drawCosineCurve(my_turtle = None):
  my_turtle.goto(-360,0)
  my_turtle.down()
  for x in range(-360, 361):
    y = math.cos(math.radians(x))
    my_turtle.goto(x,y)
  my_turtle.up()
   
def drawTangentCurve(my_turtle = None):
  my_turtle.goto(-360,0)
  my_turtle.down()
  for x in range(-360, 361):
    y = math.tan(math.radians(x))
    my_turtle.goto(x,y)
  my_turtle.up()


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
import turtle

def drawTee(myTurtle):
  myTurtle.forward(200)
  myTurtle.backward(50)
  myTurtle.right(90)
  myTurtle.backward(100)
  myTurtle.forward(50)
  myTurtle.right(90)
  myturtle.forward(150)
  
def drawFourTees(myTurtle):
  count = 0 
  while count < 4:
    myTurtle.drawTee()
    count = count + 1
  
pop = turtle.Turtle

turtle.exitonclick()

import turtle

 def make.triangle(myTurtle):  
        myTurtle.penup()
        myTurtle.pendown()
        myTurtle.goto(0,0)
        sidecount = 0 
        while sidecount < 3:  
                myTurtle.forward(100)
                myTurtle.right(120)
                sidecount = sidecount + 1

def drawMoreTriangles(myTurtle):
        count = 0
        while count < 4:
                myTurtle.penup()
                myTurtle.forward(10)
                myTurtle.pendown()
                drawTriangle(myTurtle)
count = count + 1

def drawTriAlligned(myTurtle):
        count = 0
        while count < 3:
                drawMoreTriangles(myTurtle)
                myTurtle.penup()
                myTurtle.goto(0,0)
                myTurtle.pendown()

count = count + 1
 
 myTurtle.penup()
        myTurtle.goto(0,0)
        myTurtle.pendown()
        myTurtle.left(260)
        number = 0
        while number < 3:
                drawMoreTriangles(myTurtle)
                myTurtle.penup()
                myTurtle.goto(0,0)
                number = number + 1

po = turtle.Turtle()

drawTriAlligned(po)

turtle.exitonclick()

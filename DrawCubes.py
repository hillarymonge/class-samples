import turtle

def drawTopRhombus(myTurtle):
  count = 0
  while count < 1:
    myTurtle.fillcolor("black")
    myTurtle.begin_fill()
    myTurtle.left(30)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(30)
    myTurtle.end_fill()
    count = count + 1
    
def drawRightRhombus(myTurtle):
    count = 0
    while count < 1:
      myTurtle.fillcolor("dark blue")
      myTurtle.begin_fill()
      myTurtle.left(90)
      myTurtle.forward(20)
      myTurtle.right(60)
      myTurtle.forward(20)
      myTurtle.right(120)
      myTurtle.forward(20)
      myTurtle.right(60)
      myTurtle.forward(20)
      myTurtle.end_fill()
      count = count + 1
      
def drawLeftRhombus(myTurtle):
  count = 0 
  while count < 1:
    myTurtle.fillcolor("light blue")
    myTurtle.begin_fill()
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.left(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.end_fill()
    count = count + 1      
    
zo = turtle.Turtle()

def make1toprow(myTurtle):
  count = 0 
  while count < 4:
    drawTopRhombus(zo)
    zo.penup()
    zo.forward(35)
    zo.pendown()
    count = count + 1

def make1rightsiderow(myTurtle):
  count = 0
  while count < 4:
    drawRightRhombus(zo)
    zo.penup()
    zo.left(150)
    zo.forward(35)
    zo.pendown()
    count = count + 1

def make1leftsiderow(myTurtle):
  count = 0
  while count < 4:
    drawLeftRhombus(zo)
    zo.penup()
    zo.right(90)
    zo.forward(35)
    zo.right(150)
    zo.pendown()
    count = count + 1

zo.speed(0)

def make1cuberow(myTurtle):
  make1toprow(zo)
  zo.penup()
  zo.goto(0,-20)
  zo.pendown()
  make1rightsiderow(zo)
  zo.penup()
  zo.goto(0,0)
  zo.right(150)
  zo.pendown()
  make1leftsiderow(zo)

def make2cuberow(myTurtle):
  zo.penup()
  zo.goto(18,10)
  zo.right(210)
  zo.pendown()
  make1rightsiderow(zo)
  zo.penup()
  zo.goto(18,30)
  zo.pendown()
  make1toprow(zo)
  zo.penup()
  zo.goto(18,30)
  zo.right(150)
  zo.pendown()
  make1leftsiderow(zo)

def make3cuberow(myTurtle):
  zo.penup()
  zo.goto(37,40)
  zo.right(210)
  zo.pendown()
  make1rightsiderow(zo)
  zo.penup()
  zo.goto(37,60)
  zo.pendown()
  make1toprow(zo)
  zo.penup()
  zo.goto(37,60)
  zo.right(150)
  zo.pendown()
  make1leftsiderow(zo)
  
def make4cuberow(myTurtle):
  zo.penup()
  zo.goto(54,70)
  zo.pendown()
  zo.right(210)
  zo.pendown()
  make1rightsiderow(zo)
  zo.penup()
  zo.goto(54,90)
  zo.pendown()
  make1toprow(zo)
  zo.penup()
  zo.goto(54,90)
  zo.right(150)
  zo.pendown()
  make1leftsiderow(zo)

def makecubepattern(myTurtle):
  make1cuberow(zo)
  make2cuberow(zo)
  make3cuberow(zo)
  make4cuberow(zo)

makecubepattern(zo)

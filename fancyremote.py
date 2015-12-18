import turtle
from Tkinter import *

def circle(myTurtle):
	myTurtle.circle(50)
	
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple but
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text ='right', command=lambda: shawn.right(90))
penup = Button(frame, text ='penup', command=lambda:shawn.penup())
pendown = Button(frame, text ='pendown', command=lambda:shawn.pendown())
makecircle = Button(frame, text='makecircle', command=lambda:shawn.circle(50))

# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
frame.pack()
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
makecircle.pack(side=LEFT)

turtle.exitonclick()

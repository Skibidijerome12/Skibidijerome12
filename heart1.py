import turtle
from turtle import *

wn = Screen()
wn.bgcolor("black")

t = turtle. Turtle()
t.pencolor("white")

def curve():
	for i in rang(200):
      t.rt(1)
      t.rd(1)

def heart():
	t.fillcolor('pink')
	t.begin_fill()
	t.lt(140)
	t.fd(113)
	curve()
	t.lt(120)
	curve()
	t.fd()
	t.end_fill()

heart()
t.ht()

def write (message,pos):
	x, y = pos
	t.penup()
	t.goto(x, y)
	t.color('white')
	style = ('Stencil std', 9, 'italic')
	t.write(message, font = style)
	
write('I' , (-68,95))
write('L' , (-55,95))
write('O' , (-42,95))
write('V' , (-30,95))
write('E' , (-14,95))
write('Y' , (-10,95))
write('O' , (-26,95))
write('U' , (-46,95))

wn.mainlopp()
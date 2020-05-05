# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

SQUARE 		= 4
TRIANGLE 	= 3
PENTAGON	= 5
HEXAGON		= 6


def screen_here():
	wn = turtle.Screen()
	wn.setup(width=0.7, height = 0.7)
	wn.bgcolor('lightgreen')
	wn.tracer(3)


def draw_shape(shape):

	if shape == 'square':
		turtle.color('red')
		for i in range(0,4):
			turtle.fd(400)
			turtle.lt(90)
		# turtle.fd(75)



screen_here()

# Square
turtle.color('lightgreen')
turtle.goto(-200, -200)
draw_shape('square')


# Circle
turtle.color('lightgreen')
turtle.setposition(0,-195)
turtle.color('darkred')
turtle.circle(195)

# Clock Face
class Quaters(turtle.Turtle):
	def __init__(self, shape, color, startx, starty):
		turtle.Turtle.__init__(self)
		self.shape(shape)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)

corr_quarter = [[-180,0], [0,180], [180,0], [0,-180]]
# j = 0
# for i in corr_quarter:
# 	turtle.color('lightgreen')
# 	turtle.setposition(i[0],i[1])
# 	turtle.color('black')
# 	turtle.shape('square')

sq_1  = Quaters('square', 'black', -180, 0)
sq_2  = Quaters('square', 'black', 0, 180)
sq_3  = Quaters('square', 'black', 180, 0)
sq_4  = Quaters('square', 'black', 0, -180)

sq_5  = Quaters('square', 'black', 155.8, 90)
sq_6  = Quaters('square', 'black', 90, 155.8)

sq_7  = Quaters('square', 'black', -90, 155.8)
sq_8  = Quaters('square', 'black', -155.8, 90)

sq_9  = Quaters('square', 'black', -155.8, -90)
sq_10  = Quaters('square', 'black', -90, -155.8)

sq_11  = Quaters('square', 'black', 90, -155.8)
sq_112  = Quaters('square', 'black', 155.8, -90)







while True:
	turtle.update()
	time.sleep(0.02)









# Junk:

		# Shape 
# # (y,x) and when Y plus is a minus
# s = turtle.Shape("compound")
# poly1 = ((0,200),(0, 0))
# s.addcomponent(poly1, "lightgreen", "blue")
# turtle.register_shape("myshape", s)
# turtle.shape("myshape")


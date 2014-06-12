# Polygon excercise from Week 0

# Name: Brendan Gassler

import math

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0


# This is where you put code to move bob

def square(turtle):
	for i in range(4):
		fd(turtle, 100)
		lt(turtle)

def polygon(turtle, length, n):
	angle  = 360/n
	genFunc(turtle, n, length, angle)
	"""for i in range(n):
		fd(turtle, length)
		lt(turtle, 360/n)"""

def circle(turtle, radius):
	polygon(turtle, (2*math.pi*radius)/360, 360)

def arc(turtle, radius, angle):
	tot_length = 2*math.pi*radius*angle/360
	n  = int(tot_length/3)+1
	step_length = tot_length/n
	step_angle = float(angle)/n
	genFunc(turtle, n, step_length, step_angle)
	"""for i in range(angle):
		fd(turtle, (2*math.pi*radius)/360)
		lt(turtle, 1)"""

def genFunc(turtle, n, length, angle):
	for i in range(n):
		fd(turtle, length)
		lt(turtle, angle)



#arc(bob, 50, 270)

#circle(bob, 100)

#polygon(bob, 40, 7)

#square(bob)


wait_for_user()					
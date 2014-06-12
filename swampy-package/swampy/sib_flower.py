# Flower excercise (4.2) from Week 0

# Name: Brendan Gassler

from sib_polygon import *

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()	
bob.delay = 0


def petal(turtle, radius, angle):
	for i in range(2):
		arc(turtle, radius, angle)
		lt(turtle, 180-angle) 

#petal(bob, 40, 60)

def flower(turtle, n, radius, angle):
	for i in range(n):
		petal(turtle, radius, angle)
		lt(turtle, 360/n)

flower(bob, 14, 300, 20)

wait_for_user()					


#1.
#-*-coding:utf8-*-
from swampy.TurtleWorld import*
import math
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001 # set turtle moving time 0.1 s



# for i in range(4):
# 	fd(bob,100)
# 	lt(bob)
# wait_for_user()

# t as the turtle draw square
# added length as the side length of the square


#把定義好的代碼用函數包裝起來encapsulation
def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)
# modified the square function make it to draw polygon

#把上述的square函數寫成polygon是針對其特性泛化 "generalization"
def polygon(t,length,n):
	"""draws a polygon which has side length as length, and side number as n.
	t is the passing augment in turtle"""
	n = int(n)
	# it should be very careful that the angle_turn must used flaot
	# otherwise the roundoff error would be significant as the n brcome larger!!! 
	angle_turn = 360.0/n
	for i in range(n):
		fd(t,length)
		lt(t,angle_turn)

# define the default turn angle is 1 degree
def arc(t,radius,arc_degree = 360):
	"""draws an arc with radius as radius and degree as arc_degree,
	default is 360 degrees which is equivlent to drawing a circle with
	radius = radius"""
	# set the defalut diagram is circle
	angle_turn = 1
	length = radius*angle_turn*math.pi/180
	circle_ratio = arc_degree/360.0
	for i in range(int(360/angle_turn*circle_ratio)):
		fd(t,length)
		lt(t,angle_turn)
####################################################################
#利用polyline這個函數重構了polygon和arc函數
#原本arc函數還是重複實現polygon的代碼
#但是polygon是繪出一個完整的正多邊型的函數，泛化成circle可以
def polyline(t,n,length,angle):
	"""Draws n line s】egments with the given length
	and angle (in degrees) between them. t is a turtle."""
	for i in range(n):
		fd(t,length)
		lt(t,angle)

def polygon(t,n,length):
	angle = 360/n
	# call polyline function and pass the specific angle into it 
	polyline(t,n,length,angle)

def refac_arc(t,radius,angle=360):
	#refactoring the old version circle function benefits from reusing the
	#code in ployline instead of rewriting a new one
	n = angle/1.0
	length = radius*math.pi/180
	polyline(t,int(n),length,1)
####################################################################
# square(bob,30)
# polygon(bob,4,100)
refac_arc(bob,200)
####################################################################
#						programming note
#	int type roundoff error, interface of function design

#4.12

#problem set
#p1 docstring has been finished 
#p2 ignored
#p3 didn't get the point of the question...

#practice 4-2 flower
#first construct a petal function...
# One may use pu (pen up) or pd (pen down) function to achevie the goal...
# but it's may not necessary
def petal()













wait_for_user()

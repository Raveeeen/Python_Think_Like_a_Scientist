#1.
#-*-coding:utf8-*-
from swampy.TurtleWorld import*
import math
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005 # set turtle moving time 0.1 s



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
# refac_arc(bob,200)
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

#以下打算先設計一個函數能用扇形的弧長來模擬花瓣
#1.先轉角度
def single_petal(t):
	#inital start angle set to zero 
	arc_angle = 90
	step = 1 
	shape_ratio = math.sin(arc_angle/2*(math.pi/180))/arc_angle
	r = 3/math.sin(arc_angle/2*math.pi/180)/2 #set the axis of petal as a constant thus r should change with angle
	delta_arc = r*step
	for i in range(int(arc_angle/step)):
		fd(t,delta_arc)	#move the turtle a step 
		lt(t,step)	#turn left a step of angle
	lt(t,180-arc_angle) # set the proper angle prepare for the another side of petal
	for i in range(int(arc_angle/step)):
		fd(t,delta_arc)
		lt(t,step)
lt(bob,30)
single_petal(bob)

# another problem occured is how to design the proper ratio between 
# from the geometry properties the arc_angle more large would result in widder petal
# and to the larger radius would result in longer petal 

# according to the geometry properties we could find out that the shpae ratio
# of the petal could be confirmed by length_axis/length_arc = sin(theta/2)/theta
# given a ratio we can choose the anglg of arc we need.
# because we wish to set the length of axis r*sin(theta) as a constant
# therefore with different angle we need adjust r automatically. 











wait_for_user()

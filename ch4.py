#-*-coding:utf8-*-
from swampy.TurtleWorld import*
import math
#建立視窗
# world = TurtleWorld()
# #建立烏龜
# bob = Turtle()
# print bob
#1


# #move forward direction
# fd(bob,100) 
# #turn left
# lt(bob)
# #move forward 100 again
# fd(bob,100)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001 # set turtle moving time 0.1 s
# Made Bob to draw a square 



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
	n = int(n)
	# it should be very careful that the angle_turn must used flaot
	# otherwise the roundoff error would be significant as the n brcome larger!!! 
	angle_turn = 360.0/n
	for i in range(n):
		fd(t,length)
		lt(t,angle_turn)

# define the default turn angle is 1 degree
def arc(t,radius,arc_degree = 360):
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
	for i in range(n):
		fd(t,length)
		lt(t,angle)

def polygon(t,n,length):
	angle = 360/n
	# call polyline function and pass the specific angle into it 
	polyline(t,n,length,angle)

def refac_arc(t,radius,angle):
	# must use polyline function to refactor original arc function
	n = angle/1.0
	length = radius*math.pi/180
	polyline(t,int(n),length,1)
####################################################################
# square(bob,30)
# polygon(bob,4,100)
refac_arc(bob,20,270)

















wait_for_user()

#-*-coding:utf8-*-

"""
求模操作符
% 
/
求餘商
"logical operator : and or not"
conditional structure and statement 
"""

#conditional branch
x = 6
# if x%2 == 0:
	# print 'x is even'
# else:
	# print 'x is odd'

#chained conditional 
y = 8
# if (x < y):
	# print 'x is less than y'
# elif (x > y):
	# print 'x is greater than y'
# else:
	# print 'x and y are equal'
# nested conditioanl statement

if x == y: 
	print 'x and y are equal'
else :
	if x < y:
		print 'x is less than y'
	else:
		print 'x is greater than y'
	#過多的嵌套會讓代碼難以閱讀, 多重的if條件盡可能使用邏輯運算符and取代
	
#recursive
def countdown(n):
	if n <= 0:
		print 'Blastoff!'
	else:
		print n
		countdown(n-1)
		#switch the order in the else clause would reverse the execute flow in stack
def print_n(s,n):
	if n <= 0:
		print "iteration is done"
	print s
	print_n(s,n-1)
#practice 5-1(ignored),5-2
s = 'this is a test string' 
#you can't ignored this declaration otherwise the following function would miss a augment
def print_hello(s):
	print s
def do_n(f,n):
	if n <=0:
		return None
	f(s)
	do_n(f,n-1)
#keyboard keying function
#raw_input, input 

#problem 5.14
#5-3
def check_fermat(a,b,c,n):
	if n > 2 and a**n + b**n == c**n:
		print 'OMG Fermat is wrong!'
	print 'Fermat is still right~~'
def trial_fermat():
	a = raw_input('Please input a in check_fermat\n')
	b = raw_input('Please input b in check_fermat\n')
	c = raw_input('Please input c in check_fermat\n')
	n = raw_input('Please input n in check_fermat\n')
	check_fermat(int(a),int(b),int(c),int(n))
#5-4
def is_triangle(a,b,c,n=3):
	if a == 0 or b == 0 or c == 0:
		print "zero length is not allowable!!"
		return False
	if n == 0:
		n = 3 # reset n due to the python will not reset this value automatically
		print "this is a set of sides of a triangle"
		return True
	if a > b + c:
		n = 3 # same as above
		print "this is not a set of sides of a triangle"
		return  False
	is_triangle(c,a,b,n-1)	
def input_triangle_side():
	a = raw_input('Please input the first number as a side of a triangle\n')
	b = raw_input('Please input the second number as a side of a triangle\n')
	c = raw_input('Please input the third number as a side of a triangle\n')
	a = int(float(a)); b = int(float(b)); c = int(float(c))
	is_triangle(a,b,c)
#5-5

def draw_s(t,length,n):
	"""
	it'll draw two branch node tree, and n descirbe node deep 
	of the tree. (focus on the base case then look at the general pattern 
		of the function avoid thinking straightly when you want to understand
		how the recursive work)
	"""
	if n==0:
		return
	angle = 50 
	fd(t, length*n)
	lt(t,angle)
	draw_s(t,length,n-1)
	rt(t,2*angle)
	draw_s(t,length,n-1)	
	lt(t,angle)
	bk(t,length*n)
from swampy.TurtleWorld import*
import math as m
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.05 # set turtle moving time 0.1 s

#5-6 Koch curve
def Koch_Curve(t,x):
	if x <= 2.5:
		fd(t,2.5)
		return None
	Koch_Curve(t,float(x)/3)
	lt(t,60)
	Koch_Curve(t,float(x)/3)
	rt(t,120)
	Koch_Curve(t,float(x)/3)
	lt(t,60)
	Koch_Curve(t,float(x)/3)
def SnowFlake(t,x):
	Koch_Curve(t,x)
	rt(t,120)
	Koch_Curve(t,x)
	rt(t,120)
	Koch_Curve(t,x)
	rt(t,120)
# pu(bob)	
# lt(bob,180)
# fd(bob,200)
# lt(bob,180)
# pd(bob)
num_iteration = SnowFlake(bob,450)
print num_iteration 



